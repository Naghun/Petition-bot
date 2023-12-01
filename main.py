import selenium, random, csv, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

with open('valid_proxy.csv', 'r', newline='') as file:

    reader = csv.reader(file)
    proxies = []

    for row in reader:
        proxies.append(row[0].strip('[]'))

with open('cities.csv', 'r', newline='', encoding='utf-8') as cities_file:
    cities_reader = csv.reader(cities_file)
    cities_list = [row[0] for row in cities_reader if row]


with open('people-1000.csv', 'r', newline='', encoding='utf-8') as people_file:
    people_reader = csv.reader(people_file)
    
    names = []
    last_names = []
    part_emails = []
    
    for row in people_reader:
        names.append(row[2])
        last_names.append(row[3])
        part_emails.append(row[5].split('@')[0])



def set_name(name, max_tries, wait):
    retries=0
    print("Entering Name: ")
    while int(retries) < int(max_tries):
        try:
            name_field=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first_name"]')))
            name_field.send_keys(name)
            break
        except:
            print("Error trying to set Name")
            time.sleep(2)
            retries +=1
    else:
        raise Exception("Max tries reached, Unable to set Name")
        
def set_last_name(last_name, max_tries, wait):
    retries = 0
    print("Entering Last Name: ")
    while int(retries) < int(max_tries):
        try:
            last_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last_name"]')))
            last_name_field.send_keys(last_name)
            break
        except Exception as e:
            print(f"Error trying to set Last Name: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set Last Name.")

def set_city(city, max_tries, wait):
    retries = 0
    print("Entering City: ")
    while int(retries) < int(max_tries):
        try:
            city_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="location"]')))
            city_field.send_keys(city)
            break
        except Exception as e:
            print(f"Error trying to set City: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set City.")

def set_country(country, max_tries, wait):
    retries = 0
    print("Entering Country: ")
    while int(retries) < int(max_tries):
        try:
            country_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="country"]')))
            country_field.send_keys(country)
            break
        except Exception as e:
            print(f"Error trying to set country: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set country.")

def set_email(email, max_tries, wait):
    retries = 0
    print("Entering Email: ")
    while int(retries) < int(max_tries):
        try:
            email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
            email_field.send_keys(email)
            break
        except Exception as e:
            print(f"Error trying to set email: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set email.")

def confirm_email(email, max_tries, wait):
    retries = 0
    print("Confirming Email: ")
    while int(retries) < int(max_tries):
        try:
            email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sahkopostiosoite_uudestaan"]')))
            email_field.send_keys(email)
            break
        except Exception as e:
            print(f"Error trying to confirm email: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to confirm email.")

def set_no_public_check(max_tries, wait):
    retries = 0
    print("Setting visibility checkbox: ")
    while int(retries) < int(max_tries):
        try:
            show_check = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="parent_element_form_is_public"]/label[3]/input')))
            show_check.click()
            break
        except Exception as e:
            print(f"Error trying to press don't show publicly checkbox: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to press don't show publicly checkbox.")

def dont_send_mail_check(max_tries, wait):
    retries = 0
    print("Setting dont sent email checkbox: ")
    while int(retries) < int(max_tries):
        try:
            no_send_check = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="parent_element_form_allow_announcement_notifications"]/label[3]/input')))
            no_send_check.click()
            break
        except Exception as e:
            print(f"Error trying to press don't send mails checkbox: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to press don't send mails checkbox.")

def validate_years_check(max_tries, wait):
    retries = 0
    print("Validating years checkbox")
    while int(retries) < int(max_tries):
        try:
            valid_years_check = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="parent_element_form_i_accept_tos_and_privacy_policy"]/label[2]/input')))
            valid_years_check.click()
            break
        except Exception as e:
            print(f"Error trying to validate years checkbox: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to validate years checkbox.")

def submit_button(max_tries, wait):
    retries = 0
    print("Submitting button")
    while int(retries) < int(max_tries):
        try:
            submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="parent_element_form_submit"]/button')))
            submit_button.click()
            break
        except Exception as e:
            print(f"Error trying to send petition: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to send petition.")

def accept_license(max_tries, wait):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            accept_check = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form2_conditions"]')))
            accept_check.click()
            break
        except Exception as e:
            print(f"Error trying to agree with license terms: {e}")
            time.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to agree with license terms.")






def main():


    #################
    proxy = random.choice(proxies)
    options = Options()
    #options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
    )
    wait = WebDriverWait(driver, 10)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    time.sleep(3)
    #################
    max_tries = 2
    #petition_votes_input=int(input("How many times you want to sign petition: "))
    petition_votes=4
    circle=0
    country='Slovakia'
    while circle != petition_votes:        #use petition_votes to set how many petitions outside of terminal
        driver.get('https://www.peticie.com/adam_roharik_do_finale_farmy_15')

        last_email_parts=['@gmail.com', '@hotmail.com', '@outlook.com']
        digits = random.randint(1-1000, 1)

        name = random.choice(names)
        last_name=random.choice(last_names)
        city = random.choice(cities_list)
        country = 'Slovakia'
        email = f'{random.choice(part_emails)}{digits}{random.choice(last_email_parts)}'
        print(f"name:{name}, surname: {last_name}, city:{city}, country:{country}, email: {email}")

        """
        max_attempts=3
        while max_attempts > 0:
            try:
                driver.get('https://www.peticie.com/adam_roharik_do_finale_farmy_15')
                time.sleep(10)
                break
            except Exception as e:
                print(f"Error loading the page: {e}")
                max_attempts -= 1
                print(f"Remaining attempts: {max_attempts}")
                if max_attempts == 0:
                    print("Max attempts reached. Exiting.")
                    break
                driver.quit()
                proxy = random.choice(proxies)
                options = Options()
                options.add_argument(f'--proxy-server={proxy}')
                driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options
                )
                wait = WebDriverWait(driver, 10)
                driver.set_page_load_timeout(30)
                driver.maximize_window()"""
        
        
        try:
            cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="give_consent_for_for_personalized_advertising"]')))
            if cookies:
                cookies.click()
                time.sleep(3)
        except:
            continue
        
        set_name(name, max_tries, wait)
        set_last_name(last_name, max_tries, wait)
        set_city(city, max_tries, wait)
        set_country(country, max_tries, wait)
        set_email(email, max_tries, wait)
        time.sleep(2)
        confirm_email(email, max_tries, wait)

        set_no_public_check(max_tries, wait)
        dont_send_mail_check(max_tries, wait)
        validate_years_check(max_tries, wait)
        time.sleep(2)
        submit_button(max_tries, wait)

        #accept_license(max_tries)
        circle+=1
        time.sleep(2)

        driver.quit()
    print("pettition successfull!")
if __name__ == "__main__":
    main()