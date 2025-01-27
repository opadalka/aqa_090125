# task 01 == Виправте синтаксичні помилки
print("Hello", " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"

print(hello, world)

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter[0])

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(banana,"vs",apples)

# task 05 == виправте назви змінних
side1 = 1
side2 = 2
side3 = 3
side4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side1 + side2 + side3 + side4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print("Total trees is ",total_trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
before_noon_temp = 5
after_noon_temp = before_noon_temp - 10
evening_temp = after_noon_temp + 4
print("Evening temperature is ",evening_temp)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_quantity = 24
girls_quantity = boys_quantity / 2
total_children = (boys_quantity-1) + (girls_quantity-2)
print("Today is ",total_children)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1/2) + (book_2/2)
total_sum_for_3_books = book_1 + book_2 + book_3
print("Total sum for three books is ",total_sum_for_3_books)