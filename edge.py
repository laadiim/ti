import math
from typing import Tuple

class Edge:
    def __init__(self, x_start: int, y_start: int, x_b: int, y_b: int, x_c: int, y_c: int, x_end: int, y_end: int, label: str = ""):
        self.x_start: int = x_start  # A
        self.y_start: int = y_start
        self.x_b: int = x_b          # B
        self.y_b: int = y_b
        self.x_c: int = x_c          # C
        self.y_c: int = y_c
        self.x_end: int = x_end      # D
        self.y_end: int = y_end
        self.label: str = label      # Letter or text to draw next to the arrow

    def draw(self, canvas):
        A: Tuple[int, int] = (self.x_start, self.y_start)  # Start point
        B: Tuple[int, int] = (self.x_b, self.y_b)          # Control point at t = 0.3
        C: Tuple[int, int] = (self.x_c, self.y_c)          # Control point at t = 0.6
        D: Tuple[int, int] = (self.x_end, self.y_end)      # End point

        def bezier(t):
            """Calculate a point on the cubic Bézier curve for parameter t."""
            x = (1-t)**3 * A[0] + 3 * (1-t)**2 * t * B[0] + 3 * (1-t) * t**2 * C[0] + t**3 * D[0]
            y = (1-t)**3 * A[1] + 3 * (1-t)**2 * t * B[1] + 3 * (1-t) * t**2 * C[1] + t**3 * D[1]
            return x, y

        def bezier_tangent(t):
            """Calculate the tangent vector on the cubic Bézier curve for parameter t."""
            dx = -3 * (1-t)**2 * A[0] + 3 * (1-t)**2 * B[0] - 6 * t * (1-t) * B[0] + 6 * t * (1-t) * C[0] - 3 * t**2 * C[0] + 3 * t**2 * D[0]
            dy = -3 * (1-t)**2 * A[1] + 3 * (1-t)**2 * B[1] - 6 * t * (1-t) * B[1] + 6 * t * (1-t) * C[1] - 3 * t**2 * C[1] + 3 * t**2 * D[1]
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

        # Draw the label next to the arrowhead
        text_offset_x = 15 * tangent_dy  # Offset perpendicular to the tangent
        text_offset_y = -15 * tangent_dx
        canvas.create_text(mid_x + text_offset_x, mid_y + text_offset_y, text=self.label, fill="blue", font=("Arial", 12, "bold"))
