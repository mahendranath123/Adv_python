from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()
    if username == '' and password == '':
        messagebox.showerror('Error..', 'Empty fields not allowed!')
    elif username == 'login' and password == '123':
        messagebox.showinfo('Login', 'Login Success!')

        root.destroy()
        top = Tk()
        top.configure(bg='white')
        top.state('zoomed')
        top.title('Success..')

        label4 = Label(top, text= 'Welcome!', font=('Areal',30))
        label4.place(x=500, y=300)
    else:
        messagebox.showerror('login','Incorrect user and/or password..')

root = Tk()
root.configure(bg='cyan4')
root.attributes('-fullscreen', True)
root.title("LOGIN CREDENTIALS")


global entry1
global entry2

label1 = Label(root, text='Login Page', bg='cyan4', fg='cyan', font=('Areal',20))
label1.place(x=500, y=20)

label2 = Label(root, text='User Name: ', font=('Areal',20), bg='cyan4', fg='white')
label2.place(x=310, y=190)

label3 = Label(root, text='Password: ', font=('Areal',20), bg='cyan4', fg='white')
label3.place(x=310, y=340)

entry1 = Entry(root, font=('Areal',15))
entry1.place(x=600, y=200)
entry2 = Entry(root, font=('Areal',15), show='*')
entry2.place(x=600, y=350)

button = Button(root, text='Login', bg='cyan3', font=('Areal',15), bd=5, command=login)
button.place(x=600, y=500)
root.mainloop()
