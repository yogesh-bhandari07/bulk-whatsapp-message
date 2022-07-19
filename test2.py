from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Whatsapp")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=1, rowspan=2,
            padx=5, sticky=E+W+S+N)
            
        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=1, rowspan=2,
            padx=5, sticky=E+W+S+N)

        nextBtn = Button(self, text="Next")
        nextBtn.grid(row=5, column=3)


def main():

    root = Tk()
    root.geometry("750x450+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()