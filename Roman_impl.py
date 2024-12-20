def decimal(num: str, base: int) -> int:
    try:
        return int(num, base)
    except ValueError:
        raise ValueError("invalid literal for rom() with base "+str(base)+": '"+num+"'")

def rom(num: str, base: int = 10) -> str:
    decimal_number = decimal(num, base)

    if decimal_number < 1:
        return "Number must be greater than 0"
    if decimal_number > 3999:
        return "Number must be 3999 or less for traditional romannumber numerals"

    value_to_romannumber = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    
    romannumber = ''
    for value, numeral in value_to_romannumber:
        while decimal_number >= value:
            romannumber += numeral
            decimal_number -= value

    return romannumber


print(rom("59"))