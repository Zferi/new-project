print('Медецинская анкета')
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))
if age <= 29 and weight <= 90:
    age = str(age)
    weight = str(weight)
    print(name + ' ' + surname + ',' + age + ' год,' + 'вес ' + weight + '-Состояние в норме')
elif age >= 30 and weight >= 90:
    age = str(age)
    weight = str(weight)
    print(name + ' ' + surname + ',' + age + ' год,' + 'вес ' + weight + '-Займись собой')
elif age >= 30 and weight <= 50:
    age = str(age)
    weight = str(weight)
    print(name + ' ' + surname + ',' + age + ' год,' + 'вес ' + weight + '-Пора к врачу')

