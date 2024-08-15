def print_pattern(length):
    if length < 1:
        return "Enter a number greater than or equal to 1"
    if length % 1 != 0:
        return "Provide a positive integer value greater than or equal to 1"
    else:
        return pattern(length)  # Here i am calling pattern function with valid integer

# Pattern generation function
def pattern(length):
    column = ((length * 2) + 3)
    kite = ((length * 2) + 1)
    lst_row = length

    # Upper part of the kite
    for i in range(0, (kite // 2)):
        for j in range(0, kite + 2):
            if j == (kite // 2) - i + 1:
                print("*", end="")
            elif j == (kite // 2) + i + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

    # Middle part with the number
    for i in range(1):
        for j in range(0, kite + 2):
            if (j == i + 1):
                print("*", end="")
            elif j == ((kite + 2) // 2):
                print(length, end="")
            elif j == kite:
                print("*", end="")
                break
            else:
                print(" ", end="")
        print("")

    # Lower part of the kite
    for i in range(0, (kite // 2) - 1):
        for j in range(0, kite + 1):
            if j == i + 2:
                print("*", end="")
            elif j == (kite + 1) - i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

    # Bottom part of the kite
    for i in range(0, lst_row):
        for j in range(0, column):
            print("*", end="")
        print("")

    return ""


print(print_pattern(5))  
