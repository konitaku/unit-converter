from decimal import Decimal, ROUND_HALF_UP


def convert(num: float, init_unit: str, change_unit: str) -> int:
    result = 0
    if init_unit == "m":
        cv_rate = {
            "m": 1,
            "mile": 1/1609,
            "yard": 1.09,
            "feet": 3.281,
            "inch": 39.370
        }
        result = num * cv_rate[change_unit]
        result = Decimal(str(result)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    if init_unit == "mile":
        cv_rate = {
            "m": 1609,
            "mile": 1,
            "yard": 1760,
            "feet": 5280,
            "inch": 63360
        }
        result = num * cv_rate[change_unit]
        result = Decimal(str(result)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    if init_unit == "yard":
        cv_rate = {
            "m": 1/1.094,
            "mile": 1/1760,
            "yard": 1,
            "feet": 3,
            "inch": 36
        }
        result = num * cv_rate[change_unit]
        result = Decimal(str(result)).quantize(Decimal('0.0000001'), rounding=ROUND_HALF_UP)
    if init_unit == "feet":
        cv_rate = {
            "m": 1/3.281,
            "mile": 1/5280,
            "yard": 1/3,
            "feet": 1,
            "inch": 12
        }
        result = num * cv_rate[change_unit]
        result = Decimal(str(result)).quantize(Decimal('0.0000000001'), rounding=ROUND_HALF_UP)
    if init_unit == "inch":
        cv_rate = {
            "m": 1/39.37,
            "mile": 1/63360,
            "yard": 1/36,
            "feet": 1/12,
            "inch": 1
        }
        result = num * cv_rate[change_unit]
        result = Decimal(str(result)).quantize(Decimal('0.0000000001'), rounding=ROUND_HALF_UP)
    return result
