#задача на сортировку Дан массив из 10 эллементов . отсортировать массив с 1 по 5 по возрастанию. а с 6 по 10 по убыванию


#my_list = [5, 4, 6, 7, 4, 8, 3, 2, 9, 1]
#print(my_list)
#print(my_list[0])
#print(my_list[1])
#num = 0
#
#for i in range(0, 9):
#    for j in range(i + 1, 10):
#        if my_list[i] > my_list[j]:
#            num = my_list[i]
#            my_list[i], my_list[j] = my_list[j], my_list[i]
#            my_list[1] = my_list[0]
#            my_list[j] = num
#print(my_list)

###############супертурбокалькулятор
import time

start_time = time.time() #стартатовая точка в времени
op_data = [] #массив это переменнная которая может принемать в себе несколько

test = "test"
while True:
     print("Это приложение супертурбокалькулятор")
     start = input("Если хотите работать с приложение колькулятор нажмите:start\n"
                   "Если вы хотете посмотреть историю вашей операциии нажмите:history")
     if start =="start":
         try:
             calculate = input('Калькулятор:\n "+"\n "-"\n "*"\n "/"\n" Введите нужную операцию:')

             if calculate not in ('+', '-', '*', '/'):
                 raise Exception("вы ввели неккоректную операцию из списка")

             a = float(input('ВВедите первое число:'))
             b = float(input('ВВедите второе число:'))



             if calculate =='+':
                 print(f'Резултат вычесления: {a + b}')
                 op_data.append(f"{a} + {b} = {a + b}")
             elif calculate =='-':
                 print(f'Резултат вычесления: {a - b}')
                 op_data.append(f"{a} - {b} = {a - b}")
             elif calculate == '*':
                 print(f'Резултат вычесления: {a * b}')
                 op_data.append(f"{a} * {b} = {a * b}")
             elif calculate =='/':
                 print(f'Резултат вычесления: {a / b}')
                 op_data.append(f"{a} / {b} = {a / b}")
         except ZeroDivisionError:
             print("вы не можете делить на 0")
         except ValueError:
             print("вы должны ввести цифры")
         except Exception as peremennya:
             print(peremennya)
         except:
             print("неизвестная ошибка ")
         # finally:
         #     print("Калькулятор сломался")
     elif start =="history":
         for i in op_data:
             print(i)
     else:
         end_time = time.time() #конечная точка
         print(f"приложение время работы приложения: {round(end_time - start_time, 2)}")
         print("приложение супертурбокалькулятор завершил работу!")
         break