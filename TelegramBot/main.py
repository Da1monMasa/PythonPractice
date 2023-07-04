import telebot
from telebot import types
import requests
import matplotlib.pyplot as plt
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6129050247:AAFiJ3Ozcx1qU4FI1ALGRMQpGhDXGsB-x2Y'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('О КОМПАНИИ')
    item2 = types.KeyboardButton('РЕШЕНИЯ')
    item3 = types.KeyboardButton('ПРЕЗЕНТАЦИЯ')
    item4 = types.KeyboardButton('ДИАГРАММА')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'О КОМПАНИИ')
def about_company(message):
    presentation_url = 'https://yandex.ru/maps/org/239183477213'
    company_info = '''
    ООО "СОФТЕЛ"
    Компания Софтел – это высококвалифицированные 
    кадры и уникальные разработки 
    в области ресурсоснабжения и ЖКХ
    ИНН: 9705121515, 
    ОГРН: 1187746688656
    Наш адрес: 105066, город Москва, ул. Нижняя Красносельская, 
    д. 35, стр. 64, офис 323, этаж 3

    Телефоны:
    Отдел продаж: +7 (921) 957-02-93
    Офис: 8(495) 280-10-39
    Email: info@sofiot.ru
    WhatsApp: +7 (921) 957-02-93
    Время работы: пн-пт. с 9 до 19 часов.
    '''


    # Создаем кнопку для открытия презентации
    open_button = types.InlineKeyboardButton(text='Мы на карте', url=presentation_url)
    # Создаем разметку с кнопками
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(open_button)
    bot.send_message(message.chat.id, company_info, reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == 'РЕШЕНИЯ')
def solutions(message):
    solutions_info = '''
    “Софиот” – программно-аппаратные решения для ЖКХ, производственных и строительных Компаний

    Мониторинг оборудования: “Софиот Производство”
    “Софиот Производство” – это интегрированная система мониторинга оборудования на производственных предприятиях, которая позволяет отслеживать работу оборудования в режиме реального времени, анализировать его производительность и эффективность, а также интегрироваться с другими системами управления производством. https://sofiot.ru/programmno-apparatnye-resheniya/monitoring-i-analiz-raboty-oborudovniya/

    Управление освещением: “Контроллеры Софиот” (Технология: LoRaWAN и 6LoWPAN)
    “Контроллеры Софиот” – это технология управления освещением, использующая протоколы передачи данных LoRaWAN и 6LoWPAN. Она позволяет удаленно управлять системами освещения, контролировать энергопотребление и настраивать режим работы освещения в зависимости от конкретных потребностей. https://sofiot.ru/programmno-apparatnye-resheniya/upravlenie-naruzhnym-i-vnutrennim-osveshcheniem/

    Контроль параметров: “Софиот Аналитика”
    “Софиот Аналитика” – это интегрированная система контроля параметров, которая позволяет анализировать данные из различных источников на производстве, оптимизировать процессы производства и повышать эффективность работы предприятия в целом. https://sofiot.ru/programmno-apparatnye-resheniya/avtomaticheskiy-kontrol-parametrov/

    Поиск потерь: “Софиот Баланс” (Технология: LPWAN (LoRaWAN и NB-IoT))
    “Софиот Баланс” – это технология поиска потерь на производстве, использующая протоколы передачи данных LPWAN, такие как LoRaWAN и NB-IoT. Она позволяет мониторить энергопотребление на производстве, анализировать данные и выявлять места потерь, чтобы оптимизировать работу оборудования и снизить затраты на производство. https://sofiot.ru/programmno-apparatnye-resheniya/poisk-poter-i-utechek-vody/

    Контроль ресурсов: “Софиот Учет Ресурсов” (Технология: LPWAN NB-IoT и LoRaWAN)
    “Софиот Учет Ресурсов” – это технология контроля ресурсов на производстве, использующая протоколы передачи данных LPWAN, такие как LoRaWAN и NB-IoT. Она позволяет мониторить потребление ресурсов, таких как энергия, вода, газ и другие, анализировать данные и оптимизировать их использование, что способствует снижению затрат на производство. https://sofiot.ru/programmno-apparatnye-resheniya/umnyy-uchet-kontrol-resursov/
    '''

    bot.send_message(message.chat.id, 'Вы выбрали команду "РЕШЕНИЯ"')
    bot.send_message(message.chat.id, solutions_info)

@bot.message_handler(func=lambda message: message.text == 'ПРЕЗЕНТАЦИЯ')
def presentation(message):
    presentation_url = 'https://sofiot.ru/SOFTEL-(SOFIOT)-presentation.pdf'
    preview_url = 'https://example.com/preview'

    # Создаем кнопку для открытия презентации
    open_button = types.InlineKeyboardButton(text='Открыть презентацию', url=presentation_url)

    # Создаем кнопку для скачивания презентации
    download_button = types.InlineKeyboardButton(text='Скачать презентацию', callback_data='download')

    # Создаем разметку с кнопками
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(open_button)
    keyboard.row(download_button)

    # Отправляем сообщение с кнопками пользователю
    bot.send_message(message.chat.id, 'Вы выбрали команду "ПРЕЗЕНТАЦИЯ".', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'download')
def download_presentation(call):
    presentation_url = 'https://sofiot.ru/SOFTEL-(SOFIOT)-presentation.pdf'
    presentation_file = requests.get(presentation_url)

    # Сохраняем презентацию на сервере
    with open('presentation.pdf', 'wb') as file:
        file.write(presentation_file.content)

    # Отправляем пользователю скачанный файл презентации
    with open('presentation.pdf', 'rb') as file:
        bot.send_document(call.message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == 'ДИАГРАММА')
def diagramm_call(message):
    # Данные для диаграммы (проценты загрязнения воздуха на предприятии)
    labels = ['Показатель 1', 'Показатель 2', 'Показатель 3']
    values = [40, 30, 30]

    # Построение диаграммы
    plt.pie(values, labels=labels, autopct='%1.1f%%')

    # Сохранение диаграммы в файл
    diagramm_path = 'diagramm.png'
    plt.savefig(diagramm_path)

    # Отправка диаграммы в переписку с ботом
    with open(diagramm_path, 'rb') as diagramm_file:
        bot.send_photo(message.chat.id, diagramm_file)

    # Очистка диаграммы из памяти
    plt.clf()

bot.polling()
