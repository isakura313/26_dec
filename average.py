def transToArray(fn):
	fn += ".txt"
	file = open(fn , "r")
	file_content = file.read()
	list_num = file_content.split(", ")
	for i in range(len(list_num)):
		list_num[i] = int(list_num[i])
	return list_num

def bubble(arr):
	N = len(arr)
	for i in range(N - 1):
		for j in range(N - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		print(arr)

def average(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	return sum/len(arr)


print("Программа для расчета статистик!")
file_name = input("Введи имя файлика без расширения: ")


list_num = transToArray(file_name)
bubble(list_num)
result_aveg = average(list_num)

print("Среднее для этих данных:")
print(result_aveg)



file_result = open("result.txt", "w")
file_result.write("Среднее для этих данных:\n")
file_result.write(str(result_aveg))
file_result.close()



#напишите функцию  rowToArray,  которая у нас считывает строки с запятыми в массив
 # с помощью метода readline  сложить в одну строку сначала







