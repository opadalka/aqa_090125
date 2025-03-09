"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user, blocked).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = SiteUser("John Doe", "john.doe@example.com", "user")
user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: SiteUser: John Doe, mailbox: john.doe@example.com, access level: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""

class SiteUser():
    def __init__(self, name:str, email:str, access:str):
        self.__name = name
        self.__email = email
        self.__access = access
        self.__logcountincrease = 0

    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    @property
    def access(self):
        if isinstance(self, str):
            return self.__access
        else:
            raise TypeError
    @property
    def logcount(self):
        return self.__logcountincrease
    @property
    def get_class_name(self):
        return self.__class__.__name__

    @logcount.setter
    def logcount(self, log_increase:int):
        if not isinstance(log_increase, int):
            raise ValueError("log_increase must be int")
        else:
            self.__logcountincrease += log_increase

    def __eq__(self, other_obj):
        if isinstance(other_obj, SiteUser) and self.access == other_obj.access:
            return True
        else: 
            return False
        
    def __str__(self):
        return f"{self.get_class_name}: {self.name}, mailbox: {self.email}, access level: {self.access}"

if __name__ == "__main__":    
    user1 = SiteUser("John Doe", "john.doe@example.com", 1)
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "user")
    print(user1)
    if(user1==user2):
        user1.logcount = 1
        print(user1.logcount)
    else:
        print(user1.logcount)