import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text = "샌드위치 (5000원)").grid(column = 0, row = 0)
        Label(window, text="케이크 (20000원)").grid(column=0, row=1)
        self.sandwich = Entry(window, width = 15)
        self.sandwich.grid(column = 1, row = 0)
        self.cake = Entry(window, width = 15)
        self.cake.grid(column = 1, row = 1)
        btn_order = Button(window, text = "주문하기", command = self.send_order)
        btn_order.grid(column = 0, row = 3)

    def send_order(self):
        s = self.sandwich.get()
        c = self.cake.get()
        name = self.name
        order_text = "{}: 샌드위치 (5000원) {}개, 케이크 (20000원) {}개".format(name, s, c)
        try:
            int_s = int(s)
            int_c = int(c)
            if int_s <= 0 and int_c <= 0:
                order_text = None
            else:
                if int_s <= 0 or int_c <= 0:
                    if int_s <= 0:
                        order_text = "{}: 케이크 (20000원) {}개".format(name, c)
                    elif int_c <= 0:
                        order_text = "{}: 샌드위치 (5000원) {}개".format(name, s)
        except ValueError:

            if s.isdigit():
                order_text = order_text = "{}: 샌드위치 (5000원) {}개".format(name, s)
            elif c.isdigit():
                order_text = order_text = "{}: 케이크 (20000원) {}개".format(name, c)
            else:
                order_text = None
        if order_text != None:
            self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
