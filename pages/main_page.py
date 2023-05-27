from tkinter import *


class MainPage:
    name = "Main Page"
    counter = 0

    def __init__(self):
        window = Tk()
        window.geometry("400x280")  # It's like width x height
        window.title("Python GUI")  # sets the window title
        window.resizable(False, False)
        photo_image = PhotoImage(file=r"C:\Users\Abdullah\PycharmProjects\python_win_ui\assets\favico.png")
        window.iconphoto(True, photo_image)
        label = Label(window, text="Gracious god", font=('Arial', 40, 'bold'), fg="#f55344",bg="#000000")
        label.pack(side="top", pady=10)
        # self.print_my_name()
        self.smoke_the_file()
        window.mainloop()  # This will place the window on screen or simply show the window.

    def print_my_name(self):
        print('My name: ' + self.name)
        for i in range(0, 5):
            self.increment_counter()
            print('Count is: ' + str(self.counter))

    def smoke_the_file(self):
        print(f'The name is: {self.print_my_name()}')
    def increment_counter(self):
        self.counter += 1

    def decrement_counter(self):
        self.counter -= 1
