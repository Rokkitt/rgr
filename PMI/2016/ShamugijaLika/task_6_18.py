import random
print("Программа загадывает имя одной из трех официальных жен Зевса, а игрок должен его угадать.")
name = input("\n\nНазовите одно из имен оффицильных жен Зевса: ")
number = random.randint(1, 3)
if number == 1 :
 realname = 'Метида'
 realname = 'Метида'
elif number == 2 :
 realname = 'Фемида'
 realname = 'Фемида'
else :
 realname = 'Гера'
 realname = 'Фемида'
if name == realname :
 print("Верно! Это", realname,"\nКак вам удалось угадать?")
else :
 print("Ох, нет, ты ошибся.")

input("\n\nPress Enter")
