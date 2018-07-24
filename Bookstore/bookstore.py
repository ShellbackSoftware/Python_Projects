# Stores information about books:
# Title, Author, Year, ISBN
# User can View all entries, search, add, update, delete entries
# User can also close the program
from tkinter import *
from logic import Database

db = Database("books.db")

# View all entries
def view_command():
    results.delete(0, END)
    for row in db.view():
        results.insert(END,row)

# Fills in textboxes with information from highlighted row
def get_selected_row(event):
    global selected_tuple
    index=results.curselection()[0]
    selected_tuple=results.get(index)
    e_title.delete(0,END)
    e_title.insert(END,selected_tuple[1])
    e_author.delete(0,END)
    e_author.insert(END,selected_tuple[2])
    e_year.delete(0,END)
    e_year.insert(END,selected_tuple[3])
    e_isbn.delete(0,END)
    e_isbn.insert(END,selected_tuple[4])

# Search
def search_command():
    results.delete(0,END)
    for row in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        results.insert(END,row)

# Add an entry
def add_command():
    db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    results.delete(0,END)
    results.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

# Update an entry
def update_command():
    db.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

# Delete an entry
def delete_command():
    db.delete(selected_tuple[0])

window = Tk()
window.wm_title("Book Store")
# Book title
title_label = Label(window, text = 'Title')
title_label.grid(row = 0, column = 0)

title_text = StringVar()
e_title = Entry(window,textvariable = title_text)
e_title.grid(row = 0, column = 1)


# Author
author_label = Label(window, text = 'Author')
author_label.grid(row = 0, column = 2)

author_text = StringVar()
e_author = Entry(window,textvariable = author_text)
e_author.grid(row = 0, column = 3)

# Year published
year_label = Label(window, text = 'Year')
year_label.grid(row = 1, column = 0)

year_text = StringVar()
e_year = Entry(window,textvariable = year_text)
e_year.grid(row = 1, column = 1)

# Book ISBN
isbn_label = Label(window, text = 'ISBN')
isbn_label.grid(row = 1, column = 2)

isbn_text = StringVar()
e_isbn = Entry(window,textvariable = isbn_text)
e_isbn.grid(row = 1, column = 3)

# Results box
results = Listbox(window, height = 6, width = 35)
results.grid(row = 2,column = 0,rowspan = 6,columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2,column = 2,rowspan = 6)

results.configure(yscrollcommand = sb1.set)
sb1.configure(command = results.yview)

# Binds a method to the Listbox widget
results.bind('<<ListboxSelect>>', get_selected_row)

# View all button
view_button = Button(window, text = "View All", width = 12, command=view_command)
view_button.grid(row = 2, column = 3)

# Search for entry button
search_button = Button(window, text = "Search", width = 12, command=search_command)
search_button.grid(row = 3, column = 3)

# Add entry button
add_button = Button(window, text = "Add", width = 12, command=add_command)
add_button.grid(row = 4, column = 3)

# Update entry button
update_button = Button(window, text = "Update", width = 12, command=update_command)
update_button.grid(row = 5, column = 3)

# Delete entry button
delete_button = Button(window, text = "Delete", width = 12, command=delete_command)
delete_button.grid(row = 6, column = 3)

# Close program button
close_button = Button(window, text = "Close", width = 12, command=window.destroy)
close_button.grid(row = 7, column = 3)

window.mainloop()
