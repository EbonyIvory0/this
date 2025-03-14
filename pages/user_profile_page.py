from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.user_profile_locators import LocatorsUserProfile
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random




# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserProfile(BasePage):
    def __init__(self, browser):
        """Инициализация класса.
        Объект браузера (WebDriver).
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.loc = LocatorsUserProfile
        super(UserProfile, self).__init__(browser)


    def open_user_profile_modal_window(self):
        """ Нажатие по аватару пользователя в футере приложения """
        logger.info("Нажатие по аватару пользователя в футере приложения")
        try:
            self.visibility_of_elements(
            self.loc.PROFILE_MODAL
            )[0].click()
            logger.info("Успешное нажатие по аватару пользователя")
        except Exception as e:
            print(f"Не удалось нажать по аватару пользователя в футере приложения {e}")
            raise

    def open_user_settings_in_modal_window(self):
        """ Нажатие кнопкни 
        'Настройки пользователя' в открывшемся модальном окне' """
        logger.info("Нажатие кнопкни 'Настройки пользователя'")
        try:
            self.visibility_of_elements(
            self.loc.USER_PROFILE_SETTINGS
            )[0].click()
            logger.info("Успешное нажатие по кнопке 'Настройки пользователя' ")
        except Exception as e:
            print(f"Не удалось нажать на кнопку 'Настройки пользователя' {e}")
            raise


    def edit_information_button(self):
        """ Нажатие кнопки редактирование информации """
        try:
            logger.info("Нажатие кнопки редактирования информации")
            self.visibility_of_elements(
            self.loc.REDACT_USER_INFO
            )[2].click()
            logger.info("Успешное нажатие кнопки редактирования информации")
        except Exception as e:
            logger.info(f"Не удалось нажать кнопку редактирования информации {e}")
            raise

    def user_last_name_field(self, last_name):
        """ Редактирование поля 'Фамилия' """
        try:
            logger.info("Редактирование поля фамилия")

            self.wait_element(
            self.loc.LAST_NAME_FIELD
            ).send_keys(Keys.CONTROL + "a", Keys.DELETE)

            self.wait_element(
            self.loc.LAST_NAME_FIELD
            ).send_keys(last_name)
            
            logger.info("Поле 'Фамилия' успешно заполнена")
        except Exception as e:
            logger.info(f"Не удалось заполнить поле 'Фамилия' {e}")
            raise
            

    def user_first_name_field(self, first_name):
        """ Редактирование поля 'Имя' """
        try:
            logger.info("Редактирование поля 'Имя' ")

            self.wait_element(
            self.loc.FIRST_NAME_FIELD
            ).send_keys(Keys.CONTROL + "a", Keys.DELETE)

            self.wait_element(
            self.loc.FIRST_NAME_FIELD
            ).send_keys(first_name)

            logger.info("Поле 'Имя' успешно заполнена")
        except Exception as e:
            logger.info(f"Не удалось заполнить поле 'Имя' {e}")
            raise

    def user_surname_field(self, surname):
        """ Редактирование поля 'Отчество' """
        try:
            logger.info("Редактирование поля 'Отчество'")
            
            self.wait_element(
            self.loc.SURNAME_FIELD
            ).send_keys(Keys.CONTROL + "a", Keys.DELETE)

            self.wait_element(
            self.loc.SURNAME_FIELD
            ).send_keys(surname)

            logger.info("Поле 'Отчество' успешно заполнена")
        except Exception as e:
            logger.info(f"Не удалось заполнить поле 'Отчество' {e}")
            raise

    def gender_male_radio_button(self):
        """ Клик по радио-кнопке 'Мужской'  """
        try:
            logger.info(" Клик по радио-кнопке выбора мужского пола ")
            self.wait_elements(
            self.loc.GENDER_MALE_RADIO_BUTTON
            )[0].click()
            logger.info(" Радио-кнопка выбора мужского пола нажата ")
        except Exception as e:
            logger.info(" Радио-кнопка выбора мужского пола не нажата ")
            raise


    def user_info_field(self, info):
        """ Редактирование поля 'О себе' """
        try:
            logger.info(" Попытка редактирования поля О себе ")
            self.wait_elements(
            self.loc.USER_INFO_FIELD
            )[4].click()
            
            self.wait_elements(
            self.loc.USER_INFO_FIELD
            )[0].send_keys(Keys.CONTROL + "a", Keys.DELETE)

            self.wait_elements(
            self.loc.USER_INFO_FIELD
            )[0].send_keys(info)
            logger.info(" Поле О себе успешно заполнено ")
        except Exception as e:
            logger.info(f"Не удалось отредактировать поле О себе {e}")
            raise

    
    def user_date_of_birth(self):
        """ Выбор рандомной даты рождения через плагин календаря """
        try:
            logger.info("Вызов плагина календаря")
            self.wait_element(
            self.loc.DATE_OF_BIRTH_REACT_PLUGIN
            ).click()
            logger.info("Выбор 'Февраль' ")
            february = self.visibility_of_elements(
            self.loc.FEBRUARY_MONTH
            )[1]
            february.click()
            logger.info("Месяц Февраль выбран")

            logger.info("Ожидание появления элемента")
            self.visibility_of_element(
            self.loc.DATE_OF_BIRTH_PLUGIN
            )

            week = self.visibility_of_elements(
            self.loc.WEEK_DATE_OF_BIRTH_PLUGIN
            )
            random.choice(week).click()
            logger.info("Рандомная дата рождения успешно выбрана через плагин календаря")
        except Exception as e:
            logger.info(f"Не удалось выбрать дату рождения через плагин календаря {e}")
            raise


    def save_button(self):
        """ Нажатие кнопки сохранить после заполнения всех полей """
        try:
            logger.info(" Нажатие кнопки Сохранить ")
            self.wait_elements(
            self.loc.SAVE_BUTTON
            )[1].click()
            logger.info("Кнопка Сохранить успешно нажата")
        except Exception as e:
            logger.info(f" Не удалось нажать кнопку Сохранить  {e}")
            raise

    def check_last_name(self, last_name):
        """ Проверка успешного сохранении информации в поле 'Фамилия' """
        try:
            logger.info("Проверка валидации поля Фамилия")
            check = self.wait_elements(
            self.loc.LAST_NAME_ASSERT
            )[0]
            assert check.text == last_name, ">>> Ошибка с фамилией <<<"
            logger.info("Проверка поля 'Фамилия' успешна")
        except Exception as e:
            logger.info(f"Не удалось проверить валидацию поля 'Фамилия' {e} ")
            raise


    def check_first_name(self, first_name):
        """ Проверка успешного сохранении информации в поле 'Имя' """
        try:
            logger.info("Проверка поля Имя")
            check = self.wait_elements(
            self.loc.FIRST_NAME_ASSERT
            )[0]
            assert check.text == first_name, ">>> Ошибка с именем <<<"
            logger.info("Проверка валидации поля 'Имя' успешна")
        except Exception as e:
            logger.info(f"Не удалось проверить валидацию поля 'Имя' {e}")
            raise

    def check_surname(self, surname):
        """ Проверка успешного сохранении информации в поле 'Отчество' """
        try:
            logger.info("Проверка поля Отчество")
            check = self.wait_elements(
            self.loc.SURNAME_ASSERT
            )[0]
            assert check.text == surname, ">>> Ошибка с отчеством <<<"
            logger.info("Проверка валидации поля 'Отчество' успешна")
        except Exception as e:
            logger.info(f"Не удалось проверить валидацию поля 'Отчество' {e}")
            raise

    def check_radio_button_gender_male(self):
        """ Проверка успешного сохранении информации 
        радио-кнопки выбор пола 'Мужской' """
        try:
            logger.info("Проверка радио-кнопки мужского пола")
            check = self.wait_elements(
            self.loc.GENDER_MALE_RADIO_BUTTON_ASSERT
            )[0]
            assert check.text == "Мужской", ">>> Ошибка с выбором пола <<<"
            logger.info("Проверка валидации радио-кнопки мужского пола успешна")
        except Exception as e:
            logger.info(f"Проверка валидации радио-кнопки мужского пола НЕ успешна {e}")
            raise


    def check_info(self, info):
        """ Проверка успешного сохранении информации в поле 'О себе' """
        try:
            logger.info("Проверка поля О себе")
            check = self.wait_elements(
            self.loc.USER_INFO_ASSERT
            )[0]
            assert check.text == info, ">>> Ошибка с полем 'О себе' <<<" 
            logger.info("Проверка валидации поля 'О себе ' успешна ")
        except Exception as e:
            logger.info("Проверка валидации поля 'О себе НЕ ' успешна ")
            raise


    def redact_company_info(self):
        """ Редактирование полей 'Компания' """
        try:
            logger.info("Нажатие кнопки редактирование полей 'Компания' ")
            self.visibility_of_elements(
            (By. CLASS_NAME, "cursor-pointer")
            )[3].click()
            logger.info("Кнопка редактирования нажата")
        except Exception as e:
            logger.info(f"Не удалось нажать кнопку редактирования полей 'Компания'")

    
    def redact_position_info(self):
        """ Редактирования поля 'Должность' """
        try:
            logger.info("Клик по полю 'Должность'"
            "и выбор должности из выпадающего списка")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__input-container")
            )[0].click()

            logger.info("Выбор первого элемента из выпадающего списка")
            self.element_to_be_clickable(
            (By.CLASS_NAME, "select__menu-list ")
            ).click()
            logger.info("Выбран первый элемент выпадающего списка")
        except Exception as e:
            logger.info(f"Не удалось выбрать элемент из выпадающего списка 'Должность'")

    
    def redact_departament_info(self):
        """ Редактирование поля 'Департмаент' """
        try:
            logger.info("Открытие выпадающего списка 'Департамент' ")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__input-container")
            )[1].click()    

            logger.info("Выбор второго элемента из выпадающего списка")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__option")
            )[1].click()
        except Exception as e:
            logger.info(f"Не удалось выбрать элемент из выпадающего списка 'Департамент'")

    def redact_head_of_department(self):
        """ Редактирование поля 'Руководитель' """
        try:
            logger.info("Открытие выпадающего списка 'Руководитель'")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__input-container")
            )[2].click()

            logger.info("Выбор второго элемента из выпадающего списка 'Руководитель'")
            self.visibility_of_elements(
            (By. CLASS_NAME, "select__option")
            )[1].click()
        except Exception as e:
            logger.info(f"Не удалось выбрать элемент из выпадающего списка 'Руководитель'")

            
    def check_position(self):
        """ Проверка поля 'Должность' после редактирования """
        try:
            check = self.wait_elements(
            (By.CLASS_NAME, "select__single-value")
            )[0]
            first_option = check.text
            assert first_option == check.text, "Ошибка проверки поля 'Должность' "
        except Exception as e:
            logger.info(f"Не успешная проверка поля должность после редактирования")
    
    def check_department(self):
        """ Проверка поля 'Департамент' после редактирования """
        try:
            check = self.wait_elements(
            (By.CLASS_NAME, "select__single-value")
            )[1]
            second_option = check.text
            assert second_option == check.text, "Ошибка проверки поля 'Департамент'"
        except Exception as e:
            logger.info(f"Не успешная проверка поля  Департамент после редактирования")

    def check_head_departament(self):
        


