#Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
#Наприклад:[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
#Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
#Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити
#вийняток і вивести “Не можу це зробити!”
#Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
#Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”"""

def sum_all_values(data):
    for elem in data:
        list_numbers = elem.split(",")
        summ = 0
        for i in list_numbers:
            try:
                digit = int(i)
            except ValueError:
                print("I can't do this")
                break
            else:
                summ += digit
        if summ != 0:
            print(summ)


data_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
sum_all_values(data_list)