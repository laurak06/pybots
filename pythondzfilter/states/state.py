from aiogram.fsm.state import State, StatesGroup


class UserFrom(StatesGroup):
    name = State()
    time = State()
    exact = State()


class ChooseFood(StatesGroup):
    food_name = State()
    food_size = State()


class ChooseDrink(StatesGroup):
    drink_name = State()
    drink_size = State()