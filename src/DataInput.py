from tkinter import *


class DataInput(Frame):

    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf, **kw)
        self.entries = []
        self.generate_entry()

    def generate_entry(self):
        entry_value = StringVar()
        last_value = ""
        def add_data_callback(var, indx, mode):
            nonlocal last_value
            if entry_value.get() == "":
                entry_value.set(0)
                return
            try:
                float(entry_value.get().replace(",", "."))
            except ValueError:
                entry_value.set(last_value)
                return
            if "," in entry_value.get():
                entry_value.set(entry_value.get().replace(",", "."))
                last_value = entry_value.get()
                return
            last_value = entry_value.get()
            if self.entries[-1].get() != "":
                self.generate_entry()
            # For some reason, if we remove that, it doesn't seem to work anymore. Strange...
        entry_value.trace_add("write", add_data_callback)
        entry = Entry(self, width=50, font=("Arrial", 18), bg='#FFFFFF', fg='#4682B4',
                      textvariable=entry_value)
        entry.pack(expand=YES)
        self.entries.append(entry)

    def get_data(self):
        print([entry for entry in self.entries])
        [print(entry.get()) for entry in self.entries]
        return [float(entry.get()) for entry in self.entries if entry.get() != ""]
