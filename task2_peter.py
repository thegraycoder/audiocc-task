def compute_highest_number(number, idx, last_digit, x):
    length = len(str(number))
    if idx == length:
        if x <= number:
            return x
        return 0
    else:
        digit = 9
        while digit >= last_digit:
            y = x * 10 + digit
            result = compute_highest_number(number, idx + 1, digit, y)
            if result > 0:
                return result
            digit -= 1
    return 0


def meditate(number):
    return compute_highest_number(number, 0, 0, 0)


if __name__ == '__main__':
    peters_number = input("Enter the number: ")
    res = meditate(int(peters_number))
    print(f'Last number written down by Peter is: {res}')
