from tkinter import *
import backend


def sel_row(event):
    global s
    i = list1.curselection()[0]
    s = list1.get(i)
    e1.delete(0, END)
    e1.insert(END, s[1])
    e2.delete(0, END)
    e2.insert(END, s[2])
    e3.delete(0, END)
    e3.insert(END, s[3])
    e4.delete(0, END)
    e4.insert(END, s[4])


def delete():
    backend.delete(s[0])
    list1.delete(0, END)
    for x in backend.view():
        list1.insert(END, x)


def view():
    list1.delete(0, END)
    for x in backend.view():
        list1.insert(END, x)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def search():
    list1.delete(0, END)
    for x in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, x)


def add():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    for x in backend.view():
        list1.insert(END, x)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def update():
    backend.update(s[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    for x in backend.view():
        list1.insert(END, x)


w = Tk()

w.wm_title('BOOKSTORE')

l1 = Label(w, text='Title')
l1.grid(row=0, column=0)

l2 = Label(w, text='Author')
l2.grid(row=0, column=2)

l3 = Label(w, text='Year')
l3.grid(row=1, column=0)

l4 = Label(w, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(w, text=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(w, text=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(w, text=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(w, text=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(w, height=10, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(w)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', sel_row)

b1 = Button(w, text='View all', width=12, command=view)
b1.grid(row=2, column=3)

b2 = Button(w, text='Search Entry', width=12, command=search)
b2.grid(row=3, column=3)

b3 = Button(w, text='Add Entry', width=12, command=add)
b3.grid(row=4, column=3)

b4 = Button(w, text='Update', width=12, command=update)
b4.grid(row=5, column=3)

b5 = Button(w, text='Delete', width=12, command=delete)
b5.grid(row=6, column=3)

b6 = Button(w, text='Close', width=12, command=w.destroy)
b6.grid(row=7, column=3)


w.mainloop()
