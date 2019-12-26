from ozon_neuro import assert_auto

mili = 62.37
kilometri = 100


enter_lr = input("enter the learning_rate")
lr = float(enter_lr)

allow_error = input("enter the allow error of neuro")
accur = float(allow_error)


enter_epoch = input("enter epoch")
epoch = int(enter_epoch)



assert_auto(kilometri, mili, lr, accur, epoch)
