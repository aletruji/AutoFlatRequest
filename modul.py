from webside import Gewobag
import json
from threading import Thread
import time

def threadining(link):

    threads = []

    for _ in range(count_applicants()):
        thread = Thread(target=database, args=(link,))
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()

def count_applicants():
    with open("datenbank.json", "r") as js:
        daten = json.load(js)

    # Zähle die Anzahl der Bewerber
    num_applicants = len(daten.get("applicants", []))
    return num_applicants

inn = 0
def database(link):
    link = link
    with open("datenbank.json", "r") as js:
        daten = json.load(js)

    appli_list = daten.get("applicants", [])


    for j in range(count_applicants()):
        global inn
        # i know not beautiful but i couldn't solve it
        first_name = appli_list[inn].get("first_name")
        last_name = appli_list[inn].get("last_name")
        email = appli_list[inn].get("email")
        sex = appli_list[inn].get("sex")
        num_persons = appli_list[inn].get("num_persons")
        inn += 1
        h = Gewobag(first_name, last_name, email, sex, num_persons, link)
        h.completeFunction()




if __name__ == "__main__":
    pass

