import tkinter as tk
from edge import Edge

class App(tk.Frame):

    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("První GUI aplikace")
        self.nodes: List[Node] = []
        self.canvas: tk.Canvas = tk.Canvas(parent, width=600, height=400, bg='white')
        self.nodes.append(Node(100, 200, 30))
        self.edges = []
        self.edges.append(Edge(200, 200, 250, 250, 250, 150, 301, 301, "a"))
        #self.edges.append(Edge(200, 200, 300, 300, 2, 'b'))
        self.draw()

    def draw(self):
        for edge in self.edges:
            edge.draw(self.canvas)
        for node in self.nodes:
            node.draw(self.canvas)
        self.canvas.pack()

class Node:
    def __init__(self, x: int, y: int, r: int):
        self.x: int = x
        self.y: int = y
        self.r: int = r

    def draw(self, canvas: tk.Canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


def main():
    root: tk.Tk = tk.Tk()
    app: App = App(root)
    app.mainloop()

if __name__ == "__main__":
    main()
