import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Gewobag:

    def __init__(self, first_name, last_name, email, sex, num_persons, link):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.num_persons = num_persons
        self.sex = sex
        self.link = link
        self.driver = webdriver.Chrome()        # Initialisiere den Chrome WebDriver

    def openDriver(self):

        self.driver.get(self.link)  # Öffne eine Webseite

    def cookie_button(self):

        button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "_brlbs-btn-accept-all"))
        )
        while button.is_displayed():
                # Klicke auf den Button  cookies button
                button.click()

                time.sleep(1)


    def anfrage_button(self):

        button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "rental-contact"))
        )
        # Klicke auf den Button   Anfrage senden 1 button

        button.click()



    def iframe_wechsel(self):
        WebDriverWait(self.driver, 10).until((EC.frame_to_be_available_and_switch_to_it((By.ID, "contact-iframe"))))
        # in iframe wechseln

    def choose_sex(self):
        nz_select = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "nz-select[formcontrolname='salutation']"))
        )
        nz_select.click()



        # Warte, bis die Dropdown-Option "Herr" sichtbar ist, und klicke darauf
        xpath = f"//li[contains(@class, 'ant-select-dropdown-menu-item') and text()='{self.sex}']"
        option_sex = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath))
        )
        option_sex.click()
    def selectAngehoerige(self):

        nz_select = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "nz-select[placeholder='Bitte wählen']"))
        )
        nz_select.click()



        # Warte, bis die Dropdown-Option "Herr" sichtbar ist, und klicke darauf
        option_herr = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[contains(@class, 'ant-select-dropdown-menu-item') and text()=' Für mich selbst ']"))
        )
        option_herr.click()

    def give_first_name(self):
        ffield = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, "firstName")))
        # firstname einfügen

        # Text in das Eingabefeld eingeben
        ffield.send_keys(self.first_name)

    def give_last_name(self):

        ffield = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, "lastName")))

        # Text in das Eingabefeld eingeben lastname

        ffield.send_keys(self.last_name)

    def give_email(self):

        ffield = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.ID, "email")))

        # Text in das Eingabefeld eingeben email

        ffield.send_keys(self.email)

    def give_num_persons(self):

        ffield = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            (By.ID, "formly_2_input_gewobag_gesamtzahl_der_einziehenden_personen_erwachsene_und_kinder_0")))

        # Text in das Eingabefeld eingeben
        ffield.send_keys(self.num_persons)

    def click_checkbox(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ant-checkbox"))
        )
        checkbox = self.driver.find_element(By.CLASS_NAME, "ant-checkbox")

        while 'ant-checkbox-checked' not in checkbox.get_attribute('class'):
            checkbox.click()
            time.sleep(0.5)

    def wait(self):
        input("wait ")

    def completeFunction(self):
        self.openDriver()
        self.cookie_button()
        self.anfrage_button()
        self.iframe_wechsel()
        self.choose_sex()
        self.give_first_name()
        self.give_last_name()
        self.give_email()
        self.give_num_persons()
        self.click_checkbox()
        self.selectAngehoerige()
        self.wait()




