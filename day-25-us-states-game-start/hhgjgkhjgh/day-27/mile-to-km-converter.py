# from tkinter import *
#
# window = Tk()
# window.title("Mile to Km Converter")
# window.minsize(width=250, height=125)
# window.config(padx=30, pady=30)
#
# input = Entry(width=8)
# input.grid(column=1, row=0)
#
# miles_label = Label(text="Miles", font=("Arial", 15))
# miles_label.grid(column=2, row=0)
#
# label_2 = Label(text="is equal to", font=("Arial", 15))
# label_2.grid(column=0, row=1)
#
# label_3 = Label(text="0", font=("Arial", 15))
# label_3.grid(column=1, row=1)
#
# label_4 = Label(text="Km", font=("Arial", 15))
# label_4.grid(column=2, row=1)
#
# def button_clicked():
#     label_3["text"] = float(input.get()) * 1.609344
#
# button = Button(text="Calculate", font=("Arial", 15), command=button_clicked, width=8)
# button.grid(column=1, row=2)
#
# window.mainloop()

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=255, height=130)
window.config(padx=20, pady=20)

def button_clicked():
    label3["text"] = int(input.get()) * 1.60934

input = Entry(width=8)
input.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Arial", 15))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Arial", 15))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=("Arial", 15))
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=("Arial", 15))
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked, width=4)
button.grid(column=1, row=2)

window.mainloop()