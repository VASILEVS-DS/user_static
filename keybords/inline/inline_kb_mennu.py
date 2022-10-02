from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Сообщение', callback_data='Сообщение'),
                                        InlineKeyboardButton(text='Ссылка', url='https://www.youtube.com/watch?v=dYcj8H1LhV0')
                                    ],
                                    [
                                        InlineKeyboardButton(text='alert', callback_data='alert')
                                    ]
                                ])