import matplotlib.pyplot as plt

# y = A * x
A = 1.4
x_values = list(range(0, 10))
y_values = [x * A for x in x_values]

beatles = [3, 1]
gus = [1, 3]
# plt.style.use('seaborn-whitegrid')
plt.plot(beatles, gus, "ro")
plt.axis([0, 5, 0, 5])
plt.xlabel("width")
plt.ylabel("height")
plt.scatter(x_values, y_values, linewidths=3)
plt.show()

#  сделать линией наши разделительные точки
#  сделать жуков и гусениц разного цвета
# из tkinter, сделать программу,
# в которой будет 1 кнопка,
# при нажатии на которую программа закроется

# facultative
# попробуйте импортировать в linear наши библиотеку ozon_neuro
# и сделать так что бы она вычисляла коэфицент жуки и гусеницы