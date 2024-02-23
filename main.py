import time
import requests_html
import telebot

bot = telebot.TeleBot('6989143962:AAF7ZhvpM_E0aXvTUoewR4q2A52mU1K1zY8')
id_channel = '@etweather'

last_processed_news = ''

from requests_html import HTMLSession
@bot.message_handler(content_types=['text'])
def command(message):
    global last_processed_news
    if message.text == "Start":
        while True:
            post_text = parser()

            if post_text is not None and post_text != last_processed_news:
                bot.send_message(id_channel, post_text, disable_web_page_preview=True)
                last_processed_news = post_text
            time.sleep(300)
    else:
        bot.send_message(message.from_user.id, "write Start")


def parser():
    s = HTMLSession()
    query = 'Addis Ababa'
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})

    if r:
        temp = r.html.find('span#wob_tm', first=True).text
        unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
        desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
        return f"{query}\n {temp}\n {unit}\n {desc}\n link: {'https://www.google.com/search?q=weather+addis+ababa'}"
    return


bot.polling()
