# -*- coding: utf-8 -*-
import config
import telebot
import os
import validators
from selenium import webdriver

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    uid = message.chat.id
    url = ""
    try:
        url=message.text
    except IndexError:
        bot.send_message(uid, 'You have not entered URL!')
        return
    if not validators.url(url):
        bot.send_message(uid, 'URL is invalid!')
    else:
        photo_path = str(uid) + '.png'
        driver = webdriver.Chrome('/home/vitalik/Downloads/chromedriver')
        driver.get(message.text)

        driver.set_window_size(1920, 1080)
        driver.get(url)
        driver.save_screenshot(photo_path)
        bot.send_photo(uid, photo=open(photo_path, 'rb'))
        driver.quit()
        os.remove(photo_path)

if __name__ == '__main__':
     bot.infinity_polling()