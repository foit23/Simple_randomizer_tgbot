import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
from aiogram.enums import DiceEmoji
from aiogram import F
import keyboard



bot = Bot(token = "8326658640:AAHQP51BPk9oZBdlfNNqL60_iuO16TN4sgI")
dp = Dispatcher()

@dp.message(Command("start"))
async def starts(message = types.Message):
    await message.reply("Бот который просто кидает игральную кость\nАвтор бота: @foit_23 \nЕсли вы хотите начать играть, нажмите соответствующую кнопку", reply_markup = keyboard.main)
    

@dp.message(F.text == "начать игру 🚀")
async def start_game_menu(message: types.Message):
    await message.answer("Нажмите соответствующую кнопку для выбора игры", reply_markup = keyboard.game_menu)

@dp.callback_query(F.data == "dice")
async def dice_em(callback: types.CallbackQuery):
    await callback.message.answer_dice(emoji = DiceEmoji.DICE)

@dp.callback_query(F.data == "darts")
async def darts_em(callback: types.CallbackQuery):
    await callback.message.answer_dice(emoji = DiceEmoji.DART)

@dp.callback_query(F.data == "basketball")
async def basket_em(callback: types.CallbackQuery):
    await callback.message.answer_dice(emoji = DiceEmoji.BASKETBALL)

@dp.callback_query(F.data == "football")
async def foot_em(callback: types.CallbackQuery):
    await callback.message.answer_dice(emoji = DiceEmoji.FOOTBALL)

@dp.callback_query(F.data == "slot_machine")
async def slot_em(callback: types.CallbackQuery):
    await callback.message.answer_dice(emoji = DiceEmoji.SLOT_MACHINE)

@dp.callback_query(F.data == "bowling")
async def bow_em(callback: types.CallbackQuery):
    await callback.message.answer_dice(emoji = DiceEmoji.BOWLING)


@dp.message(Command("Reroll"))
async def reroll(message = types.Message):
    await message.answer_dice(emoji = DiceEmoji.DICE)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())