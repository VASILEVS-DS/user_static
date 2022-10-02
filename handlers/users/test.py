from aiogram import types
from loader import dp
from keybords.default import kb_test

@dp.message_handler(text='Любой текст')
async def test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Тут должен быть какой-нибудь текст', reply_markup=kb_test)
