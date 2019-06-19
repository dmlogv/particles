import random
import tkinter as tk
import tkinter.ttk as ttk


class ParticleGui(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=3, pady=3, fill='both', expand=True)
        self.winfo_toplevel().title(self.__class__.__name__)

        self.particles = []
        self.now_moving = False  # Mutex

        self.create_widgets()
        self.fill()

    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.update()

        self.canvas.bind('<ButtonPress-1>', self.random_move)
        self.canvas.bind('<ButtonPress-2>', self.random_position)
        self.canvas.bind('<ButtonPress-3>', self.move_to_pointer)
    
    def get_canvas_size(self):
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        return w, h

    def random_move(self, _):
        for particle in self.particles:
            self.canvas.move(particle, random.randint(-2, 2), random.randint(-2, 2))

    def random_position(self, _):
        w, h = self.get_canvas_size()

        for particle in self.particles:
            x, y, _, _ = self.canvas.coords(particle)
            self.canvas.move(particle, random.randint(int(-x), int(w - x)), random.randint(int(-y), int(h - y)))

    def move_to_pointer(self, event):
        # Prevent multiple run
        if self.now_moving:
            return
        
        self.now_moving = True

        target_x = event.x
        target_y = event.y

        def move_particle(particle, x, y):
            actual_x, actual_y, _, _ = self.canvas.coords(particle)
            
            if actual_x == x and actual_y == y:
                return 0
            
            dx, dy = x - actual_x, y - actual_y
            dmax = max(abs(dx), abs(dy))

            def magic(c):
                return c / dmax if dmax else 0

            self.canvas.move(particle, magic(dx), magic(dy))
            self.canvas.update()

            return 1

        while True:
            moved = 0
            for particle in self.particles:
                moved += move_particle(particle, target_x, target_y)

            self.after(0)

            if not moved:
                break
        
        self.now_moving = False
            

    def fill(self):
        for _ in range(100):          
            self.particles.append(self.canvas.create_oval(-10, -10, -12, -12))
            self.random_position(None)


if __name__ == '__main__':
    window = ParticleGui()
    window.mainloop()
