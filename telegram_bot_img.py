import telegram
from environs import Env

env = Env()
env.read_env()
telegram_token = env("TELEGRAM_TOKEN")

bot = telegram.Bot(token=telegram_token)
bot.send_message(chat_id='@img_universe', text="I'm sorry Dave I'm afraid I can't do that.")
print(bot.get_me())