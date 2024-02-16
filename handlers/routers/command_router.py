from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

import text as text
from keyboards.inline.currency import currency_button

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    """Обработка команды start"""
    await msg.answer(
        text.start.format(name=msg.from_user.full_name),
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("help"))
async def get_help(msg: Message) -> None:
    """Обработка команды help"""
    await msg.answer(text.help, reply_markup=ReplyKeyboardRemove())


@router.message(Command("convert"))
async def get_convert(msg: Message) -> None:
    """Обработка команды convert"""
    await msg.answer(text.convert, reply_markup=currency_button())
