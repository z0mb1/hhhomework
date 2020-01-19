class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.brand.capitalize()} {self.model.capitalize()}'


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, *cars):
        self.cars = list(cars)

    def __str__(self):
        return ', '.join((str(car) for car in self.cars))

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.cars):
            return self.cars[self.index]
        else:
            raise StopIteration

    def __add__(self, car):
        self.cars.append(car)

    def __delete__(self, index):
        del self.cars[index]


if __name__ == '__main__':
    car1 = Car('opel', 'zafira')
    car2 = Car('opel', 'astra')
    car3 = Car('ford', 'focus')
    car4 = Car('honda', 'jazz')
    my_garage = Garage(car1, car2, car3)
    print('\n---iter method works')
    for index, car in enumerate(my_garage):
        print(index, car)
    for index, car in enumerate(my_garage):
        print(index, car)
    print('\n---add method works')
    my_garage + car4
    print(my_garage)
    print('\n---delete method works')
    del my_garage.cars[2]
    print(my_garage)

