import tkinter as tk
from PIL import Image, ImageTk
import random
import threading


image_path = "nya face.jpg"  # doesnt work


def create_window(show_image=False):
    root = tk.Tk()
    root.title("nya nya")
    root.geometry("200x100")
    root.overrideredirect(True)

    
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    color_index = 0

    label = tk.Label(root, text="nya nya", font=("Arial", 20, "bold"))
    label.pack(expand=True)

    
    if show_image:
        img = Image.open(image_path)
        img = img.resize((150, 75))  
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(root, image=photo)
        image_label.photo = photo
        image_label.pack()

    
    def update_color():
        nonlocal color_index
        color_index = (color_index + 1) % len(colors)
        label.config(fg=colors[color_index])
        label.after(100, update_color)

    update_color()

    
    x, y = random.randint(100, 500), random.randint(100, 300)
    dx, dy = 3, 3

    
    def bounce():
        nonlocal x, y, dx, dy
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        
        x += dx
        y += dy

        
        if x <= 0 or x + 200 >= screen_width:
            dx = -dx
        if y <= 0 or y + 100 >= screen_height:
            dy = -dy

        root.geometry(f"200x100+{x}+{y}")
        root.after(30, bounce)

    bounce()

    
    def on_close():
        root.destroy()
        create_window()
        create_window()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


def spawn_with_image():
    while True:
        threading.Timer(10, lambda: create_window(show_image=True)).start()


threading.Thread(target=create_window).start()
threading.Thread(target=spawn_with_image).start()
