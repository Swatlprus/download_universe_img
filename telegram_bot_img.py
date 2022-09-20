import telegram
from environs import Env

env = Env()
env.read_env()
telegram_token = env("TELEGRAM_TOKEN")

bot = telegram.Bot(token=telegram_token)
bot.send_photo(chat_id='@img_universe', photo=open('images/apod_0.jpg', 'rb'))
print(bot.get_me())