from tkinter import *
from ozon_neuro import assert_auto
from PIL import Image

class Assert_Ozon:
	def __init__(self, root, img_path, title,main_cond, second_cond, lr, accur, epoch, labelText, button_Text):
		self.root = root
		root.title = title

		self.label = Label(root, text=labelText)
		self.label.grid(row=0, column=1, columnspan=4)

		self.label = Label(root, text=main_cond)
		self.label.grid(row=1, column=1, columnspan = 1)

		self.main_cond = Entry()
		self.main_cond.grid(row=1, column=2, columnspan=2)


		self.label = Label(root, text=second_cond)
		self.label.grid(row=2, column=1, columnspan = 1)

		self.second_cond = Entry()
		self.second_cond.grid(row=2, column=2, columnspan=2)

		self.label = Label(root, text=lr)
		self.label.grid(row=3, column=1, columnspan = 1)

		self.lr = Entry()
		self.lr.grid(row=3, column=2, columnspan=2)

		self.label = Label(root, text=accur)
		self.label.grid(row=4, column=1, columnspan = 1)

		self.accur = Entry()
		self.accur.grid(row=4, column=2, columnspan=2)

		self.label = Label(root, text=epoch)
		self.label.grid(row=5, column=1, columnspan = 1)

		self.epoch = Entry()
		self.epoch.grid(row=5, column=2, columnspan=2)

		self.main_btn = Button(root, text= button_Text, command = self.assertation)
		self.main_btn.grid(row=6, column=1, columnspan=3)

		self.label_result = Label(root, text='')
		self.label_result.grid(row=7, column=1, columnspan=3)

		self.img_src = PhotoImage(file=(img_path))
		self.lab1 = Label(image=self.img_src, bd=0)
		self.lab1.image = self.img_src
		self.lab1.grid(row=8, column=1, columnspan=3)

	def assertation(self):
		result = assert_auto(int(self.main_cond.get()), int(self.second_cond.get()), float(self.lr.get()), float(self.accur.get()), int(self.epoch.get()))
		self.label_result["text"] = str(result)




root = Tk()

ozon_length = Assert_Ozon(root,"ozon.gif", "main_cond", "second_cond", "lr", "accur", "epoch",  "программа коэфицента длины", "Введите данные", "Вычислить")

root.geometry("400x400")
root.mainloop()




# прочитать про assert
# сделать в программе лого компании на заднем фоне ( и в классе!)
#пускай геометрия тоже задается в классе
# сделать лейблы к нашим entry





