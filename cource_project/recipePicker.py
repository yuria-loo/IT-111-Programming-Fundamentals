import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet

bg_color = "#C27A7A"

pyglet.font.add_file("fonts/Ubuntu-Bold.ttf")
pyglet.font.add_file("fonts/Shanti-Regular.ttf")

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def fetch__db():
    connection = sqlite3.connect("data/JapaneseMealRecipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    idx = random.randint(0, len(all_tables)-1)

    # fetch ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records

def pre_process(table_name, table_records):
    title = table_name[:-6]
    title = "".join([char if char.islower() else " " + char for char in title])

    # ingredients
    ingredients = []
    for item in table_records:
        name = item[1]
        qty = item[2]
        unit = item[3]
        ingredients.append(qty + " " + unit + " of " + name)

    return title, ingredients


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    # logo widgets
    logo_img = ImageTk.PhotoImage(file="assets/Japanese1.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    # Label Widget
    tk.Label(frame1, 
            text="ready for your random recipe?",
            bg=bg_color,
            fg="white",
            font=("Shanti", 14)
            ).pack()

    # Button Widget
    tk.Button(
        frame1,
        text="Next",
        font=("Ubuntu", 20),
        bg="#824141",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()

    table_name, table_records = fetch__db()
    title, ingredients = pre_process(table_name, table_records)

    # logo widgets
    logo_img = ImageTk.PhotoImage(file="assets/Japanese2.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    # Label Widget for a title
    tk.Label(frame2, 
            text=title,
            bg=bg_color,
            fg="white",
            font=("TkHeadingFont", 20)
            ).pack(pady=25)
    
    for item in ingredients:
        # Label Widget for each ingredient
        tk.Label(
            frame2, 
            text=item,
            bg="#824141",
            fg="white",
            font=("Shanti", 12)
            ).pack(fill="both")
    

    # Button Widget
    tk.Button(
        frame2,
        text="Back",
        font=("Ubuntu", 18),
        bg="#824141",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1()
        ).pack(pady=20)    
  

# initiallize app
root = tk.Tk()
# Title
root.title("Recipe Picker")
# Disply in center
root.eval("tk::PlaceWindow . center")


# Create a frame Widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)
# Grid Method
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()


# run app
root.mainloop()