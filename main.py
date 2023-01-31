import requests
import telegram
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "5771432493:AAHEBM57dN76_r5WXFYHPJvIEDoM00eJct0"
API_URL = "https://yannlevy-openai-whisper-stt.hf.space/api/predict"

def transcribe(bot, update):
    audio = update.message.voice.get_file().download_as_bytearray()
    payload = {
        "data": [
            {
                "name": "voice.ogg",
                "data": audio.decode("utf-8")
            },
            None,
            "small",
            None,
            "English",
            None
        ]
    }
    response = requests.post(API_URL, json=payload)
    transcription = response.json()["data"][0]
    bot.send_message(chat_id=update.message.chat_id, text=transcription)

bot = telegram.Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

voice_handler = MessageHandler(Filters.voice, transcribe)
dispatcher.add_handler(voice_handler)

updater.start_polling()
