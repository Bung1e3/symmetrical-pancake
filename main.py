import telebot
from telebot import types

bot = telebot.TeleBot('1407758820:AAGs7QhHebGqiwGxKGREfmcpBm0eLFn39x4')

@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Наши контакты☎")
    item2 = types.KeyboardButton("Помочь с выбором")
    item3 = types.KeyboardButton("Оставить свои контакты")

    markup.add(item1, item2,item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nКак я могу помочь тебе?😊".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
@bot.message_handler(content_types=['text'])
def lalala(message):
        phone = " "
        if message.text[0] == '+':
            bot.send_message(message.chat.id,"Спасибо за то что выбрали нас!\nБудет работать как часы")
        else:
        #if message.chat.type == 'private':
            if message.text == 'Наши контакты☎':
                bot.send_message(message.chat.id," Instagram https://www.instagram.com/app.minsk/ \n Telegram: https://t.me/app_minsk")
            elif message.text == 'Помочь с выбором':
                markup1 = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Iphone📱", callback_data='iphone')
                item2 = types.InlineKeyboardButton("Apple Watch⌚", callback_data='watch')
                item3 = types.InlineKeyboardButton("Airpods🎧", callback_data='airpods')
                item4 = types.InlineKeyboardButton("Ipad", callback_data='ipad')
                item5 = types.InlineKeyboardButton("MacBook👨‍💻", callback_data='mac')
                markup1.add(item1, item2, item3, item4, item5)

                bot.send_message(message.chat.id, 'Давай мы тебе что-нибудь подберём?', reply_markup=markup1)
            elif message.text == 'Оставить свои контакты':
                phone = message.text
            else:
                bot.send_message(message.chat.id, 'Давай попробуем ешё раз, нажимай "Помочь с выбором"')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    r = " "
    k = call.message.chat.username
    k1 = call.message.chat.first_name

    try:
        if call.message:
            if call.data == 'airpods':
                r += "Apple"
                markupair = types.InlineKeyboardMarkup(row_width=2)
                air159 = types.InlineKeyboardButton("AirPods", callback_data='air159')
                air199 = types.InlineKeyboardButton("AirPods Wireless Case", callback_data='air199')
                air249 = types.InlineKeyboardButton("Airpods Pro", callback_data='air249')
                markupair.add(air159, air199, air249)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Выбирай какие AirPods ты хочешь?",
                                      reply_markup=markupair)

                @bot.callback_query_handler(func=lambda call: True)
                def callback_inline(call):
                    if call.data == 'air159':
                        r = "AirPods"
                        markupkup = types.InlineKeyboardMarkup(row_width=1)
                        itemair = types.InlineKeyboardButton("Заказыкаем",callback_data='YYAP')
                        markupkup.add(itemair)
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                         text='Прекрасный выбор, твои ' + r + ' у нас по самой лучшей цене <b>159$</b>\n<b>Хочешь зказать?</b>\n Укажи свой номер телефона и мы с тобой свяжемся!\nИли можешь написать нам @pedigri13 !!! ',
                                         reply_markup=markupkup, parse_mode='html')
                        # show alert
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                                  text="ХОРОШИЙ ВЫБОР!!! Давай продолжать")
                    elif call.data == 'air199':
                        r = " AirPods Wireless Case"
                        markupkup = types.InlineKeyboardMarkup(row_width=1)
                        itemair = types.InlineKeyboardButton("Заказыкаем", callback_data='YYAP')
                        markupkup.add(itemair)
                        # show alert
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                                  text="ХОРОШИЙ ВЫБОР!!! Давай продолжать")
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text='Прекрасный выбор, твои ' + r + ' у нас по самой лучшей цене <b>199$</b>\n<b>Хочешь зказать?</b>\n Жми "Заказываем", и с тобой свяжутся в TELEGRAM',
                                              reply_markup=markupkup, parse_mode='html')


            elif call.data == 'YYAP':
                bot.send_message(585138914,
                                 'Привет, у нас новый заказ от ' + k1 + '\nОн выбрал ' + r + '\nВот его номер телефона:' + '\nUsername @' + k + '\n')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Спасибо за заказ мы с тобой свяжемся в Telegram',
                                      reply_markup=None, parse_mode='html')

            elif call.data == 'iphone':
                r = "Iphone"
                markup = types.InlineKeyboardMarkup(row_width=1)
                iph1 = types.InlineKeyboardButton("IPhone 12/12 mini, 12 Pro/12 Pro Max📱", callback_data='i12')
                iph2 = types.InlineKeyboardButton("Iphone 11/11 Pro/11 Pro Max📱", callback_data='i11')
                iph3 = types.InlineKeyboardButton("Iphone Xr/Xs/Xs Max и ниже📱", callback_data='low')
                markup.add(iph1, iph2, iph3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Какой Iphone хочешь?",
                                      reply_markup=markup)
            elif call.data == 'watch':
                r = "Apple Watch"
                markupaw = types.InlineKeyboardMarkup(row_width=1)
                aws3 = types.InlineKeyboardButton("AW S3", callback_data='aws3')
                aws6 = types.InlineKeyboardButton("AW S6", callback_data='aws6')
                awsse = types.InlineKeyboardButton("AW SE", callback_data='awse')
                markupaw.add(aws3, aws6, awsse)
                bot.send_message(call.message.chat.id, 'Хорошо, давай подберём те которые ты хочешь)', reply_markup=markupaw)
                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Хорошо, давай подберём те которые ты хочешь)",
                                      reply_markup=None)
            elif call.data == 'ipad':
                r = "Ipad"
                markupip = types.InlineKeyboardMarkup(row_width=2)
                ip = types.InlineKeyboardButton("Ipad 10,2", callback_data='ip')
                ippro = types.InlineKeyboardButton("Ipad Pro", callback_data='ippro')
                ipair = types.InlineKeyboardButton("Ipad Air", callback_data='ipair')
                markupip.add(ip, ipair, ippro)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Прекрасно, давай вместе выберем твой новый Ipad",
                                      reply_markup=markupip)
            elif call.data == 'i12':
                r =  r + " 12"
                markup = types.InlineKeyboardMarkup(row_width=2)
                iph1 = types.InlineKeyboardButton("Iphone 12 Mini🔥", callback_data='i12mn')
                iph2 = types.InlineKeyboardButton("Iphone 12 ", callback_data='i12just')
                iph3 = types.InlineKeyboardButton("Iphone 12 Pro", callback_data='pro')
                iph4 = types.InlineKeyboardButton("Iphone 12 Pro Max🔥", callback_data='promax')
                markup.add(iph1, iph2, iph3,iph4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Как из новых Iphone тебе нужен?📱",
                                      reply_markup=markup)
            elif call.data == 'i11':
                r = r + " 11"
                markup = types.InlineKeyboardMarkup(row_width=2)
                iph1 = types.InlineKeyboardButton("Iphone 11", callback_data='i1161')
                iph3 = types.InlineKeyboardButton("Iphone 11 Pro", callback_data='11pro')
                iph4 = types.InlineKeyboardButton("Iphone 11 Pro Max", callback_data='11promax')
                markup.add(iph1, iph3, iph4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Какой объём памяти выбираем?",
                                      reply_markup=markup)
            elif call.data == 'low':
                r = r + " X"
                markup = types.InlineKeyboardMarkup(row_width=2)
                iph1 = types.InlineKeyboardButton("Iphone Xr", callback_data='ixr')
                iph3 = types.InlineKeyboardButton("Iphone Xs", callback_data='ixs')
                iph4 = types.InlineKeyboardButton("Iphone Xs Max", callback_data='ixsmax')
                markup.add(iph1, iph3, iph4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какой Ipone выбираем?",
                                  reply_markup=markup)
            elif call.data == 'i12mn' or 'i12just':
                r = r + " Mini"
                markup = types.InlineKeyboardMarkup(row_width=1)
                iph1 = types.InlineKeyboardButton("64 Gb", callback_data='i12mn64')
                iph3 = types.InlineKeyboardButton("128 Gb🔥", callback_data='i12mn128')
                iph4 = types.InlineKeyboardButton("256 Gb", callback_data='i12mn256')
                markup.add(iph1, iph3, iph4)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какой объём памяти?💾",
                                  reply_markup=markup)
            elif call.data == 'i12mn64':
                if call.data == 'i12mn64':
                    r = r + " 64 Gb"
                elif call.data == 'i12mn128':
                    r = r + ' 128 Gb'
                else:
                    r = r + '256 Gb'
                markup = types.InlineKeyboardMarkup(row_width=1)
                iph1 = types.InlineKeyboardButton("Белый🤍", callback_data='i12wh')
                iph3 = types.InlineKeyboardButton("Чёрный🖤", callback_data='i12bl')
                iph4 = types.InlineKeyboardButton("Зелёный💚", callback_data='i12gr')
                iph2 = types.InlineKeyboardButton("Синий💙", callback_data='i12blue')
                iph5 = types.InlineKeyboardButton("Красный❤️", callback_data='i12red')
                markup.add(iph1, iph3, iph4, iph2, iph5)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какой объём памяти?💾",
                                  reply_markup=markup)

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)