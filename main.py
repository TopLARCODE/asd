import logging
import os
from random import randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
waiting = 0
TOKEN = "5578158606:AAEzBwvCx0DvnsIVO07l-vmsL-9MLIMNdxo"
ADMIN_ID = "1764135502"
CHANNEL_ID = "@FrostyNew"
LINK = "https://t.me/+lC38pJ-tiZdkYjVi"
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

mainMenu = InlineKeyboardMarkup(row_width=1)
btnRandom = InlineKeyboardButton(text="👤 Подписаться", url="https://t.me/FrostyNew")
btnUrl = InlineKeyboardButton(text="✅  Проверить Подписку", callback_data="btnAbout")
mainMenu.insert(btnRandom)
mainMenu.insert(btnUrl)
btnLink = InlineKeyboardButton(text="✅ Ссылка На Софт", url=LINK)
mainMenu2 = InlineKeyboardMarkup(row_width=1)
mainMenu2.insert(btnLink)
def check_sub(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        if chat_member['status'] != 'kicked':
            return True
        else:
            return False
    else:
            return False

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(ADMIN_ID, "@{0.username} написал(а) " + message.text + "".format(message.from_user), parse_mode="Markdown")
        print("ID " + str(message.from_user.id) + " Написал(а) "+ message.text)
        await bot.send_message(message.from_user.id, "✅ *{0.first_name}*, Добро пожаловать!\nЭто - бот который за подписку на канал «*Fʀᴏsᴛʏ*» выдаст вам софт.\nЖду вашего ответа❗️".format(message.from_user), parse_mode= 'Markdown', reply_markup=mainMenu)


@dp.callback_query_handler(text="btnAbout")
async def bot_message(message: types.Message):
    #await bot.send_message(ADMIN_ID, "@{0.username} написал(а) " + message.text + "".format(message.from_user), parse_mode="Markdown")
    #print("ID " + str(message.from_user.id) + " Написал(а) "+ message.text)
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.delete_message(message.from_user.id, message.message.message_id)
        await bot.send_message(message.from_user.id, "✅ *{0.first_name}*, Спасибо за подписку!\nНе отписывайтесь , ведь там очень много крутого❗️".format(message.from_user), parse_mode= 'Markdown', reply_markup=mainMenu2)
    else:
        await bot.delete_message(message.from_user.id, message.message.message_id) 
        await bot.send_message(message.from_user.id, "✅ *{0.first_name}*, Вы не подписались на канал.".format(message.from_user), parse_mode= 'Markdown', reply_markup=mainMenu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)




