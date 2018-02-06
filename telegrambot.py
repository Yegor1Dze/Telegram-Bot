#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

GROUP_ID = -1001312654220 #

def start(bot, update):
    update.message.reply_text(
    """
    Бот создан исключительно (возможно пока что) для 9-Б класса 106 школы!
    
    Список всех команд:

    /start - выводит данное сообщение
    /help - тоже самое, что и /start
    /shedule - рассписание на неделю
    /changes - замены/изменения в рассписании (только на следующий день)

    Больше функций будет добавлено позже!
    """)


def shedule_day(bot, update):
    keyboard = [[InlineKeyboardButton("Понедельник", callback_data='1'),
                 InlineKeyboardButton("Вторник", callback_data='2'),
                 InlineKeyboardButton("Среда", callback_data='3')],

                [InlineKeyboardButton("Четверг", callback_data='3'),
                InlineKeyboardButton("Пятница", callback_data='4'),
                InlineKeyboardButton("Мероприятия", callback_data='6')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите день недели:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="Вы выбрали: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)



def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("419019533:AAFaakkQ3uOUI89DGMUktA4t_U_4pn99CQs")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('shedule', shedule_day))  
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', start))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

#-1001312654220