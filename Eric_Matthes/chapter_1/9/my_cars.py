#my_cars.py

#from car import Car, ElectricCar

#my_beetle = Car('volkswagen','beetle',2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = ElectricCar('tesla','roadster',2019)
#print(my_tesla.get_descriptive_name())

### или так

# import car - импортируем весь модуль и 
#- обращаемся к импортированному модуля, затем методу
# модуль.метод - car.get_descriptive_name() car.ElectricCar(....)

#import car

#my_beetle = car.Car('volkswagen','beetle',2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = car.ElectricCar('tesla','roadster',2019) - модуль.класс
#print(my_tesla.get_descriptive_name())

########--------------------- Импортирование модуля в модуль

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())
