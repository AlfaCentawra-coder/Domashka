#Список
mutable_list = ["Дикий сквонч", 13256, False, 3.14]
print (mutable_list)
mutable_list[2] = tuple([1, 3, 9, 7, 5])
print (mutable_list)

#Кортеж
immutable_var = [1, 3, 5, 9], True, "Print surprise"
print (immutable_var)
immutable_var[2] = 'Вабба-лабба-даб-даб!' #Кортеж не поддерживает обращение по элементам
print (immutable_var[0])