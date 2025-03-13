"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

    сторона_а (довжина сторони a).
    кут_а (кут між сторонами a і b).
    кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:

    Значення сторони сторона_а повинно бути більше 0.
    Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення
    кут_б обчислюється автоматично.
    Для встановлення значень атрибутів використовуйте метод __setattr__.
"""

class Romb():
    def __setattr__(self, name, value): 
        if name == 'side_a':
           if value > 0:
                super().__setattr__(name, value)
           else:
                super().__setattr__(name, value)
                print("Side A cannot be 0")
        if name == 'angle_a':
            if value == 90 and self.side_a > 0:
                super().__setattr__(name, value)
                print(f"This is romb, because angle a is {value} and angle b is {180-value} and side a is {self.side_a}")
            else:
                super().__setattr__(name, value)
                print(f"This is NOT romb, because angle a is {value} and/or side a is {self.side_a}")

romb_instance = Romb()
setattr(romb_instance, 'side_a', 10)
setattr(romb_instance, 'angle_a', 90)