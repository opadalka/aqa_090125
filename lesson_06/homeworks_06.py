# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color_list = ['green', 'yellow', 'red']
for alien_color in alien_color_list:
    if alien_color == 'green':
        print("You just earned 5 points")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
for alien_color in alien_color_list:
    if alien_color == 'green':
        print("You just earned 5 points")
    else:
        print("You just earned 10 points")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
for alien_color in alien_color_list:
    if alien_color == 'green':
        print("You just earned 5 points")
    elif alien_color == 'red':
        print("You just earned 15 points")
    else:
        print("You just earned 10 points")
# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
stop_word = "quit"
pizza_topping_list = []
for i in range(7):
    pizza_topping = input("What topping do you want:")
    if pizza_topping != stop_word:
        print(f"You have added {pizza_topping} to your pizza")
        pizza_topping_list.append(pizza_topping)
    else:
        "You are finished with extra toppings"
        break
print(pizza_topping_list)
# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
natural_number = input("Enter number:")
list_of_numbers = list(natural_number)
sum = 0
for i in range(len(list_of_numbers)):
    sum += int(list_of_numbers[i])
print(f"Sum of all entered digits is: {sum}")
# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

summary = 0
i=1
while i >0:
    number = int(input("Enter digit:"))
    summary +=number
    i = number
    if i==0:
        print(f"Total sum is {summary}")
        break

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for i in range(max_guesses):
    player_number = int(input("Type your assumption:"))
    if player_number == secret_number:
        print("You WON!")
        break
    elif player_number > secret_number:
        print(f"You entered number which is greater")
    else:
        print(f"You entered number which is smaller")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
for elem in fruits:
    if elem != 'orange':
        print(f"Fruit item is : {elem}")
    else:
        continue
# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i%2==0]
print(result)  #  [4, 16, 36, 64, 100]
