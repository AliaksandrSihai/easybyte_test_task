import random

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

import text
from keyboards.inline.currency import currency_button

router = Router()

@router.message(F.text.in_(text.welcome))
async def start_small_talk(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(text=f'{random.choice(text.welcome)}!')

@router.message(F.text.in_(text.bye))
async def finish_small_talk(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(text=f'{random.choice(text.bye)}!')

@router.message()
async def small_talk(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(text=msg.text)

