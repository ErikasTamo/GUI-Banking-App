from tkinter import *

def updateBal(root, uid, pin):
	for i in root.winfo_children():
		if isinstance(i, Label):
			i.destroy()
	with open("files/logins.txt", 'r') as f:
		lines = f.readlines()
	for line in lines:
		acc = line.split(',')
		if acc[0] == uid and acc[1] == pin:
			bal = acc[3].strip("\n")
			Label(root, text=f"Hello {acc[2]}!", font=('arial', 20)).place(x=90, y=15)
			Label(root, text=f"Your Balance: {bal}$", font=('arial', 20)).place(x=45, y=60)

def deposit(root, uid, pin):
	def save():
		newBal = int(amount.get())
		with open("files/logins.txt", 'r') as f:
			lines = f.readlines()
		with open("files/logins.txt", 'w') as f:
			for line in lines:
				line = line.split(",")
				if line[0] != uid and line[1] != pin:
					f.write(f"{line[0]},{line[1]},{line[2]},{line[3]}\n")
				else:
					f.write(f"{line[0]},{line[1]},{line[2]},{int(line[3])+int(newBal)}")
		updateBal(root, uid, pin)

	main = Toplevel(root)
	main.geometry("400x200")
	main.resizable(False, False)
	Label(main, text="Deposit", font=('arial', 20)).place(x=150, y=10)

	Label(main, text="Amount", font=('arial', 20)).place(x=20, y=60)
	amount = Entry(main, font=('arial', 20))
	amount.place(x=130, y=65, height=35, width=150)
	Button(main, text="Deposit", font=('arial', 20), command=save).place(x=40, y=120, height=35, width=200)

def withdraw(root, uid, pin):
	def save():
		newBal = int(amount.get())
		with open("files/logins.txt", 'r') as f:
			lines = f.readlines()
		with open("files/logins.txt", 'w') as f:
			for line in lines:
				line = line.split(",")
				if line[0] != uid and line[1] != pin:
					f.write(f"{line[0]},{line[1]},{line[2]},{line[3]}\n")
				else:
					f.write(f"{line[0]},{line[1]},{line[2]},{int(line[3])-int(newBal)}")
		updateBal(root, uid, pin)

	main = Toplevel(root)
	main.geometry("400x200")
	main.resizable(False, False)
	Label(main, text="Withdaw", font=('arial', 20)).place(x=150, y=10)

	Label(main, text="Amount", font=('arial', 20)).place(x=20, y=60)
	amount = Entry(main, font=('arial', 20))
	amount.place(x=130, y=65, height=35, width=150)
	Button(main, text="Withdraw", font=('arial', 20), command=save).place(x=40, y=120, height=35, width=200)

def send(root, uid, pin):
	def save():
		reciverU = reciveUID.get()
		reciverB = amount.get()
		with open("files/logins.txt", 'r') as f:
			lines = f.readlines()
		with open("files/logins.txt", 'w') as f:
			for line in lines:
				line = line.split(',')
				if line[0] == uid:
					f.write(f"{line[0]},{line[1]},{line[2]},{int(line[3])-int(reciverB)}\n")
				elif line[0] == reciverU:
					f.write(f"{line[0]},{line[1]},{line[2]},{int(line[3])+int(reciverB)}\n")
				else:
					f.write(f"{line[0]},{line[1]},{line[2]},{line[3]}\n")
		updateBal(root, uid, pin)

	main = Toplevel(root)
	main.geometry("400x300")
	main.resizable(False, False)

	Label(main, text="Reciver", font=('arial', 20)).place(x=20, y=60)
	reciveUID = Entry(main, font=('arial', 20))
	reciveUID.place(x=130, y=65, height=35, width=150)

	Label(main, text="Amount", font=('arial', 20)).place(x=20, y=110)
	amount = Entry(main, font=('arial', 20))
	amount.place(x=130, y=115, height=35, width=150)
	Button(main, text="Send", font=('arial', 20), command=save).place(x=40, y=170, height=35, width=200)
