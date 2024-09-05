from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast

# Function to handle the login process
def signin():
    file = open("datasheet.txt", "r")
    d = file.read()
    r = ast.literal_eval(d)
    file.close()
    
    username = user.get()
    password = code.get()
    
    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        Label(screen, text="Hello world", bg="#fff", font=("calibri(Body)", 50, 'bold')).pack(expand=True)
        
        screen.mainloop()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def signup():
    username = signup_user.get()
    password = signup_code.get()
    confirm_password = confirm_code.get()
    if password == confirm_password:
        try:
            file = open('datasheet.txt', "r+")
            d = file.read()
            r = ast.literal_eval(d)
            
            dict2 = {username: password}
            r.update(dict2)
            file.seek(0)
            file.truncate(0)
            file.write(str(r))
            file.close()
            
            messagebox.showinfo("Signup", "Successfully signed up")
        except:
            file = open("datasheet.txt", "w")
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', "Both passwords should match")
        print (r.keys())
        print(r.values())
def signup_command():
    window = Toplevel(root)
    window.title("Sign Up")
    window.geometry("925x500+300+200")
    window.configure(bg='#fff')
    window.resizable(False, False)

    img = PhotoImage(file='loginnn.png')
    Label(window, image=img, border=0, bg="white").place(x=50, y=90)
    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign Up", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI light', 23))
    heading.place(x=100, y=5)
    
    def on_enter_user(e):
        signup_user.delete(0, "end")
    
    def on_leave_user(e):
        if signup_user.get() == "":
            signup_user.insert(0, "Username")
    
    global signup_user  # Make it global to be accessed in the signup function
    signup_user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
    signup_user.place(x=30, y=80)
    signup_user.insert(0, 'Username')
    signup_user.bind("<FocusIn>", on_enter_user)
    signup_user.bind("<FocusOut>", on_leave_user)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)
    
    def on_enter_password(e):
        signup_code.delete(0, "end")
        
    
    def on_leave_password(e):
        if signup_code.get() == "":
            signup_code.insert(0, "Password")
    
    global signup_code  # Make it global to be accessed in the signup function
    signup_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
    signup_code.place(x=30, y=150)
    signup_code.insert(0, 'Password')
    signup_code.bind("<FocusIn>", on_enter_password)
    signup_code.bind("<FocusOut>", on_leave_password)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)
    
    def on_enter_confirm(e):
        confirm_code.delete(0, "end")
    
    def on_leave_confirm(e):
        if confirm_code.get() == "":
            confirm_code.insert(0, "Confirm Password")
    
    global confirm_code  # Make it global to be accessed in the signup function
    confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>", on_enter_confirm)
    confirm_code.bind("<FocusOut>", on_leave_confirm)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)
    
    Button(frame, width=39, pady=7, text='Sign up', bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text="  I have an account--", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
    label.place(x=90, y=340)

    signin_button = Button(frame, width=6, text="Sign in", border=0, background="white", cursor="hand2", fg="#57a1f8", command=signin)
    signin_button.place(x=200, y=340)
    
    window.mainloop()

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

root = Tk()
root.title('Login')
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

image = Image.open("loginnn.png")
img = ImageTk.PhotoImage(image)
image_label = Label(root, image=img, bg="white")
image_label.place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

translator = Label(frame, text="   Uni-Connect", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading = Label(frame, text="  Sign In", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 17, "bold"))
translator.place(x=40, y=1)  # Adjusted y-coordinate
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
sign_up.place(x=200, y=300)  # Adjusted x and y coordinates to align with the text

root.mainloop()
