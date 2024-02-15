from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

import text as text
from state.states import UserState

router = Router()


@router.callback_query()
async def convert_eur(query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(UserState.currency)
    await state.update_data(currency=query.data)
    # await query.message.answer(text=text.choice_currency.format(currency=query.data))
    await query.message.answer(
        text=text.amount.format(currency=query.data), reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserState.amount)
