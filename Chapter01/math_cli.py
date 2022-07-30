import argparse


def math(number1, number2, type):
    if type == "+":
        print(number1 + number2)
    elif type == "-":
        print(number1 - number2)
    elif type == "/":
        print(number1 / number2)
    else:
        print(number1 * number2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number1', type=int, help="Number 1")
    parser.add_argument('number2', type=int, help="Number 2")
    parser.add_argument('-o', '--operator', type=str, default='+', help="Operators like +, -")
    args = parser.parse_args()

    math(args.number1, args.number2, args.operator)
