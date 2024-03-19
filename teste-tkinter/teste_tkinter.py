import tkinter as tk
from random import randint

def spawn_circle():
    global counter
    
    x = randint(0, 433)
    y = randint(0, 333)

    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")

    canvas.create_text(x, y, text=str(counter), fill="black")

    label_info = tk.Label(root, text=f"{counter}: ({x}, {y})")
    label_info.pack()

    counter += 1

def main() -> None:
    global root
    global canvas
    global counter

    counter = 0

    root = tk.Tk()
    root.title("Simple window")

    root.geometry("1024x768")

    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(root, text="Spawn circle", command=spawn_circle)
    button.pack(pady=10)

    label_viewport = tk.Label(root, text="The great viewport!")
    label_viewport.pack()

    canvas = tk.Canvas(frame, bg = "gray", width=433, height=333)
    canvas.pack(side=tk.LEFT, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas_frame = tk.Frame(canvas, bg="gray")
    canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))
    
    root.mainloop()

if __name__ == "__main__":
    main()
