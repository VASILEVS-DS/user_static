from aiogram import types
from keybords.inline import ikb_menu
from loader import dp
from aiogram.types import CallbackQuery
from keybords.default import kb_test

'''
@dp.message_handler(text='Инлайн меню')
async def show_inline_menu(message: types.Message):
    await message.answer('Инлайн кнопки ниже', reply_markup=ikb_menu)

@dp.callback_query_handlers(text='Сообщение')
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки заменены', reply_markup=kb_test)


@dp.callback_query_handlers(text='alert')
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки заменены', show_alert=True)
'''