from typing import List
import tkinter as tk
import automat as a

automat_matrix = [[0, 0, 2, 0, 2, 1, 2, 7, 7, 10, 7, 11], [3, 4, 4, 5, 6, 9, 11, 8, 9, 9, 11, 11]]

def load_images(directory: str) -> List[tk.PhotoImage]:
    """Load a list of images from the specified directory."""
    images = []
    for i in range(12):
        try:
            images.append(tk.PhotoImage(file=f"{directory}/{i}.png"))
        except tk.TclError as e:
            print(f"Error loading image {directory}/{i}.png: {e}")
    return images


def redraw(label: tk.Label, active_state: int, images: List[tk.PhotoImage]):
    """Update the label to display the image for the active state."""
    label.config(image=images[active_state])
    label.image = images[active_state]  # Keep a reference to avoid garbage collection.


def main():
    aut = a.Automat(automat_matrix, 0)

    # Initialize Tkinter root window
    root = tk.Tk()
    root.title("Vizualizace automatů")

    # Load images from the "states" directory
    images = load_images("states")
    if not images:
        print("No images loaded. Exiting.")
        return

    # Initialize active state
    active_state = 0

    # Create a Label to display the images
    image_label = tk.Label(root, image=images[active_state])
    image_label.pack()

    # Define a function to handle key presses
    def handle_key(event, key):
        active_state = aut.move(key)
        redraw(image_label, active_state, images)

    def reset(event):
        active_state = aut.reset()
        redraw(image_label, active_state, images)

    def end(event):
        root.destroy()

    # Bind arrow keys to the handle_key function
    root.bind("a", lambda e: handle_key(e, "a"))
    root.bind("b", lambda e: handle_key(e, "b"))
    root.bind("r", reset)
    root.bind("<Escape>", end)

    # Start the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
