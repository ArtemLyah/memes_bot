from aiogram.dispatcher.filters.state import StatesGroup, State

# create state group that will be used in handling messages on different levels
# the methods will be levels or pages of the bot's answers

class Statemachine(StatesGroup):
    s1 = State()