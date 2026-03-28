import tkinter as tk
from tkinter import messagebox
import intruder_detection


# EXIT SYSTEM
def exit_system(event=None):
    root.destroy()


# LOGIN FUNCTION
def login():

    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Access Granted")
        open_dashboard()
    else:
        messagebox.showerror("Login", "Invalid Credentials")


# DASHBOARD
def open_dashboard():

    root.destroy()

    dash = tk.Tk()
    dash.title("AI Threat Detection Dashboard")
    dash.attributes("-fullscreen", True)
    dash.configure(bg="#0a1a40")

    dash.bind("<Shift-Q>", lambda e: dash.destroy())

    frame = tk.Frame(dash, bg="#0a1a40")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        frame,
        text="AI THREAT DETECTION SYSTEM",
        font=("Arial", 32, "bold"),
        fg="white",
        bg="#0a1a40"
    ).pack(pady=30)

    tk.Button(
        frame,
        text="START CAMERA",
        font=("Arial", 18),
        width=20,
        command=intruder_detection.start_camera
    ).pack(pady=20)

    tk.Button(
        frame,
        text="EXIT SYSTEM",
        font=("Arial", 18),
        width=20,
        command=dash.destroy
    ).pack(pady=20)

    dash.mainloop()


# LOGIN WINDOW
root = tk.Tk()
root.title("AI Security System")

root.attributes("-fullscreen", True)

root.bind("<Shift-Q>", exit_system)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

canvas = tk.Canvas(
    root,
    width=width,
    height=height,
    bg="#0a1a40",
    highlightthickness=0
)

canvas.pack()

login_frame = tk.Frame(root, bg="#0a1a40")
login_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(
    login_frame,
    text="AI SECURITY SYSTEM",
    font=("Arial", 30, "bold"),
    fg="white",
    bg="#0a1a40"
).pack(pady=20)

tk.Label(login_frame, text="Username", font=("Arial", 14), fg="white", bg="#0a1a40").pack()
entry_user = tk.Entry(login_frame, font=("Arial", 14))
entry_user.pack(pady=5)

tk.Label(login_frame, text="Password", font=("Arial", 14), fg="white", bg="#0a1a40").pack()
entry_pass = tk.Entry(login_frame, show="*", font=("Arial", 14))
entry_pass.pack(pady=5)

tk.Button(
    login_frame,
    text="LOGIN",
    font=("Arial", 14),
    width=12,
    command=login
).pack(pady=20)

root.mainloop()