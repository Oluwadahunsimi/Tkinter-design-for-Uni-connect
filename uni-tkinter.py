from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel, Label, Entry, Frame, Checkbutton, BooleanVar
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\olalere\Desktop\Desktop\Softwares\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_stroked_text(canvas, x, y, text, font, text_color, stroke_color, stroke_width):
    for dx in [-stroke_width, 0, stroke_width]:
        for dy in [-stroke_width, 0, stroke_width]:
            if dx != 0 or dy != 0:
                canvas.create_text(x + dx, y + dy, anchor="nw", text=text, font=font, fill=stroke_color)
    canvas.create_text(x, y, anchor="nw", text=text, font=font, fill=text_color)

def open_authentication_page():
    root = Toplevel(window)
    root.title('Login')
    root.geometry("925x500+300+200")
    root.configure(bg="#fff")
    root.resizable(False, False)

    def signin():
        # Add signin function code here
        pass

    def signup_command():
        window = Toplevel(root)
        window.title("Sign Up")
        window.geometry("925x500+300+200")
        window.configure(bg='#fff')
        window.resizable(False, False)

        # Add signup window UI components here
        pass

    def on_enter(e):
        if user.get() == "Username":
            user.delete(0, END)

    def on_leave(e):
        if user.get() == "":
            user.insert(0, "Username")

    def on_enter_password(e):
        if code.get() == "Password":
            code.delete(0, END)
            code.config(fg="black")
            code.config(show="•")

    def on_leave_password(e):
        if code.get() == "":
            code.insert(0, "Password")
            code.config(fg="black")
            code.config(show="")

    def toggle_password_visibility():
        if show_password.get():
            code.config(show="")
        else:
            code.config(show="•" * len(code.get()))

    image = Image.open("loginnn.png")
    img = ImageTk.PhotoImage(image)
    image_label = Label(root, image=img, bg="white")
    image_label.place(x=50, y=50)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    translator = Label(frame, text="   Uni-Connect", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading = Label(frame, text="  Sign In", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 17, "bold"))
    translator.place(x=40, y=1)
    heading.place(x=105, y=50)

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=95)
    user.insert(0, "Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=120)

    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=160)
    code.insert(0, "Password")
    code.bind('<FocusIn>', on_enter_password)
    code.bind('<FocusOut>', on_leave_password)

    show_password = BooleanVar()
    show_password_checkbox = Checkbutton(frame, text="Show Password", variable=show_password, bg="white", command=toggle_password_visibility)
    show_password_checkbox.place(x=200, y=163)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=187)

    Button(frame, width=39, pady=7, text="Sign In", bg="#57a1f8", border=0, command=signin).place(x=35, y=240)

    label = Label(frame, text="      Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 10))
    label.place(x=30, y=300)

    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor="hand2", fg="#57a1f8", command=signup_command)
    sign_up.place(x=200, y=300)

    root.mainloop()

window = Tk()
window.geometry("1366x768")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_authentication_page,
    relief="flat"
)
button_1.place(x=1150, y=30, width=140, height=40)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(1200, 200, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(1280, 350, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(100, 230, image=image_image_3)

canvas.create_text(
    90,
    385,
    anchor="nw",
    text="Welcome to UniConnect, your all-in-one academic support system.  \nBook appointments, manage results, and track attendance all in one \nplace.",
    fill="#000000",
    font=("MicrosoftYaHeiUI", 16),
    width=800
)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(60, 150, image=image_image_4)

create_stroked_text(
    canvas,
    90,
    270,
    text="Streamline Your Academic \nExperience with",
    font=("MicrosoftYaHeiUI Bold", 30),
    text_color="#000000",
    stroke_color="#000000",
    stroke_width=1
)

create_stroked_text(
    canvas,
    375,
    318,
    text="UniConnect",
    font=("MicrosoftYaHeiUI Bold", 30),
    text_color="#105ada",
    stroke_color="#105ada",
    stroke_width=1
)

original_image_5 = Image.open(relative_to_assets("image_5.png"))
resized_image_5 = original_image_5.resize((450, 450), Image.Resampling.LANCZOS)
image_image_5 = ImageTk.PhotoImage(resized_image_5)
image_5 = canvas.create_image(950, 400, image=image_image_5)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(x=930, y=30, width=80, height=40)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=840, y=30, width=68, height=40)

canvas.create_text(
    120,
    225,
    anchor="nw",
    text="Connecting Students with Success",
    fill="#32CD32",
    font=("MicrosoftYaHeiUI Bold", 16)
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(x=610, y=30, width=69, height=40)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(x=90, y=500, width=180, height=60)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(x=720, y=30, width=85, height=40)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(160, 60, image=image_image_6)

window.resizable(False, False)
window.mainloop()
