import tkinter as tk
from tkinter import messagebox

values = [1, 3, 2, 4, 5]


def start():
    window = tk.Tk()
    global list_of_values
    greeting = tk.Label(text="Greetings, traveler")
    greeting.pack()
    command_button_clear = tk.Button(text="Click me if you want to clear numbers list", width=50, height=5, 
                                     bg="purple", command=clear_values)
    command_button_clear.pack()
    command_button_sort = tk.Button(text="Click me if you want to sort numbers list", width=50, height=5, 
                                    bg="purple", command=sort_values)
    command_button_sort.pack()
    command_button_add_value = tk.Button(text="Click me if you want to add new value", width=50, height=5, 
                                         bg="purple", command=add_value_to_list)
    command_button_add_value.pack()

    list_of_values = tk.Label(text=str(values))
    list_of_values.pack()
    window.mainloop()


def clear_values():
    values.clear()
    tk.messagebox.showinfo("Cleared!", str(values))
    update_list_of_values()


def sort_values():
    values.sort()
    tk.messagebox.showinfo("Sorted!", str(values))
    update_list_of_values()


def update_list_of_values():
    list_of_values.config(text=str(values))


def add_value_to_list():
    values.append(int(input("Enter a number to add: ")))
    update_list_of_values()


start()
