import tkinter as tk
from tkinter import messagebox
from functools import partial

distance_Val = "Kilometers"

def store_distance(set_distance):
    global distance_Val
    distance_Val = set_distance

def call_convert(rlabel1, inputn):
    value = inputn.get()

    if distance_Val == "Miles":
        kilometers = float(value) * 1.60934
        rlabel1.config(text="%.1f Kilometers" % kilometers)
        messagebox.showinfo("Distance Converter", "Successfully converted to Kilometers")
 
 
    elif distance_Val == "Kilometers":
        miles = float(value) / 1.609
        rlabel1.config(text="%.1f Miles" % miles)
        messagebox.showinfo("Distance Converter", "Successfully converted to Miles")

    return


#window
root = tk.Tk()
 
root.geometry('300x150+600+200')
 
root.title('Distance Converter')
 

root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(1, weight = 1)
 
inputNumber = tk.StringVar()
var = tk.StringVar()
 

input_label = tk.Label(root, text ="Enter distance")
input_entry = tk.Entry(root, textvariable = inputNumber)
input_label.grid(row = 1)
input_entry.grid(row = 1, column = 1)
result_label = tk.Label(root)
result_label.grid(row = 3, columnspan = 4)
 

dropDownList = ["Miles", "Kilometers"]
drop_down = tk.OptionMenu(root, var, *dropDownList,
                          command = store_distance)
var.set(dropDownList[0])
drop_down.grid(row = 1, column = 2)
 

call_convert = partial(call_convert, result_label,
                       inputNumber)
result_button = tk.Button(root, text ="Convert",
                          command = call_convert)
result_button.grid(row = 2, columnspan = 2)
 
root.mainloop()