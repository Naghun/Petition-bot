import selenium, random, csv, clipboard
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service

with open('proxy/valid_proxy.csv', 'r', newline='') as file:

    reader = csv.reader(file)
    proxies = []

    for row in reader:
        proxies.append(row[0].strip('[]'))

with open('data/cities.csv', 'r', newline='', encoding='utf-8') as cities_file:
    cities_reader = csv.reader(cities_file)
    cities_list = [row[0] for row in cities_reader if row]


with open('data/people-1000.csv', 'r', newline='', encoding='utf-8') as people_file:
    people_reader = csv.reader(people_file)
    
    names = []
    last_names = []
    part_emails = []
    
    for row in people_reader:
        names.append(row[2])
        last_names.append(row[3])
        part_emails.append(row[5].split('@')[0])



def set_name(name, max_tries, driver):
    retries=0
    while int(retries) < int(max_tries):
        try:
            driver.send_keys('#first_name', name)
            break
        except:
            print("Error trying to set Name")
            driver.sleep(2)
            retries +=1
    else:
        raise Exception("Max tries reached, Unable to set Name")
        
def set_last_name(last_name, max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.send_keys('#last_name', last_name)
            break
        except Exception as e:
            print(f"Error trying to set Last Name: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set Last Name.")

def set_city(city, max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.send_keys('#location', city)
            break
        except Exception as e:
            print(f"Error trying to set City: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set City.")

def set_country(country, max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.send_keys('#country', country)
            break
        except Exception as e:
            print(f"Error trying to set country: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set country.")

def set_email(email, max_tries, driver):
    retries = 0
    my_email=email
    clipboard.copy(my_email)
    while int(retries) < int(max_tries):
        try:
            driver.send_keys('#email', f'{Keys.CONTROL + 'v'}')
            break
        except Exception as e:
            print(f"Error trying to set email: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to set email.")

def confirm_email(email, max_tries, driver):
    retries = 0
    letter = f"Keys.SHIFT + '2'"
    while int(retries) < int(max_tries):
        try:
            driver.send_keys('#sahkopostiosoite_uudestaan', email)
            break
        except Exception as e:
            print(f"Error trying to confirm email: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to confirm email.")

def set_no_public_check(max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.click('#parent_element_form_is_public > label:nth-child(4) > input[type=radio]')
            break
        except Exception as e:
            print(f"Error trying to press don't show publicly checkbox: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to press don't show publicly checkbox.")

def dont_send_mail_check(max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.click('#parent_element_form_allow_announcement_notifications > label:nth-child(4) > input[type=radio]')
            break
        except Exception as e:
            print(f"Error trying to press don't send mails checkbox: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to press don't send mails checkbox.")

def validate_years_check(max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.click('#parent_element_form_i_accept_tos_and_privacy_policy > label:nth-child(3) > input[type=radio]')
            break
        except Exception as e:
            print(f"Error trying to validate years checkbox: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to validate years checkbox.")

def submit_button(max_tries, driver):
    retries = 0
    while int(retries) < int(max_tries):
        try:
            driver.click('#parent_element_form_submit > button')
            break
        except Exception as e:
            print(f"Error trying to send petition: {e}")
            driver.sleep(2)
            retries += 1
    else:
        raise Exception("Max tries reached, Unable to send petition.")



def main():

    #################
    max_tries=2
    petition_votes=2
    circle=0
    max_attempts=3

    while circle < petition_votes:
        print(f"Circle is: {circle}")
        print(f"Petition number: {petition_votes}")
        last_email_parts=['@gmail.com', '@hotmail.com', '@outlook.com']
        digits = random.randint(1-1000, 1)
        name = random.choice(names)
        last_name=random.choice(last_names)
        city = random.choice(cities_list)
        country = 'Slovakia'
        first_email_part=f'{name}{last_name}{digits}'
        email = f'{random.choice(part_emails)}{digits}{random.choice(last_email_parts)}'

        while max_attempts > 0:
            #proxy = random.choice(proxies)
            #options.add_argument(f'--proxy-server={proxy}')
            try:
                driver = Driver(uc=True)
                driver.open('https://www.peticie.com/adam_roharik_do_finale_farmy_15')
                break
            except Exception as e:
                print(f"Error loading the page: {e}")
                max_attempts -= 1
                print(f"Remaining attempts: {max_attempts}")

                if max_attempts == 0:
                    print("Max attempts reached. Exiting.")
                    break

        #######################
        try:
            driver.click('#give_consent_for_for_personalized_advertising')
        except:
            pass
        #################
        
        set_name(name, max_tries, driver)
        set_last_name(last_name, max_tries, driver)
        set_city(city, max_tries, driver)
        set_country(country, max_tries, driver)
        set_email(email, max_tries, driver)
        driver.sleep(2)
        confirm_email(email, max_tries, driver)

        set_no_public_check(max_tries, driver)
        dont_send_mail_check(max_tries, driver)
        validate_years_check(max_tries, driver)
        driver.sleep(2)
        submit_button(max_tries, driver)
        driver.sleep(2)

        driver.quit()
        circle+=1
        print("pettition successfull!")


if __name__ == "__main__":
    main()