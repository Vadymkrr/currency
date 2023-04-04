from _decimal import Decimal


def to_2_places_decimal(value: str) -> Decimal:
    '''
    Conver str value to Decimal with 2 places
    example:
        Input: str('123 456') -> Output: Decimal(123.45)
    '''
    return round(Decimal(value), 2)
