small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
unique_set = set(small_list)
print(unique_set)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
quantity_of_elements = len(small_list)
print(quantity_of_elements)
sum=0
for i in small_list:
    sum +=i
average = sum/quantity_of_elements
print(f"Average for values from the list is {average}")
# task 3. Перевірте, чи є в списку big_list дублікати
list_quantity = len(big_list)
set_quantity = len(set(big_list))
status = list_quantity > set_quantity
print(f"In list there are duplicates - {status}")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
list_values = list(add_dict.values())
max_val = max(list_values)
key_name = [key for key, val in add_dict.items() if val==12]
print(f"Max value {max_val} relates to key - {key_name[0]}")
# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {value: key for key, value in add_dict.items()}
print(new_dict)
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = base_dict | add_dict
for key in base_dict.keys():
    if key in add_dict.keys():
        value_combined = str(add_dict[key]) + str(base_dict[key])
        print(value_combined)
        sum_dict[key] = value_combined
print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print(set(line))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set3=list(set_1 ^ set_2)
sum=0
length = len(set3)
for i in range(length):
    sum +=set3[i]
print(sum)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Emma', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45), ('Tony', 15)]
set_1 = {1,2,3,4,5}
set_2 = {3,4,5,6,7,8,9}
set_3 = set_1 ^ set_2
print(set_3)
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

dict1= dict(person_list)
dict2 = {value: key for key, value in dict1.items()}
list1 = []
list2 = []
list3 = []
list4 = []
changed_dict ={'10-19':"", '20-29':"", '30-39':"", '40-49':""}
for (key1, val1), (key2, val2) in zip(dict1.items(), dict2.items()):
    if int(val1) >= 10 and int(val1)<=19:
        list1.append(val2)
        changed_dict['10-19'] = list1
    elif int(val1) >= 20 and int(val1)<=29:
        list2.append(val2)
        changed_dict['20-29'] = list2
    elif int(val1) >= 30 and int(val1) <= 39:
        list3.append(val2)
        changed_dict['30-39'] = list3
    else:
        list4.append(val2)
        changed_dict['40-49'] = list4
print(changed_dict)