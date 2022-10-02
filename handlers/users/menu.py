from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from keybords.default import kb_menu



@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    await message.answer("Выбери число из меню ниже", reply_markup=kb_menu)