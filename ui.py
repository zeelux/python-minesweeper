import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Mine Sweeper")

# greeting = tk.Label(text="Hello, Tkinter")
# greeting.pack()

# button = tk.Button(
#     text=" ",
#     width=20,
#     height=20,
#     # bg="blue",
#     # fg="yellow",
# )
# button.pack()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.FLAT,
            borderwidth=0,
            width=20,
            height=20
        )
        frame.grid(row=i, column=j)
        btn = tk.Button(
          # command=lambda: print(f"Button {i}.{j} clicked!"),
          master=frame,
          width=20,
          height=20,
          relief=tk.RAISED,
          text=f" "
        )
        btn.pack()

window.mainloop()
