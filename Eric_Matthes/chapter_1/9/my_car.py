#my_car.py
from car import Car #открыть модуль car.py и импортировать класс Car 

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23 # присваиваем значение атрибуту
my_new_car.read_odometer()