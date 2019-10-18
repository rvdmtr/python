#making_pizzas.py

#import pizza - импортировать все функции из модуля

#import pizza as p #- задать псевдоним импортированному модулю

#from pizza import make_pizza as mp - импортировать конкретную функцию
# и задать ей псевдоним, если имя нативной функции слишком длинное или 
# или совпадает с именем другой функции в программе

from pizza import make_pizza # импортировать конкретную функцию из модуля


#pizza.make_pizza(15,'mushrooms','cheese','lira') # модуль.функция
#pizza.make_pizza(18,'peperoni')

#mp(15,'mushrooms','cheese','lira') # импортированной функции задано имя

make_pizza(15,'mushrooms','cheese','lira')#конкретно импортированная функция


#p.make_pizza(15,'mushrooms','cheese','lira')#обращение к псевдониму модуля
