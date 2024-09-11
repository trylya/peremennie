my_dict={'Anna':1987, 'Masha':1984, 'Ivan':1989}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Max'))
my_dict.update({'Alla':1990, 'Alex':1993})
a= my_dict.pop ('Ivan')
print (a)
print(my_dict)

me_set={5,7,9,3,5,7,9,'ball', True, 'ball', True}
print(me_set)
me_set.add(2)
me_set.add(4)
me_set.discard(9)
print(me_set)