from aiogram.utils.keyboard import InlineKeyboardBuilder

import text

currency_dict = {
    text.eur: text.eur,
    text.rub: text.rub,
    text.gbp: text.gbp,
    text.cny: text.cny,
    text.usd: text.usd,
}


def currency_button():
    """Перечень валют для конвертации"""
    inline_keyboard = InlineKeyboardBuilder()
    for text_button, callback in currency_dict.items():
        inline_keyboard.button(text=text_button, callback_data=callback)

    inline_keyboard.adjust(2, 2)
    return inline_keyboard.as_markup()
