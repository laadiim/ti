from typing import List
import tkinter as tk
import automat as a

# matrix for automat
automat_matrix = [[0, 0, 2, 0, 2, 1, 2, 7, 7, 10, 7, 11], [3, 4, 4, 5, 6, 9, 11, 8, 9, 9, 11, 11]]

# loads images to show
def load_images(directory: str) -> List[tk.PhotoImage]:
    """Load a list of images from the specified directory."""
    images = []
    for i in range(12):
        try:
            images.append(tk.PhotoImage(file=f"{directory}/{i}.png"))
        except tk.TclError as e:
            print(f"Error loading image {directory}/{i}.png: {e}")
    return images


# redraws the window
def redraw(label: tk.Label, active_state: int, images: List[tk.PhotoImage]):
    """Update the label to display the image for the active state."""
    label.config(image=images[active_state])
    label.image = images[active_state]  # Keep a reference to avoid garbage collection.


def main():
    aut = a.Automat(automat_matrix, 0)

    # initialize tkinter root window
    root = tk.Tk()
    root.title("Vizualizace automatů")

    # load images from the "states" directory
    images = load_images("states")
    if not images:
        print("No images loaded. Exiting.")
        return

    # initialize active state
    active_state = 0

    # create a Label to display the images
    image_label = tk.Label(root, image=images[active_state])
    image_label.pack()

    # define a function to handle key presses
    def handle_key(event, key):
        active_state = aut.move(key)
        redraw(image_label, active_state, images)

    def reset(event):
        active_state = aut.reset()
        redraw(image_label, active_state, images)

    def end(event):
        root.destroy()

    # bind arrow keys to the handle_key function
    root.bind("a", lambda e: handle_key(e, "a"))
    root.bind("b", lambda e: handle_key(e, "b"))
    root.bind("r", reset)
    root.bind("<Escape>", end)

    # start the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
