import tkinter as tk
import math

class App(tk.Frame):

    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("První GUI aplikace")
        self.nodes: List[Node] = []
        self.canvas: tk.Canvas = tk.Canvas(parent, width=600, height=400, bg='white')
        self.nodes.append(Node(100, 200, 30))
        self.edges = []
        self.edges.append(Edge(200, 200, 300, 300, 1, 'a'))
        self.edges.append(Edge(200, 200, 300, 300, 2, 'b'))
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

class Edge:
    def __init__(self, x_start: int, y_start: int, x_end: int, y_end: int, offset: float, letter: str):
        self.x_start: int = x_start
        self.y_start: int = y_start
        self.x_end: int = x_end
        self.y_end: int = y_end
        self.offset: float = offset
        self.letter: str = letter
        
    def draw(self, canvas):
        A: Tuple[int, int] = (self.x_start, self.y_start)
        C: Tuple[int, int] = (self.x_end, self.y_end)

        # Calculate the control point B based on the offset
        vect = [self.x_end - self.x_start, self.y_end - self.y_start]
        vect[0] /= 2
        vect[1] /= 2
        vect[0] += self.offset * (self.y_end - self.y_start)
        vect[1] -= self.offset * (self.x_end - self.x_start)

        B = (A[0] + vect[0], A[1] + vect[1])

        def bezier(t):
            """Calculate the point on the Bézier curve for parameter t."""
            x = (1 - t)**2 * A[0] + 2 * (1 - t) * t * B[0] + t**2 * C[0]
            y = (1 - t)**2 * A[1] + 2 * (1 - t) * t * B[1] + t**2 * C[1]
            return x, y

        def bezier_tangent(t):
            """Calculate the tangent vector on the Bézier curve for parameter t."""
            dx = 2 * (1 - t) * (B[0] - A[0]) + 2 * t * (C[0] - B[0])
            dy = 2 * (1 - t) * (B[1] - A[1]) + 2 * t * (C[1] - B[1])
            return dx, dy

        # Generate points along the curve
        points = []
        for t in range(101):  # t goes from 0 to 1 in steps of 0.01
            points.append(bezier(t / 100))

        # Flatten points for create_line
        flattened_points = [coord for point in points for coord in point]

        # Draw the Bézier curve
        canvas.create_line(flattened_points, smooth=True, fill="black", width=2)

        # Calculate midpoint (t = 0.5) and its tangent
        mid_x, mid_y = bezier(0.5)
        tangent_dx, tangent_dy = bezier_tangent(0.5)

        # Normalize the tangent vector
        tangent_length = math.sqrt(tangent_dx**2 + tangent_dy**2)
        tangent_dx /= tangent_length
        tangent_dy /= tangent_length

        # Define arrow properties
        arrow_length = 15
        arrow_angle = math.radians(30)

        # Calculate arrowhead points
        arrow_x1 = mid_x - arrow_length * (math.cos(arrow_angle) * tangent_dx - math.sin(arrow_angle) * tangent_dy)
        arrow_y1 = mid_y - arrow_length * (math.sin(arrow_angle) * tangent_dx + math.cos(arrow_angle) * tangent_dy)
        arrow_x2 = mid_x - arrow_length * (math.cos(-arrow_angle) * tangent_dx - math.sin(-arrow_angle) * tangent_dy)
        arrow_y2 = mid_y - arrow_length * (math.sin(-arrow_angle) * tangent_dx + math.cos(-arrow_angle) * tangent_dy)

        # Draw the arrow
        canvas.create_line(mid_x, mid_y, arrow_x1, arrow_y1, fill="red", width=2)
        canvas.create_line(mid_x, mid_y, arrow_x2, arrow_y2, fill="red", width=2)

        letter_x = mid_x - arrow_length * (math.cos(90) * tangent_dx - math.sin(90) * tangent_dy)
        letter_y = mid_y - arrow_length * (math.sin(90) * tangent_dx + math.cos(90) * tangent_dy)

        canvas.create_text(letter_x, letter_y, text=self.letter)


def main():
    root: tk.Tk = tk.Tk()
    app: App = App(root)
    app.mainloop()

if __name__ == "__main__":
    main()
