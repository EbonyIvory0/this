from pages.main_page import MainPage
import random
import string
import pytest


def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


@pytest.mark.smoke_main_page
def test_03_create_channel_send_message__and_delete_channel(browser):  # Передаем фикстуру browser
    main = MainPage(browser)  # Создаем экземпляр MainPage, передавая browser
    name_channel = generate_random_string(5) # Генерация рандомного названия канала
    info_channel = generate_random_string(5) # Генерация рандомного описания канала
    rand_message = generate_random_string(5)

    main.decline_notifications()
    main.create_channel_button() # Нажатие кнопки 'Создать канал'
    main.enter_name_channel(name_channel) # Ввод названия канала
    main.channel_info(info_channel) # Ввод описания канала
    main.channel_creation_confirmation_button() # Нажатие кнопки 'продолжить' после заполнения всех обязательных полей после создания канала
    
    main.Waiting_for_modal_window_to_close() # Ожидание закрытия модального окна
    main.write_a_message(rand_message) # Ввод сообщения в созданный канал
    main.send_message() # Отправка сообщения в созданный канал
    main.check_message(rand_message) # Проверка отправки сообщения
    
    main.header_button_channel() # Вызов модального окна через название канала в хедере приложения
    main.settings_tab_in_modal_window() # вкладка настройки в модальном окне
    main.archive_channel() # Архивирование канала
    main.archive_channel_check() # Проверка уведомления об архивировании канала



@pytest.mark.create_delete_channel
def test_04_create_channel__and_delete_channel(browser):
    main = MainPage(browser)
    name_channel = generate_random_string(5) # Генерация рандомного названия канала
    info_channel = generate_random_string(5) # Генерация рандомного описания канала
    main.create_channel_button() # Нажатие кнопки 'Создать канал'
    main.enter_name_channel(name_channel) # Ввод названия канала
    main.channel_info(info_channel) # Ввод описания канала
    main.channel_creation_confirmation_button() # Нажатие кнопки 'продолжить' после заполнения всех обязательных полей после создания канала
    main.Waiting_for_modal_window_to_close() # Ожидание закрытия модального окна
    main.header_button_channel() # Вызов модального окна через название канала в хедере приложения
    main.settings_tab_in_modal_window() # вкладка настройки в модальном окне
    main.delete_channel() # Удаление канала
    main.delete_channel_check() # Проверка уведомления об удалении канала



@pytest.mark.enter_channel_write_message
def test_05_enter_in_random_channel_and_write_a_message(browser):
    main = MainPage(browser)
    rand_message = generate_random_string(5)
    main.enter_in_random_channel() # Вход в рандомный канал
    main.write_a_message(rand_message) # Ввод сообщения в поле ввода
    main.send_message() # Отправка сообщения кликом по кнопке 'Отправить'
    main.check_all_messages(rand_message) # Проверка сообщения 

@pytest.mark.send_and_delete_message
def test_06_enter_random_channel_write_message_delete_message(browser):
    main = MainPage(browser)
    rand_message = generate_random_string(5)
    main.enter_in_random_channel() # Вход в рандомный канал
    main.write_a_message(rand_message) # Ввод сообщения в поле ввода
    main.send_message() # Отправка сообщения кликом по кнопке 'Отправить'
    main.delete_message() # Удаление сообщения 
    main.message_deletion_check(rand_message) # Проверка удаления сообщения 


