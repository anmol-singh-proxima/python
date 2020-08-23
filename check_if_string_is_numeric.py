
# This program checks if the entered input is numeric(i.e. number either int or float) or not
# It is basically for handling the exception caused due to the wrong input.

def is_number(num):
    """This function checks if the entered string is numeric(either int or float) or not"""
    num = num.strip()
    if num.isdigit():
        return True
    else:
        part = num.partition('.')
        if ((part[0].isdigit() and part[1] == '.' and part[2].isdigit()) or
                (part[0].isdigit() and part[1] == '.' and part[2] == "") or
                (part[0] == "" and part[1] == '.' and part[2].isdigit())):
            return True
    return False


def is_float(num):
    """This function checks if the entered string is a floating point number or not"""
    num = num.strip()
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_integer(num):
    """This function checks if the entered string is an integer or not"""
    num = num.strip()
    try:
        int(num)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    number = input("Enter a number: ")
    number = number.strip()
    if is_number(number):
        print(f"{number} is a number")
    if is_float(number):
        print(f"{number} is a float")
    if is_integer(number):
        print(f"{number} is an integer")
