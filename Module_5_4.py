class House:
    houses_history = list()
    def __new__(cls, *args,**kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название:{self.name},кол-во этажей:{self.number_of_floors}'
    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')
        global houses_history
        House.houses_history.remove(self.name)



house1 = House('ЖК Эльбрус',30)
print(House.houses_history)
house2 = House('ЖК Нью - Васюки',40)
print(House.houses_history)
house3 = House('ЖК Гадюкино',2)
print(House.houses_history)
del house3
print(House.houses_history)
del house1
print(House.houses_history)