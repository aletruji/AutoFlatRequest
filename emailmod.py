import os
import smtplib
from email import policy
from email.message import EmailMessage
from email.parser import BytesParser
import modul
from imapclient import IMAPClient, imapclient
import os
from dotenv import load_dotenv
import subprocess
import logging
import datetime
import time
from bs4 import BeautifulSoup


load_dotenv()
imap_gmx = "imap.gmx.net"
mail_passwort = os.getenv("mail_passwort")
mail_account_login = os.getenv("mail_account_login")
mail_account_receive = os.getenv("mail_account_receive")
SMTP_SERVER = 'mail.gmx.net'
SMTP_PORT = 587

mailbox = "Inbox"
SUBJECT_KEYWORD = "Neues Mietangebot passend zu Ihrer Suche!"
CONFIRM_KEYWORD = "Bewerbung verschickt"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_monitor_idle.log"),
        logging.StreamHandler()
    ]
)
def is_within_time_window(start_hour=0, end_hour=23):
    now = datetime.datetime.now()
    current_hour = now.hour
    weekday = now.weekday()  # Montag=0, Sonntag=6
    if 0 <= weekday <= 6 and start_hour <= current_hour < end_hour:
        return True
    return False

def extract_links_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links


def execute_script():
    try:
        logging.info("Führe Skript aus: main.py")
        script_name = "main.py"
        #hier die html funktion einfügen
        #subprocess.run(['python', script_name], check=True)
        logging.info("Funktion erfolgreich ausgeführt.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler beim Ausführen des Skripts: {e}")


def monitor_emails():
    while True:

        if is_within_time_window():

            with imapclient.IMAPClient(imap_gmx) as server:
                server.login(mail_account_login, mail_passwort)
                server.select_folder('INBOX', readonly=False)

                # Suche nach ungelesenen E-Mails mit dem gewünschten Betreff
                messages = server.search(['UNSEEN', 'SUBJECT', SUBJECT_KEYWORD])
                for uid in messages:
                    print("hier1")
                    raw_message = server.fetch(uid, ['RFC822'])[uid][b'RFC822']
                    email_message = BytesParser(policy=policy.default).parsebytes(raw_message)

                    # Hier kannst du den Inhalt der E-Mail weiter verarbeiten, falls nötig

                    # Markiere die E-Mail als gelesen
                    #server.add_flags(uid, [imapclient.SEEN])
                    html_content = None
                    for part in email_message.walk():
                        if part.get_content_type() == "text/html":
                            html_content = part.get_payload(decode=True).decode(part.get_content_charset())
                            break  # Nur den ersten HTML-Teil verwenden

                    if html_content:
                        # Links extrahieren
                        links = extract_links_from_html(html_content)
                        if links:
                            # Ersten Link verwenden, oder alle Links weitergeben
                            first_link = links[0]
                            #print("Erster Link:", first_link)

                            # Hier kann der Link weiterverarbeitet werden, z.B. für die send_email-Funktion
                            # send_email(first_link)  # Falls send_email einen Link als Argument akzeptiert

                    # Führe die gewünschte Funktion aus
                    send_email()
                    print("email send   ...")
                    modul.threadining(first_link)
                    print("threading abgesendet")


        # Warte eine bestimmte Zeit, bevor erneut geprüft wird (z. B. 60 Sekunden)
        time.sleep(15)




def send_email():
    msg = EmailMessage()
    msg['Subject'] = CONFIRM_KEYWORD
    msg['From'] = mail_account_login
    msg['To'] = mail_account_receive
    msg.set_content("Bewerbung abgeschlossen !")  #"Es wurde erfolgreich eine Bewerbung abgeschlossen!")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(mail_account_login, mail_passwort)
        smtp.send_message(msg)



if __name__ == "__main__":
    monitor_emails()