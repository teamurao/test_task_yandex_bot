import telebot
from telebot import types
import webbrowser

TOKEN = "6447108138:AAFb-I6FpT41cEZ7Bii5V9dRCbJVPpijxCA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    reply_markup = create_menu()
    func = f'''Привет, {message.from_user.first_name}! Смотри, что я умею:
    /help - если нужна помощь
    /selfie - мое последнее селфи
    /school_photo - фото из старшей школы
    /hobby - прочитаю пост о хобби
    /rep - репозиторий с кодом бота
    /github - мой гитхаб
    /voice_gpt - что такое GPT?
    /voice_sql - в чем разница между SQL и NoSQL?
    /voice_love_story - история первой любви'''

    bot.send_message(message.chat.id, func, parse_mode='html', reply_markup=reply_markup)


@bot.message_handler(commands=['selfie'])
def selfie(message):
    file = open('./selfie.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, 'Каталась на кораблике по Москве-реке')

@bot.message_handler(commands=['school_photo'])
def scool_photo(message):
    file = open('./school_photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, 'Заканчиваю 10 класс')

@bot.message_handler(commands=['voice_gpt'])
def gpt(message):
    file = open('./gpt.ogg', 'rb')
    bot.send_voice(message.chat.id, file)
    bot.send_message(message.chat.id, 'Объяснение, что такое GPT для бабушки')

@bot.message_handler(commands=['voice_sql'])
def sql(message):
    file = open('./sql.ogg', 'rb')
    bot.send_voice(message.chat.id, file)
    bot.send_message(message.chat.id, 'Объяснение, что чем отличается SQL от NoSQL')

@bot.message_handler(commands=['voice_love_story'])
def sql(message):
    file = open('./love_story.ogg', 'rb')
    di = open('./leonardo-dicaprio.mp4', 'rb')
    bot.send_voice(message.chat.id, file)
    bot.send_message(message.chat.id, 'Угадал рассказчика? 😏')
    bot.send_video(message.chat.id, di)

@bot.message_handler(commands=['hobby'])
def hobby(message):
    text = '''
    <b>Пост о моем главном увлечении</b>
    Хм... сложно сказать, что мне нравится больше всего 🤔 Мне нравится узнавать что-то новое и решать сложные задачи.
    Сейчас доучиваюсь на курсе по Data Science в Яндекс.Практикуме, самое увлекательное для меня - когда модель показывает лучший результат.
    Можно просидеть над задачей несколько дней, а когда наконец она решается, то получаешь массу эмоций "какой ты всё-таки молодец, что не сдался".
    
    А еще я не прочь за день посмотреть все серии дорамы или сериала 😁
    '''
    bot.send_message(message.chat.id, text, parse_mode='HTML')

def create_menu():
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Github')
    btn2 = types.KeyboardButton('Репозиторий с ботом')
    markup.add(btn1, btn2)
    return markup

@bot.message_handler(func=lambda message: message.text == 'Github')
def github(message):
    url = 'https://github.com/teamurao'
    webbrowser.open(url)

@bot.message_handler(func=lambda message: message.text == 'Репозиторий с ботом')
def rep(message):
    url = 'https://github.com/teamurao/test_task_yandex_bot'
    webbrowser.open(url)

bot.polling(non_stop=True)