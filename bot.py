from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from vkparse import get_members, get_intersection
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

f1 = get_members("eternalclassic")
s2 = get_members("afterpiece")
get_intersection(f1, s2)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(get_intersection(f1, s2))


if __name__ == '__main__':
    executor.start_polling(dp)