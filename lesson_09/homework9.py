
# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 1
    list_result = []
    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
        # Enter the action to take if the result is greater than 25
            break
        else:
            #print(str(number) + "x" + str(multiplier) + "=" + str(result))
            list_result.append(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
            multiplier += 1
    print(*list_result, sep="\n")
    




# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_value(a, b):
    try:
        c= a + b
        return c
    except TypeError:
        return False

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(list):
    avr_value = sum(list, 0)/len(list)
    return int(avr_value)


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
    return opposite_list


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest(list_words):
    max_val_list = [len(elem) for elem in list_words]
    index1 = max_val_list.index(max(max_val_list))
    return list_words[index1]
    



if __name__ == "__main__":
   # list2 = ["Hello", "Pet", "Animal", "Sophisticated", "Umbrella"]
    #longest(list2)
    #val = "Hello my dear friend"
    #val1 = ["H", "e", "l", "l", "o"]
    #print(opposite([1, 2, 3, 4]))
    #list1 = [1, 2, 3, 6]
    #print(average(list1))
    print(multiplication_table(3))
    #sum_value("a", 5)