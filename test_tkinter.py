from tkinter import *

root = Tk()

root.title("Ozon Neuro")
root.geometry("300x400")

def toSquare():
	# здесь будет наша представление програмы
	result = int(entry_data.get())
	result = result ** 2
	res_square["text"] = str(result)
	res_square.pack()
	# получить текстовое значение label на запись

def toCoob():
	# здесь будет наша представление програмы
	result = int(entry_data.get())
	result = result ** 3
	res_coob["text"] = str(result)
	res_coob.pack()


entry_data = Entry()
entry_data.pack()

label_square = Label(root, text="результат квадрата")
label_square.pack()

res_square = Label(root, text="")
res_square.pack()

label_coob = Label(root, text="результат  куба")
label_coob.pack()

res_coob = Label(root, text="")
res_coob.pack()

square_btn = Button(root, text="square", command = toSquare, font="Arial")
square_btn.pack()

coob_btn = Button(root, bg="red", text="cube", command = toCoob)
coob_btn.pack()
root.configure(background='black')
root.mainloop()


