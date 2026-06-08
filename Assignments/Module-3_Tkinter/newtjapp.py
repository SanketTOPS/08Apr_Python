import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.geometry("400x500")
tk.title("NewApp")
tk.config(bg="lightblue")


"""l1=tkinter.Label(text="Firstname")
l1.pack()

l2=tkinter.Label(text="Lastname")
l2.pack()"""

"""l1=tkinter.Label(text="Firstname",bg="lightblue",fg="red",font='Constantia 15 bold')
l1.place(x=0,y=0)

l2=tkinter.Label(text="Lastname",bg="lightblue",fg="red",font='Constantia 15 bold')
l2.place(x=0,y=30)"""

l1=tkinter.Label(text="Firstname",bg="lightblue",fg="red",font='Constantia 15 bold')
l1.grid(row=0,column=0,sticky='w')

l2=tkinter.Label(text="Lastname",bg="lightblue",fg="red",font='Constantia 15 bold')
l2.grid(row=1,column=0,sticky='w')

t1=tkinter.Entry()
t1.grid(row=0,column=1,sticky='w')

t2=tkinter.Entry()
t2.grid(row=1,column=1,sticky='w')

m=tkinter.Radiobutton(value=0,text="Male",bg="lightblue",fg="red",font='Constantia 15 bold')
f=tkinter.Radiobutton(value=1,text="Female",bg="lightblue",fg="red",font='Constantia 15 bold')
m.grid(row=2,column=0,sticky='w')
f.grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Gujarati",bg="lightblue",fg="red",font='Constantia 15 bold').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi",bg="lightblue",fg="red",font='Constantia 15 bold').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English",bg="lightblue",fg="red",font='Constantia 15 bold').grid(row=5,column=0,sticky='w')

city=['Rajkot','Ahmedabad','Surat','Baroda','Gandhinagar']
ttk.Combobox(values=city).grid(row=6,column=0,sticky="w")

def btnClick():
    #print("Button Click!")
    #messagebox.showerror("Error","Something wrong...")
    #messagebox.showinfo("Success","Signup Successfully!")
    #messagebox.showwarning("Warning","Your C drive is full...")
    #t1.get()
    #t2.get()
    print("Firstname:",t1.get())
    print("Lastname:",t2.get())
    
    
tkinter.Button(text="Submit",fg="red",font='Constantia 15 bold',command=btnClick).place(x=160,y=250)
tk.mainloop()