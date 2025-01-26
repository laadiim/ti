from typing import List
import window
import tkinter as tk
from edge import Edge


def load_images(directory: str) -> List[tk.PhotoImage]:
    images = []
    for i in range(11):
        images.append(tk.PhotoImage(file=f"{directory}/{i}.png"))
    return images


def redraw(root: tk.Tk, active_state: int, images: List[tk.PhotoImage]):
    pass


def main():
    images = load_images("states")
    acitve_state = 0
    root: tk.Tk = tk.Tk()
    image = tk.Label(root, images[active_state])
    root.mainloop()


if __name__ == "__main__":
    main()
