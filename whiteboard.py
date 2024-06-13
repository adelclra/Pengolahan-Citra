import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from PIL import Image, ImageDraw
import os

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard App")
        
        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X)

        self.color_button = tk.Button(self.button_frame, text='Change Color', command=self.change_color)
        self.color_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text='Clear Canvas', command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.line_width_label = tk.Label(self.button_frame, text='Line Width:')
        self.line_width_label.pack(side=tk.LEFT, padx=5)

        self.line_width_slider = tk.Scale(self.button_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.line_width_slider.set(2)
        self.line_width_slider.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text='Save as Image', command=self.save_as_image)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.text_widget_label = tk.Label(self.button_frame, text='Notes:')
        self.text_widget_label.pack(side=tk.LEFT, padx=5)

        self.text_widget = tk.Text(self.button_frame, height=2, width=30)
        self.text_widget.pack(side=tk.LEFT, padx=5)

        self.color = 'black'
        self.old_x = None
        self.old_y = None
        self.line_width = self.line_width_slider.get()
        self.eraser_on = False
        self.active_button = self.color_button

        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def change_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delete('all')

    def save_as_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", '*.png'), ("All files", '*.*')])
        if file_path:
            self.save_canvas(file_path)

    def save_canvas(self, file_path):
        # Create an image from the canvas content
        self.canvas.update()
        self.canvas.postscript(file='temp_canvas.ps', colormode='color')
        image = Image.open('temp_canvas.ps')
        image.save(file_path, 'png')
        os.remove('temp_canvas.ps')

    def start_draw(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def draw(self, event):
        self.line_width = self.line_width_slider.get()
        self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

if __name__ == '__main__':
    root = tk.Tk()
    WhiteboardApp(root)
    root.mainloop()
