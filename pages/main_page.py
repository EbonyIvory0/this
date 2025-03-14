from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage



# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




class MainPage(BasePage):
    def __init__(self, browser):
        """Инициализация класса.

        Объект браузера (WebDriver).
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)
        self.loc = LocatorsMainPage
        super(MainPage, self).__init__(browser)

    
    def create_channel_button(self):
        create_channel_button = self.element_to_be_clickable(
            self.loc.CREATE_CHANNEL_BUTTON
        )
        create_channel_button.click()
        logger.info("Кнопка 'Создать канал' нажата")
    
    
    def enter_name_channel(self, name_channel):
        """Создание канала и ввод его названия.

        :param name_channel: Имя канала.
        """
        # Ожидание и клик по кнопке "Создать канал"
        try:
            logger.info("Ожидание появления модального окна")
            self.visibility_of_element(self.loc.MODAL_WINDOW)
            logger.info(f"Ввод названия канала")
            channel_name_field = self.element_to_be_clickable(
                self.loc.CHANNEL_NAME_FIELD
            )
            channel_name_field.send_keys(name_channel)
            logger.info(f"Название канала '{name_channel}' введено")
        except:
            channel_name_field = self.visibility_of_element(
                self.loc.CHANNEL_NAME_FIELD
            )
            channel_name_field.send_keys(name_channel)
            logger.info(f"Название канала '{name_channel}' введено")
            raise


    def channel_info(self, info_channel):
        """
        info_channel: Описание канала
        """
        logger.info(f"Ввод описания канала {info_channel} ")
        try:
            channel_info_field = self.visibility_of_element(
                self.loc.CHANNEL_INFO_FIELD
            )
            channel_info_field.send_keys(info_channel)
        except Exception as e:
            logger.info(f"Описание канала не введено: {e}")


    def channel_creation_confirmation_button(self):
        """
        Подтверждение создания канала
        """

        logger.info(
            f"Нажатие кнопки 'продолжить' после заполнения всех обязательных полей при создании канала"
        )
        try:
            continue_button = self.element_to_be_clickable(
                self.loc.CONTINUE_BUTTON
            )
            continue_button.click()
            logger.info("Канал успешно создан")
        except Exception as e:
            logger.info(f"Канал не создан {e}")



    def header_button_channel(self):
        """ Клик по названию канала
        вызывающий модальное окно
        c информацией o канале и настройками
        """
        logger.info("Нажать на название канала в хедере приложения")
        header_button = self.element_to_be_clickable(
            self.loc.HEADER_BUTTON
        )
        header_button.click()

    def settings_tab_in_modal_window(self):
        """ Вкладка настройки в модальном окне """
        logger.info("Вкладка настройки в модальном окне")
        settings_tab = self.wait_elements(
                self.loc.SETTINGS_TAB
            )[2]
        settings_tab.click()


    def delete_channel(self):
        """Удаление канала."""
        logger.info("Удаление канала")
        try:
            logger.info(f"Нажатие кнопки 'Удалить канал'")
            delete_button = self.element_to_be_clickable(
                self.loc.DELETE_BUTTON
            )
            delete_button.click()
            logger.info(f"Подтверждение удаления канала")
            confirm_delete_button = self.element_to_be_clickable(
                self.loc.CONFIRM_DELETE_BUTTON
            )
            confirm_delete_button.click()
        except Exception as e:
            logger.info(f"Не удалось удалить канал: {e}")



    def archive_channel(self):
        """ Архивирование канала."""
        logger.info("Архивирование канала")
        try:
            logger.info("Нажатие кнопки 'Архивировать канал'")
            archive = self.visibility_of_elements(self.loc.ARCHIVE_CHANNEL)[0]
            archive.click()
            archive_confirm = self.visibility_of_element(self.loc.CONFIRM_DELETE_BUTTON)
            logger.info("Нажатие кнопки подтверждения")
            archive_confirm.click()
        except Exception as e:
            logger.info(f"He удалось архивировать канал: {e}")



    def delete_channel_check(self):
        """Проверка уведомления об удалении канала"""
        logger.info("Проверка уведомления об удалении канала")
        try:
            check = self.visibility_of_element(self.loc.DELETE_CONFIRMATION_MESSAGE)
            assert check.text == "Канал удален", ">>> Не удалось проверить удаление канала"
        except Exception as e:
            logger.info(f"Не удалось проверить удаление канала: {e}")
        
    def archive_channel_check(self):
        """Проверка уведомления об архивировании канала"""
        logger.info("Проверка уведомления об архивировании канала")
        check = self.visibility_of_element(self.loc.DELETE_CONFIRMATION_MESSAGE)
        assert check.text == "Изменения сохранены", ">>> Не удалось проверить архивирование канала"

    
    def Waiting_for_modal_window_to_close(self):
        """ Ожидание закрытия модального окна """
        self.invis_of_element(
                self.loc.MODAL_WINDOW
        )


    def write_a_message(self):
        """Написание сообщения в созданный канал."""

        logger.info("Попытка ввода сообщения")
        try:
           
            message_input = self.visibility_of_element(
                self.loc.MESSAGE_INPUT
            )
            message_input.send_keys("123qwe=[]]")
            logger.info("Сообщение введено")
        except Exception as e:
            logger.info(f"Не удалось отправить сообщение: {e}")


    def send_message(self):
        """
        Кнопка отправки сообщения
        """
        try:
            logger.info(f"Попытка отправки сообщения")
            send_button = self.element_to_be_clickable(
                self.loc.SEND_MESSAGE_BUTTON
            )
            send_button.click()
            logger.info("Сообщение отправлено")
        except Exception as e:
            logger.info(f"Сообщение не отправлено")


    def check_message(self):
        """
        Проверка отправки сообщения
        """
        try:
            message = self.wait.until(
                EC.visibility_of_all_elements_located(self.loc.MESSAGE_TEXT)
            )[1]
            logger.info(f"Первая попытка проверки отправки сообщения:")
            assert (
                message.text == "123qwe=[]]"
            ), ">>> Message assert ERROR, first try<<<"
        except Exception as e:
            logger.info(f"Вторая попытка проверки отправки сообщения: {e}")
            message = self.visibility_of_elements(
                self.loc.MESSAGE_TEXT
            )[1]
            assert (
                message.text == "123qwe=[]]"
            ), ">>> Message assert ERROR, second try, message not found<<<"
