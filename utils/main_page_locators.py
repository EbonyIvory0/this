from selenium.webdriver.common.by import By   


class LocatorsMainPage:
    CREATE_CHANNEL_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Создать канал"]')
    CHANNEL_NAME_FIELD = (By.ID, "name")
    CHANNEL_INFO_FIELD = (By.ID, "description")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Продолжить']")

    HEADER_BUTTON = (By.CLASS_NAME, "header__button")
    MODAL_WINDOW = (By.CLASS_NAME, "dialog__paper")
    SETTINGS_TAB = (By.CSS_SELECTOR, '[role="tab"]')
    DELETE_BUTTON = (By.CLASS_NAME, "settings__button-warning")
    CONFIRM_DELETE_BUTTON = (By.CLASS_NAME, "error-button")
    DELETE_CONFIRMATION_MESSAGE = (
        By.CSS_SELECTOR,
        ".Toastify__toast-body > div:nth-child(2)",
    )
    ARCHIVE_CHANNEL = (By. CLASS_NAME, "settings__button")
    ARCHIVE_CONFIRM_BUTTON = (By.CLASS_NAME, "error-button")


    MESSAGE_INPUT = (By.CLASS_NAME, "ql-editor")
    SEND_MESSAGE_BUTTON = (By.XPATH, '//button[text()="Отправить"]')
    MESSAGE_TEXT = (By.CLASS_NAME, "message-text")

