from sys import argv

def pen_and_apple(pen_count, apple_count):
    print "I have %d pens," % pen_count,
    print "I have %d apples." % apple_count
    print "Uh! Apple-Pen!"

def plus_number(number1, number2):
    return number1 + number2

pen_and_apple(10, 10)

pen_and_apple(10 + 5, 10 / 3 - 2)

amount_of_pen = 20
amount_of_apple = 20
pen_and_apple(amount_of_pen, amount_of_apple)
pen_and_apple(amount_of_pen + 5, amount_of_apple / 3 - 3)
amount = 7
pen_and_apple(amount_of_pen + amount, amount_of_apple / amount)

script, pen, apple = argv
int_of_pen = int(pen)
int_of_apple = int(apple)
pen_and_apple(int_of_pen, int_of_apple)
pen_and_apple(int_of_pen + 5, int_of_apple - 5)
pen_and_apple(int_of_pen * amount / 5, int_of_apple / amount)
pen_and_apple(plus_number(amount, amount), amount)

int_of_pen = int(raw_input("Input pens amount: "))
int_of_apple = int(raw_input("Input apples amount: "))
pen_and_apple(int_of_pen, int_of_apple)
