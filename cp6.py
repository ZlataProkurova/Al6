array = input("Введите массив чисел через запятую: ").split(",")
print(array)
d = int(input ('Значение дельты: '))
m = int (array [0])
n = 0
for i in range (len(array)):
	array[i] = int(array[i])
	if int(array[i]) < m:
		m = array[i]
for i in range (len(array)):
	if array [i] - m == d:
		n += 1
print (n)		