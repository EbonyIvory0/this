from selenium.webdriver.common.by import By   


class LocatorsUserProfile:
    PROFILE_MODAL = (By. CLASS_NAME, "MuiAvatar-root")
    USER_PROFILE_SETTINGS = (By. CLASS_NAME, "item-title")

    REDACT_USER_INFO = (By. CLASS_NAME, "cursor-pointer")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    FIRST_NAME_FIELD = (By. NAME, "firstName")
    SURNAME_FIELD = (By. NAME, "patronymic")
    GENDER_MALE_RADIO_BUTTON = (By. CLASS_NAME, 'MuiRadio-root')
    USER_INFO_FIELD = (By. CLASS_NAME, "custom-input__container")

    INPUT_INFO = (By. TAG_NAME, "textarea")

    DATE_OF_BIRTH_REACT_PLUGIN = (By. ID, "dob")
    FEBRUARY_MONTH = (By. CSS_SELECTOR, "div.calendar-header > select > option")
    DATE_OF_BIRTH_PLUGIN = (By. CLASS_NAME, "react-datepicker")
    WEEK_DATE_OF_BIRTH_PLUGIN = (By. CLASS_NAME, "react-datepicker__week")

    SAVE_BUTTON = (By. CLASS_NAME, "button-title")

    #ASSERTS
    LAST_NAME_ASSERT = (By. XPATH, "//form/div[2]/div[1]/div[1]")
    FIRST_NAME_ASSERT = (By. XPATH, "//form/div[2]/div[2]/div")
    SURNAME_ASSERT = (By. XPATH, "//form/div[2]/div[3]/div")
    GENDER_MALE_RADIO_BUTTON_ASSERT = (By. XPATH, "//form/div[2]/div[4]/div")
    USER_INFO_ASSERT = (By. XPATH, "//form/div[2]/div[6]/div")


    last_name = (By. CLASS_NAME, "field-value")

