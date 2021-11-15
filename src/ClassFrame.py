from tkinter import *
class ClassFrame(Frame):

    def __init__(self, containeur, color):
        super().__init__(containeur, bg=color)
        self.Title = None
        self.Subtitle = None
        self.Buttom = None
        self.Entry = None
        self.Canvas = None
        self.Bind = None

    def get_Frame(self):
        return self.Frame

    def get_Title(self):
        return self.Title

    def get_Subtitle(self):
        return self.Subtitle

    def get_Buttom(self):
        return self.Buttom

    def get_Entry(self):
        return self.Entry

    def get_Canvas(self):
        return self.Canvas

    def get_Bind(self):
        return self.Bind

    def add_Title(self, content, police, size, background, forground):
        self.Title = Label(self, text=content, font=(police, size), bg=background, fg=forground)
        self.Title.pack()

    def add_Subitle(self, content, police, size, background, forground):
        self.Subtitle = Label(self, text=content, font=(police, size), bg=background, fg=forground)
        self.Subtitle.pack()

    def add_Buttom(self, content, police, size, background, forground, cmd):
        self.Buttom = Button(self, text=content, font=(police, size), bg= background, fg=forground, command=cmd)
        self.Buttom.pack(pady=25)

    def add_Entry(self, police, size, background, forground):
        self.Entry = Entry(self, font=(police, size), bg= background, fg=forground)
        self.Entry.pack(expand=YES)

    def add_Bind(self, cmmd):
        self.Bind = bind(self, command=cmd)

    #def add_Canvas(self, content, police, size, background, forground):
      #  self.Title = tkinter.Canvas(self, text=content, front=(police, size), bg= background, fg=forground)