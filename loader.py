from aiogram import Bot, Dispatcher, types
from utils.db_api.db_gino import db
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

storage = MemoryStorage()
__all__ = ['bot', 'dp', 'db']