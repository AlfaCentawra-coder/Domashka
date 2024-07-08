#Библиотека
my_dict = {'Lera': 1974, "Pasha": 1981, "Lika": 2006, "Tolya": 2000, "Max": 2015}
print (my_dict)

print ('Dict - ', my_dict['Pasha'])
print ('Exiting value - ', my_dict.get('Anton'))

my_dict.update({'Valera': 1999, 'Dima': 2004, 'Vanya': 2022})
print (my_dict)

a = my_dict.pop('Lera', 'Lika')
print (my_dict)
print (a)

#Множество
my_set = {1, True, 1, 3, False, 6, 6.784, 5, "String", 7, 'Float'}
print(my_set)

my_set.update({'Parta', 745})
print(my_set)

my_set.remove(False)
print(my_set)