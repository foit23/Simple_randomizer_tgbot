from aiogram.types  import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard = [[KeyboardButton(text = "начать игру 🚀")]],
    resize_keyboard = True,
    one_time_keyboard = True
)


game_menu = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text = "Кубик 🎲", callback_data = "dice"), InlineKeyboardButton(text = "Дарц 🎯", callback_data = "darts")],
        [InlineKeyboardButton(text = "Баскетболл 🏀", callback_data = "basketball"), InlineKeyboardButton(text = "Футболл ⚽", callback_data = "football")],
        [InlineKeyboardButton(text = "Казино 🎰", callback_data = "slot_machine"), InlineKeyboardButton(text = "Боулинг 🎳", callback_data = "bowling")]
    ]
)