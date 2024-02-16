from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from services import convert_currency
from state.states import UserState

router = Router()


@router.message(UserState.amount, F.text.regexp(r"^(\d+)$"))
async def get_currency(msg: Message, state: FSMContext) -> None:
    """Получение выбранной валюты"""

    await state.update_data(amount=msg.text)
    result = await state.get_data()
    rate = await convert_currency(
        base_currency=result.get("currency"), amount=int(result.get("amount"))
    )
    formatted_text = "\n".join([f"{key}: {value}" for key, value in rate.items()])
    await msg.answer(
        f"Актуальная конвертация {result.get('amount')} {result.get('currency')} на данный момент равна :\n{formatted_text}"
    )
    await state.clear()
