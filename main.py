import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
from aiogram.enums import DiceEmoji

bot = Bot(token = "8326658640:AAHQP51BPk9oZBdlfNNqL60_iuO16TN4sgI")
bot = Bot(token = "YOUR TOKEN")
dp = Dispatcher()

@dp.message(Command("start"))
async def starts(message = types.Message):
    await message.answer("Бот который просто кидает игральную кость, для броска введите команду /Reroll \n Автор бота: @foit_23")

@dp.message(Command("Reroll"))
async def reroll(message = types.Message):
    await message.answer_dice(emoji = DiceEmoji.DICE)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())