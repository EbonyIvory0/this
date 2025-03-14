from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import json
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

last_name = generate_random_string(10)
first_name = generate_random_string(10)
surname = generate_random_string(10)
info = generate_random_string(10)

action = ActionChains

browser = webdriver.Chrome()
browser.get("https://app.staging.sphera.work/")
browser.maximize_window()
with open("cookies.json", "r") as file:
    cookies = json.load(file)
for cookie in cookies:
    browser.add_cookie(cookie)
    browser.refresh()

wait = WebDriverWait(browser, 10)



profile_modal = wait.until(
    EC.visibility_of_all_elements_located((By. CLASS_NAME, "MuiAvatar-root"))
)[0].click()

settings = wait.until(
    EC.visibility_of_all_elements_located((By. CLASS_NAME, "item-title"))
)[0].click()

redact_user_info_button = wait.until(
    EC.visibility_of_all_elements_located((By. CLASS_NAME, "cursor-pointer"))
)[3].click()






doljnost = wait.until(
    EC.visibility_of_all_elements_located((By. CLASS_NAME, "select__input-container"))
)[0].click()
choose_doljnost = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "select__menu-list "))
).click()
check_dolj = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "select__single-value"))
)[0]




# depart = wait.until(
#     EC.visibility_of_all_elements_located((By. CLASS_NAME, "select__input-container"))
# )[1].click()    
# choose_depart = wait.until(
#     EC.visibility_of_all_elements_located((By. CLASS_NAME, "select__option"))
# )[1].click()


# check_depart = wait.until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "select__single-value"))
# )[1]

# print(check_depart.text)

# # second_option_text = check_depart.text

# second_option_text = check_depart.text
# print(second_option_text)


# rucovod = wait.until(
#     EC.visibility_of_all_elements_located((By. CLASS_NAME, "select__input-container"))
# )[2].click()

# choose_rucovod = wait.until(
#     EC.visibility_of_all_elements_located((By. CLASS_NAME, "select__option"))
# )[1].click()





save = wait.until(
    EC.visibility_of_all_elements_located((By. CLASS_NAME, "button-title"))
)[1].click()

# check_rucovod = browser.find_elements(By. CLASS_NAME, "select__single-value")[2]

# third_option = check_rucovod.text
# assert third_option == check_rucovod.text, "unluck????<<<<<"

# second_option_text = check_depart.text
# assert second_option_text == check_depart.text, "again unluck<<<<<<<<<<<<"

# first_option_text = check_dolj.text
# assert first_option_text == check_dolj.text, "again unluck<<<<<<<<<<<<"



time.sleep(1)