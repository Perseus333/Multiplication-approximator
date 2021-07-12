import random


print('Random numbers[R] or manually inserted numbers[M]? ')
type_of_numbers = str(input('> ')).lower()


def random_decimal():
    return random.uniform(0.1, 99.9)


def ten_rounder(number):
    ten = round(number / 10) * 10
    return ten


def difference_between_ten(number, ten):
    return abs(ten - number)


# To choose between a random number and pre-selected numbers
if type_of_numbers == 'r':
    number1 = random_decimal()
    number2 = random_decimal()

elif type_of_numbers == 'm':
    print('It is recommended to insert a value smaller than 100')
    number1 = input('Write the first number: ')
    number2 = input('Write the second number: ')
    number1 = number1.replace(',', '.')
    number2 = number2.replace(',', '.')
    number1 = float(number1)
    number2 = float(number2)

else:
    print('You can only select one of two values: "R" for random or "M" to select them manually')
    number1 = random_decimal()
    number2 = random_decimal()


number1_rounded = ten_rounder(number1)
number2_rounded = ten_rounder(number2)

difference1 = difference_between_ten(number=number1, ten=number1_rounded)
difference2 = difference_between_ten(number=number2, ten=number2_rounded)


if difference1 < difference2 and number1 < number1_rounded:
    easy_number1 = number1_rounded
    easy_number2 = round(number2) - difference1

elif difference1 < difference2 and number1 > number1_rounded:
    easy_number1 = number1_rounded
    easy_number2 = round(number2) + difference1

elif difference1 > difference2 and number2 < number2_rounded:
    easy_number1 = round(number1) - difference2
    easy_number2 = number2_rounded

elif difference1 > difference2 and number2 > number2_rounded:
    easy_number1 = round(number1) + difference2
    easy_number2 = number2_rounded
else:
    easy_number1 = number1_rounded
    easy_number2 = number2_rounded

# To prevent small numbers to cause a 100% difference
if number1 < 10:
    easy_number1 = round(number1)
if number2 < 10:
    easy_number2 = round(number2)


final_output = round(easy_number1 * easy_number2)

real_value = number1 * number2
final_difference = round(abs(real_value - final_output), 2)
final_relative_difference = round((final_difference / real_value) * 100, 2)


print(f'Number 1 was: {number1}')
print(f'Number 2 was: {number2}')
print('-------------')
print(f'Approximate value was: {final_output}')
print(f'Real value was: {real_value}')
print(f'The difference was: {final_difference}')
print(f'The relative difference was: {final_relative_difference}%')
