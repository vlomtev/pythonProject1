# Задача 1
# name = input('Enter name:')
# age = input('Enter age:')
# weight = input('Enter weight:')
# print('Name:', name, 'Age:', age, 'Weight:', weight)
#
# Задача 2
# num = int(input('enter seconds:' ))
# hour = num // 3600
# minutes = (num // 60) % 60
# seconds = num % 60
# print('time is', f'{hour} : {minutes} : {seconds}')
#
# Задача 3
# n = int(input('enter number:'))
# n1 = n
# n2 = int(f'{n}{n}')
# n3 = int(f'{n}{n}{n}')
# result = n1 + n2 + n3
# print(result)
#
# Задача 4
# num = int(input('enter number:'))
# remains = num % 10
# num = num // 10
# while num > 0:
#     if num % 10 > remains:
#         remains = num % 10
#     num = num // 10
# print(remains)
#
# Задача 5
# revenue = int(input('enter revenue'))
# expenses = int(input('enter expenses'))
# profit = revenue - expenses
# if profit < 0:
#     print(f'убыток оставляет: {profit}')
# if profit > 0:
#     print(f'прибыль составляет: {profit}')
#
#  Задача 6
# revenue = int(input('enter revenue:'))
# expenses = int(input('enter expenses:'))
# profit = revenue - expenses
# if profit > 0:
#     profitability = (profit / revenue)*100
#     profitability = round(profitability, 2)
#     print(f'прибыль составляет {profit}')
#     print(f'рентабельность составляет {profitability}%')
#     employees = int(input('enter the number of employees:'))
#     profit_employee = profitability / employees
#     profit_employee = round(profit_employee, 2)
#     print(f'прибыль на одного сотрудника составляет {profit_employee}')
#
# elif profit < 0:
#     profit = profit*-1
#     print(f'убыток составил {profit}')
# else:
#     print(f'Результат деятельности фирмы {profit} денежных единиц')
#
# # Задача 7
# a = int(input('результат в первый день а = '))
# b = int(input('цель b = '))
# i = 0
# while a < b:
#     a = a + a/10
#     i = i + 1
# print(f'спортсмен достигнет результата на {i+1} день')