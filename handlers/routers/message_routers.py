import random

from aiogram import F, Router
from aiogram.types import Message

import text

router = Router()


@router.message(F.text.in_(text.welcome))
async def start_small_talk(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(text=f"{random.choice(text.welcome)}!")


@router.message(F.text.in_(text.bye))
async def finish_small_talk(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(text=f"{random.choice(text.bye)}!")


@router.message()
async def small_talk(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(text=msg.text)
