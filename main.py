from tkinter import *
import string
import random
import apps


root = Tk()
root.title("Bank")
root.geometry("350x500")
root.resizable(False, False)

def main(uid, pin, name):
	for i in root.winfo_children():
		i.destroy()

	def updateBal(uid, pin):
		with open("files/logins.txt", 'r') as f:
			lines = f.readlines()
		for line in lines:
			acc = line.split(',')
			if acc[0] == uid and acc[1] == pin:
				bal = acc[3].strip("\n")
				Label(root, text=f"Your Balance: {bal}$", font=('arial', 20)).place(x=45, y=60)
	
	Label(root, text=f"Hello {name}!", font=('arial', 20)).place(x=90, y=15)
	updateBal(uid, pin)

	Button(root, text="Deposit", font=('arial', 20), command=lambda:apps.deposit(root, uid, pin)).place(x=20,y=130, height=40, width=150)
	Button(root, text="Withdraw", font=('arial', 20), command=lambda:apps.withdraw(root, uid, pin)).place(x=180,y=130, height=40, width=150)
	Button(root, text="Send", font=('arial', 20), command=lambda:apps.send(root, uid, pin)).place(x=20,y=185, height=40, width=150)
	Button(root, text="Log Out", font=('arial', 20), command=login).place(x=180,y=185, height=40, width=150)

def login():
	for i in root.winfo_children():
		i.destroy()
	def register():
		def addToFile():
			uid = "".join(random.sample(string.digits, 6))
			pin = "".join(random.sample(string.digits, 4))
			nam = name.get()
			bal = 500

			print(f"Name     : {nam}\nUser ID  : {uid}\nPIN Code : {pin}")

			Label(main, text=f"Name: {nam}", font=('arial', 20)).place(x=20,y=200)
			Label(main, text=f"User ID: {uid}", font=('arial', 20)).place(x=20,y=250)
			Label(main, text=f"PIN Code: {pin}", font=('arial', 20)).place(x=20,y=300)
			Label(main, text=f"Balance: {bal}$", font=('arial', 20)).place(x=20, y=350)

			with open("files/logins.txt", 'a') as f:
				f.write(f"{uid},{pin},{nam},{bal}\n")

		main = Toplevel(root)
		main.geometry("500x400")

		Label(main, text="Register", font=('arial', 20)).place(x=210, y=10)
		Label(main, text="Name", font=('arial', 20)).place(x=20, y=80)
		name = Entry(main, font=('arial', 20))
		name.place(x=130, y=85, width=180, height=35)
		Button(main, text="Register", font=('arial', 20), command=addToFile).place(x=20, y=140, height=35, width=180)

	def check_login():
		uid = uidE.get()
		pin = pinE.get()
		with open("files/logins.txt", 'r') as f:
			lines = f.readlines()
		for line in lines:
			acc = line.split(',')
			if acc[0] == uid and acc[1] == pin:
				main(acc[0], acc[1], acc[2])

	Label(root, text="Welcome Back", font=('arial', 20)).place(x=90, y=30)
	Label(root, text="Please Log In", font=('arial', 20)).place(x=100, y=60)

	Label(root, text="User ID", font=('arial', 18)).place(x=130, y=130)
	Label(root, text="PIN Code", font=('arial', 18)).place(x=120, y=210)

	uidE = Entry(root, font=('arial', 20), justify="center")
	uidE.place(x=85, y=165, height=30, width=180)
	pinE = Entry(root, font=('arial', 20), justify="center")
	pinE.place(x=85, y=245, height=30, width=180)

	Button(root, text="Log In", font=('arial', 20), command=check_login).place(x=80, y=290, height=35, width=190)
	Button(root, text="Register", font=('arial', 20), command=register).place(x=80, y=330, height=35, width=190)

if __name__ == "__main__":
	login()

root.mainloop()