from tkinter import Tk, Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, root):
        self.canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.create_grid()
        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)
        self.canvas.bind("<B1-Motion>", self.erase)

    def create_grid(self):
        """Creates a grid of blue squares on the canvas."""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

    def create_eraser(self, event):
        """Creates an eraser at the mouse click location."""
        self.eraser = self.canvas.create_rectangle(
            event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink"
        )

    def erase(self, event):
        """Erases blue squares by setting them to white."""
        if self.eraser:
            self.canvas.moveto(self.eraser, event.x, event.y)
            overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            for item in overlapping_items:
                if item != self.eraser:
                    self.canvas.itemconfig(item, fill="white")

root = Tk()
root.title("Eraser Canvas")
app = EraserCanvas(root)
root.mainloop()