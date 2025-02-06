# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 1

    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
            multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sumVal(a, b):
    c=a+b
    return c

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(list):
    avr_value = sum(list, 0)/len(list)
    return avr_value

list1 = [1, 2, 4, 54, 65, 21, 99]
average_value = average(list1)
print("Average is", average_value)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def opposite(value):
    opposite_list = []
    list_str = list(value)
    length = len(list_str)
    for i in range(length):
        index = (length-1) -i
        opposite_list.append(list_str[index])
    print(opposite_list)

val = "Hello my dear friend"
opposite(val)
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest(list_words):
    max_val_list = [len(elem) for elem in list_words]
    index1 = max_val_list.index(max(max_val_list))
    print(list_words[index1])

list2 = ["Hello", "Pet", "Animal", "Sophisticated", "Umbrella"]
longest(list2)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    value2 = str1.find(str2, 0)
    if value2 >=0:
        return value2
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def is_even(numbers):
    sum = 0
    for i in numbers:
        if i%2==0:
            sum +=i
    return sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Total sum {is_even(numbers)}")

# task 8
def findStrElements(list):
    lst2 =[]
    for i in lst1:
        if isinstance(i, str):
            lst2.append(i)
    return(lst2)

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(findStrElements(lst1))

# task 9
def findLetter():
    i=1
    while i>0:
        input_word = input("Enter word:")
        index1 = input_word.find("H")
        index2 = input_word.find("h")
        if index1 >=0 or index2 >=0:
            i=0
        else:
            i+=1
findLetter()
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
def countSum(number):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum

natural_number = list(input("Enter number:"))
print(countSum(natural_number))