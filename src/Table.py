from tkinter import *
class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

class Scrollbar_:
    def __init__(self):
        self.window = Tk()

        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, yscrollcommand=self.scrollbar.set)
        for i in range(100):
            self.listbox.insert("end", str(i))
        self.listbox.pack(side="left", fill="both")

        self.scrollbar.config(command=self.listbox.yview)