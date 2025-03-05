# Python calculator  #CONDITIONS


def calculator():
    n = float(input("Enter 1st Number: "))
    op = input("Type the operator (add/sub/mul/div/pow/squ): ").lower()
    n2 = float(input("Enter 2th Number: "))

    if op in ('div', 'squ') and n2 == 0:  # can't divide by zero
        return "Can't divide by 0"
    elif op == 'add':
        return n + n2
    elif op == 'sub':
        return n - n2
    elif op =='mul':
        return n * n2
    elif op == 'div':
        return round(n / n2, 4)
    elif op == 'pow':
        return pow(n, n2)  # n ** n2
    elif op == 'squ':
        return round(n ** (1 / n2), 4)  # pow(n, 1/n2)
    else:
        return f"Bad Operator name: '{op}'"


print(calculator())



