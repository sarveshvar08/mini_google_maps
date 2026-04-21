import tkinter as tk
from graph_data import create_map
from dijkstra import dijkstra, get_path

class MapUI:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=900, height=550, bg="#1e1e1e")
        self.canvas.pack()

        self.nodes, self.graph = create_map()

        self.node_items = {}
        self.start = None
        self.end = None

        self.car = None
        self.path_coords = []
        self.step_index = 0

        self.draw_map()

    def draw_map(self):
        drawn_edges = set()

        # 🚧 DRAW ROADS (ALWAYS SAME SHAPE)
        for node in self.graph:
            x1, y1 = self.nodes[node]

            for neighbor, weight in self.graph[node]:
                if (neighbor, node) in drawn_edges:
                    continue

                x2, y2 = self.nodes[neighbor]

                # ALWAYS horizontal → vertical
                self.canvas.create_line(x1, y1, x2, y1, fill="#555", width=2)
                self.canvas.create_line(x2, y1, x2, y2, fill="#555", width=2)

                # weight label
                mx, my = (x1 + x2)//2, (y1 + y2)//2
                self.canvas.create_text(mx, my, text=str(weight), fill="white")

                drawn_edges.add((node, neighbor))

        # 🏢 DRAW BUILDINGS
        for node, (x, y) in self.nodes.items():
            rect = self.canvas.create_rectangle(
                x-20, y-20, x+20, y+20,
                fill="#4da6ff", outline=""
            )
            self.canvas.create_text(x, y, text=node, fill="black")

            self.node_items[rect] = node
            self.canvas.tag_bind(rect, "<Button-1>", self.on_click)

    def on_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]

        if item not in self.node_items:
            return

        node = self.node_items[item]

        if not self.start:
            self.start = node
            self.canvas.itemconfig(item, fill="green")

        elif not self.end:
            self.end = node
            self.canvas.itemconfig(item, fill="red")

            self.start_animation()

        else:
            self.reset()

    # 🚗 START ANIMATION
    def start_animation(self):
        parent = dijkstra(self.graph, self.start)
        path = get_path(parent, self.start, self.end)

        self.path_coords = []

        for i in range(len(path)-1):
            x1, y1 = self.nodes[path[i]]
            x2, y2 = self.nodes[path[i+1]]

            steps = 25

            # 🚀 EXACT SAME LOGIC AS ROAD DRAWING
            # horizontal → vertical

            # horizontal movement
            for t in range(steps):
                x = x1 + (x2 - x1) * t / steps
                y = y1
                self.path_coords.append((x, y))

            # vertical movement
            for t in range(steps):
                x = x2
                y = y1 + (y2 - y1) * t / steps
                self.path_coords.append((x, y))

        self.step_index = 0

        # create car
        if self.car:
            self.canvas.delete(self.car)

        x, y = self.path_coords[0]
        self.car = self.canvas.create_text(x, y, text="🚗", font=("Arial", 16))

        self.animate_car()

    # 🎬 ANIMATION LOOP
    def animate_car(self):
        if self.step_index >= len(self.path_coords):
            return

        x, y = self.path_coords[self.step_index]

        self.canvas.coords(self.car, x, y)

        self.step_index += 1

        self.root.after(30, self.animate_car)

    # 🔄 RESET
    def reset(self):
        self.canvas.delete("all")
        self.start = None
        self.end = None
        self.car = None
        self.draw_map()