from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

import text as text
from keyboards.inline.currency import currency_button

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext) -> None:
    """Обработка команды start"""
    # await state.set_state(UserState.currency)
    await msg.answer(
        text.start.format(name=msg.from_user.full_name),
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(Command("help"))
async def get_menu(msg: Message) -> None:
    """Обработка команды menu"""
    await msg.answer(text.help, reply_markup=ReplyKeyboardRemove())


@router.message(Command("convert"))
async def cancel_handler(msg: Message) -> None:
    """Обработка команды cancel"""
    await msg.answer(text.convert, reply_markup=currency_button())
