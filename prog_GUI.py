




# import tkinter
# top = tkinter.Tk()

# # Code to add widgets will go here...
# top.mainloop()

# import tkinter as tk
# class App(tk.Tk):
#    def __init__(self):
#       super().__init__()

# app = App()
# app.mainloop()

# from tkinter import *
# from tkinter import messagebox
# top = Tk()
# top.geometry("500x250")
# def hello_world():
#    msg=messagebox.showinfo( "My Title", "My Message")
# B = Button(top, text ="Hello", command = hello_world)
# B.place(x=20,y=150)
# top.mainloop()

# from tkinter import *
# root = Tk()
# var = StringVar()
# label = Label( root, textvariable=var, relief=RAISED )
# var.set("I am using Python GUI!")
# label.pack()
# root.mainloop()

from tkinter import *
root = Tk()
text = Text(root)
	# insert(index [,string]...)
	# This method inserts strings at the specified index location
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()
	# tag_add(tagname, startindex[,endindex] ...)
	# This method tags either the position defined by startindex, or a range delimited by the positions startindex and endindex.
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
	# tag_config
	# You can use this method to configure the tag properties, which include, justify(center, left, or right), tabs(this property has the same functionality of the Text widget tabs's property), and underline(used to underline the tagged text).
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="white")
root.mainloop()

