# class def

class Person:
    
    # Это функция контруктор
    def __init__(self, name, age):
        # Атрибуты класса
        self.name = name
        self.age = age
    
    # self - Это ссылка на OBJ или Экземпляр класса
    # Метод класса
    def introduce(self,):
        print(f"Hi i'm {self.name}")
        

# class OBJ - Экземпляр класса
# ardager = Person("Ardager", 25)

# ardager.introduce()

# print(type(ardager))
# print(type(123))
# print(type("Hello"))


# Родительский класс
class Hero:
    
    def __init__(self, name, hp, lvl):
        self.name_1 = name
        self.hp_1 = hp
        self.lvl_1 = lvl
        
    def action(self,):
        print(f"{self.name_1} делает базовое действие")

# naofume = Hero("NaoFume", 100, 3)

# Дочерний класс
class ShiledHero(Hero):
    pass # ---
    ... # ---


naofume = ShiledHero("NaoFume", 100, 3)

naofume.action()


# class -- CamelCase
# переменных, методов, функций -- snek_case

