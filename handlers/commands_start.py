from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
import asyncio

content_chat = -1001780671252
ids_user = []
markup = types.InlineKeyboardMarkup()

bat_1 = types.InlineKeyboardButton(text='🍼Р0DDOM (D0 4)🍼', callback_data='bat_1')
bat_2 = types.InlineKeyboardButton(text='👶Л@П0ЧkИ (I0+-)👶', callback_data='bat_2')
bat_3 = types.InlineKeyboardButton(text='🎒|||k0льNицы🎒(I4+-)', callback_data='bat_3')
bat_4 = types.InlineKeyboardButton(text='📚STУDENТКИ (I7+-)📚', callback_data='bat_4')
bat_5 = types.InlineKeyboardButton(text='🏆🤑Всё тарифы вместе🤑🏆', callback_data='bat_5')

markup.add(bat_1)
markup.add(bat_2)
markup.add(bat_3)
markup.add(bat_4)
markup.add(bat_5)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(id = message.chat.id)
    await message.answer(text="""<b>✅ Вы успешно активировали промокод.
Вам доступна скидка в 20% </b>""")

    await bot.copy_message(chat_id=message.chat.id,message_id=5,from_chat_id=content_chat) #Отправка приветсвия
    await message.answer(text="""<b>Выберите желаемый товар или категорию:</b>""",reply_markup=markup)