name = 'qwe'
DB_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'
def main():
    print(name)
    print(DB_URL)
# main()

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(f'{self.brand} {self.model} is starting...')

car1 = Car('Skoda','Octavia','Blue')

# car1.start()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} is making sound'
    
class Dog(Animal):
    def speak(self):
        return f'{self.name} barks'
    
dog = Dog('Kyzya')
# print(dog.speak())

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def access_level(self):
        return f'User {self.name} has basic access'
    

class Developer(User):
    def __init__(self, name, role, programming_language):
        super().__init__(name, role)
        self.programming_language = programming_language

    def access_level(self):
        base_access = super().access_level()
        return f'{base_access} Can access development tools. Lang: {self.programming_language}'
    

user = User('John', 'Moder')
dev = Developer('Jane', 'Dev', 'Java')

# print(user.access_level())
# print(dev.access_level())

class Engineer:
   def manage(self):
       return "Developing software."

class Manager:
   def manage(self):
       return "Managing projects."

class Lead(Engineer, Manager):
   def lead_team(self):
       return "Leading the team."

team_lead = Lead()

# print(team_lead.manage())

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def _display_salary(self):
        return f'Зарплата: {self._salary}'
    
worker = Employee('Jack', 5000)
# print(worker._salary)


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def __display_balance(self):
        return f'Balance: {self.__balance}'
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def __apple_fee(self):
        self.__balance -= 10

    def get_balance(self):
        return self.__balance
    
account = BankAccount('Jim', 10000)
# print(account.holder)
# print(account.__balance)

class Person:
   def __init__(self, name, age):
       self.name = name
       self.__age = age

   def get_age(self):
       return self.__age

   def set_age(self, age):
       if age >= 0:
           self.__age = age
       else:
           raise ValueError("Age cannot be negative")

person = Person("Olha", 25)
print(person.get_age())

person.set_age(30)
print(person.get_age())

person.set_age(-5)