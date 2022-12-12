from .user_filters import IsFather
from dispatcher import dp

if __name__ == "filters":
    dp.filters_factory.bind(IsFather)