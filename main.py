import requests
import os
import telebot
from datetime import datetime
from telebot import types, TeleBot
from bs4 import BeautifulSoup
from telebot import types




bot: TeleBot =telebot.TeleBot("1465386978:AAER4hIr6kGbAGc7KGqLj2un2DRFG_vfUWQ")



def foo():
	URL = "https://www.google.com/search?ei=IrMCYOiFBIytrgTdqKT4DA&q" \
		  "=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B" \
		  "8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+r+&gs_lcp=Cg" \
		  "Zwc3ktYWIQAxgAMgkIABCxAxAKECoyBwgAELEDEEMyBAgAEAoyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEA" \
		  "oyBAgAEAoyBAgAEAoyBAgAEEM6BAgAEEc6AggAOgYIABAWEB46BAgAEA06BggAEAcQHjoICAAQCBAHEB46BQg" \
		  "AELEDOgoIABCxAxCDARBDOgYIABAKECpQmTJYqGFg-GtoAHACeACAAWmIAd4JkgEEMTAuM5gBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab"
	URL2 = "https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80+%D0%B2" \
		   "+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&oq=%D0%B4%D0%BE&aqs=chrome.1.69i59l3j69i" \
		   "57j0j69i61l3.2039j1j7&sourceid=chrome&ie=UTF-8"


	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}



	full_page = requests.get(URL2, headers=headers)
	# print(full_page.content)
	soup = BeautifulSoup(full_page.content, "html.parser")
	# <span class="DFlfde SwHCTb" data-precision="2" data-value="28.172480000000004">28,17</span>
	convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
	return(convert[0].text)


def foo2():
	URL = "https://www.google.com/search?ei=IrMCYOiFBIytrgTdqKT4DA&q" \
		  "=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%B" \
		  "8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+r+&gs_lcp=Cg" \
		  "Zwc3ktYWIQAxgAMgkIABCxAxAKECoyBwgAELEDEEMyBAgAEAoyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEA" \
		  "oyBAgAEAoyBAgAEAoyBAgAEEM6BAgAEEc6AggAOgYIABAWEB46BAgAEA06BggAEAcQHjoICAAQCBAHEB46BQg" \
		  "AELEDOgoIABCxAxCDARBDOgYIABAKECpQmTJYqGFg-GtoAHACeACAAWmIAd4JkgEEMTAuM5gBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

	full_page = requests.get(URL, headers=headers)
	# print(full_page.content)
	soup = BeautifulSoup(full_page.content, "html.parser")
	# <span class="DFlfde SwHCTb" data-precision="2" data-value="28.172480000000004">28,17</span>
	convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
	return(convert[0].text)





@bot.message_handler(commands=["rate_of_rub"])
def crs(message):
	bot.send_message(message.chat.id,foo())


@bot.message_handler(commands=["rate_of_hrn"])
def crs(message):
	bot.send_message(message.chat.id,foo2())


@bot.message_handler(commands=["date"])
def time(message):
  d1=datetime.now()
  bot.reply_to(message,d1.strftime("Today is %A  %B   %Y year "))


@bot.message_handler(commands=["start","help"])
def help(message):
    bot.reply_to(message,"Команды-/steam /inst /website /date /rate_of_rub /rate_of_hrn /calculator ")



@bot.message_handler(commands=['website'])
def open_website(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://www.google.com/"))
	bot.send_message(message.chat.id,
                     'Ок ',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['inst'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com"))
	bot.send_message(message.chat.id, 'Ок', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['steam'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в ", url="https://store.steampowered.com/"))
	bot.send_message(message.chat.id,"Ок" , parse_mode='html', reply_markup=markup)


#////////////////////////////////////////////////////////////
user_num1 =''
user_num2 =''
user_proc = ''
user_result = None


def process_num1_step(message, user_result = None):
    try:
       global user_num1


       if user_result == None:
          user_num1 = int(message.text)
       else:

          user_num1 = str(user_result)

       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
       itembtn1 = types.KeyboardButton('+')
       itembtn2 = types.KeyboardButton('-')
       itembtn3 = types.KeyboardButton('*')
       itembtn4 = types.KeyboardButton('/')


       markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

       msg = bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
       bot.register_next_step_handler(msg, process_proc_step)
    except Exception as e:
       bot.reply_to(message, 'Это не число ')


def process_proc_step(message):
    try:
       global user_proc
       user_proc = message.text
       markup = types.ReplyKeyboardRemove(selective=False)
       msg = bot.send_message(message.chat.id, "Введите второе число", reply_markup=markup)
       bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e:
       bot.reply_to(message, 'Это не число')


def process_num2_step(message):
    try:
       global user_num2
       user_num2 = int(message.text)
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
       itembtn1 = types.KeyboardButton('Результат')
       itembtn2 = types.KeyboardButton('Продолжить вычисление')
       markup.add(itembtn1, itembtn2)
       msg = bot.send_message(message.chat.id, " Результат или продолжить операцию?", reply_markup=markup)
       bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e:
       bot.reply_to(message, 'Это не число ')


def process_alternative_step(message):
    try:
       calc()
       markup = types.ReplyKeyboardRemove(selective=False)

       if message.text.lower() == 'результат':
          bot.send_message(message.chat.id, calcResultPrint(), reply_markup=markup)
       elif message.text.lower() == 'продолжить вычисление':
          process_num1_step(message, user_result)

    except Exception as e:
       bot.reply_to(message, 'Что то пошло не так...')


def calcResultPrint():
    global user_num1, user_num2, user_proc, user_result
    return "Результат: " + str(user_num1) + ' ' + user_proc + ' ' + str(user_num2) + ' = ' + str( user_result )


def calc():
    global user_num1, user_num2, user_proc, user_result
    user_result = eval(str(user_num1) + user_proc + str(user_num2))
    return user_result


@bot.message_handler(commands=['calculator'])
def send_welcome(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id,message.from_user.first_name + " введите число", reply_markup=markup)
    bot.register_next_step_handler(msg, process_num1_step)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()


bot.polling(none_stop=True)


