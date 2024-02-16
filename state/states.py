from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    """Состояния выбора пользователя"""

    currency = State()
    amount = State()
