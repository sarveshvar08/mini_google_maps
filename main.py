import tkinter as tk
from ui import MapUI

root = tk.Tk()
root.title("Mini Google Maps")

app = MapUI(root)

root.mainloop()