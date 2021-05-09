import telebot
import time
import pyshorteners

TG_BOT_TOKEN = ''

bot = telebot.TeleBot(token=TG_BOT_TOKEN)

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Heya! I am a File To Link Bot created by TeLe TiPs.Send me any file (Video, Audio, Photo, Document)👇🏻')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Send me any type of a file & I will send you the shorten link of it')  

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


if __name__ == "__main__":
    plugins = dict(root="plugins")
    bot = Client(
        "FileToLink",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    bot.run()

