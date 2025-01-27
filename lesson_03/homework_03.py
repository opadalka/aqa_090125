# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = f"\'Would you tell me, please, which way I ought to go from here?\'\n"\
f"\'That depends a good deal on where you want to get to\' - said the Cat.\n"\
f"\'I don\'t much care where\' —— said Alice.\n"\
f"\'Then it doesn\'t matter which way you go\' - said the Cat.\n"\
f"\'So long as I get somewhere\' - Alice added as an explanation.\n"\
f"\'Oh, you're sure to do that\' - said the Cat - \'if you only walk long enough.\'"
print(alice_in_wonderland)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_BlackSea = 436402
square_AzovSea = 37800
print(f"Площа Чорного моря становить {square_BlackSea} км2, \n"\
f"а площа Азовського моря становить {square_AzovSea} км2.\n"\
f"Чорне та Азовське моря разом займають площу {square_BlackSea+square_AzovSea} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
products_quantity_general = 375291
products_quantity_3 = products_quantity_general - 250449
products_quantity_2 = 222950 - products_quantity_3
products_quantity_1 = products_quantity_general - (products_quantity_3 + products_quantity_2)
print(f"На 1 складі розміщується {products_quantity_1} товарів, на 2 складі - {products_quantity_2}, на 3 складі - {products_quantity_3}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_toBePaid = 18
payment_sum = 1179
computer_price = payment_sum * month_toBePaid
print(f"Вартість комп’ютера становитиме {computer_price} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019%8
print(f"Остача від ділення {a}")
b = 9907%9
print(f"Остача від ділення {b}")
c = 2789%5
print(f"Остача від ділення {c}")
d = 7248%6
print(f"Остача від ділення {d}")
e = 7128%5
print(f"Остача від ділення {e}")
f = 19224%9
print(f"Остача від ділення {f}")
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
food_dict = {
    "pizzaL":"4",
    "pizzaS":"2",
    "juice":"4",
    "cake":"1",
    "water":"3"
}
price_dict ={
    "pizzaL":"274",
    "pizzaS":"218",
    "juice":"35",
    "cake":"350",
    "water":"21"
}
sum_total =0
for (key1,val1), (key2,val2) in zip(food_dict.items(), price_dict.items()):
    sum_total += int(val1)*int(val2)
print(f"Загальна вартість продуктів {sum_total} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_quantity = 232
photo_num = 232//8
print(f"Знадобиться {photo_num} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?

"""
distance = 1600
petrol_quantity = distance//100*9
stop_quantity = petrol_quantity//48
print(f"Необхідно бензину для подорожі {petrol_quantity} літра. Кількість заправок становитиме {stop_quantity}")