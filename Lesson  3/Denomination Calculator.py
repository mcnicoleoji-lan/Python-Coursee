from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("data:image/jpeg;base64,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")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)

# -------------------------------
# Function for opening new/top window
# -------------------------------
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)

    lbl = Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey"
    )

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    # -------------------------------
    # Calculation Function
    # -------------------------------
    def calculator():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(
        top,
        text="Calculate",
        command=calculator,
        bg="brown",
        fg="white"
    )

    # -------------------------------
    # Placing Widgets
    # -------------------------------
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

# -------------------------------
# Start Main Loop
# -------------------------------
root.mainloop()
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if MsgBox == "ok":
        topwin()

button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg="brown",
    fg="white"
)
button1.place(x=260, y=360)

# -------------------------------
# Function for opening new/top window
# -------------------------------
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg="light grey")
    entry = Entry(top)

    lbl = Label(
        top,
        text="Here are number of notes for each denomination",
        bg="light grey"
    )

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    # -------------------------------
    # Calculation Function
    # -------------------------------
    def calculator():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(
        top,
        text="Calculate",
        command=calculator,
        bg="brown",
        fg="white"
    )

    # -------------------------------
    # Placing Widgets
    # -------------------------------
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

# -------------------------------
# Start Main Loop
# -------------------------------
root.mainloop()
