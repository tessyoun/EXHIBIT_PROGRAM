import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw
import os

class GridDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("부스 그리기")

        self.canvas_width = 800
        self.canvas_height = 600
        self.cell_size = 20

        self.drawing_mode = tk.StringVar(value="draw")
        self.selected_color = tk.StringVar(value="blue")
        self.undo_stack = []

        self.grid_data = [["white" for _ in range(self.canvas_width // self.cell_size)] for _ in range(self.canvas_height // self.cell_size)]

        self.setup_ui()
        self.create_grid()

        self.canvas.bind("<B1-Motion>", self.draw_or_erase)
        self.canvas.bind("<ButtonPress-1>", self.start_draw_or_erase)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw_or_erase)

        self.root.bind("<KeyPress-z>", self.set_draw_mode)
        self.root.bind("<KeyPress-Z>", self.set_draw_mode)
        self.root.bind("<KeyPress-x>", self.set_erase_mode)
        self.root.bind("<KeyPress-X>", self.set_erase_mode)

        self.current_action = []

    def setup_ui(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(side=tk.TOP, pady=10)

        colors_frame = tk.Frame(top_frame)
        colors_frame.pack(side=tk.LEFT, padx=5)

        colors = [("파란색", "blue"), ("빨간색", "red"), ("초록색", "green"), ("노란색", "yellow")]
        for color_name, color_value in colors:
            color_button = tk.Radiobutton(colors_frame, text=color_name, variable=self.selected_color, value=color_value)
            color_button.pack(side=tk.LEFT, padx=5)

        options_frame = tk.Frame(top_frame)
        options_frame.pack(side=tk.RIGHT, padx=5)

        draw_button = tk.Radiobutton(options_frame, text="그리기", variable=self.drawing_mode, value="draw")
        draw_button.pack(side=tk.LEFT, padx=5)
        erase_button = tk.Radiobutton(options_frame, text="지우기", variable=self.drawing_mode, value="erase")
        erase_button.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side=tk.BOTTOM, pady=10)

        self.save_path_entry = tk.Entry(bottom_frame, width=50)
        self.save_path_entry.pack(side=tk.LEFT, padx=5)
        browse_button = tk.Button(bottom_frame, text="찾아보기...", command=self.browse_save_path)
        browse_button.pack(side=tk.LEFT, padx=5)
        save_button = tk.Button(bottom_frame, text="이미지 저장하기", command=self.save_image)
        save_button.pack(side=tk.LEFT, padx=5)
        undo_button = tk.Button(bottom_frame, text="뒤로가기", command=self.undo)
        undo_button.pack(side=tk.LEFT, padx=5)

    def create_grid(self):
        self.canvas.delete('grid_line')
        for i in range(0, self.canvas_width, self.cell_size):
            self.canvas.create_line([(i, 0), (i, self.canvas_height)], tag='grid_line', fill='black')
        for i in range(0, self.canvas_height, self.cell_size):
            self.canvas.create_line([(0, i), (self.canvas_width, i)], tag='grid_line', fill='black')

    def start_draw_or_erase(self, event):
        self.current_action = []
        self.last_row_col = None

    def draw_or_erase(self, event):
        x, y = event.x, event.y
        row, col = y // self.cell_size, x // self.cell_size

        if self.last_row_col == (row, col):
            return

        self.last_row_col = (row, col)

        x1, y1 = col * self.cell_size, row * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size

        action = (x1, y1, x2, y2, self.drawing_mode.get(), self.selected_color.get())
        self.current_action.append(action)

        if self.drawing_mode.get() == "draw":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.selected_color.get(), outline="")
            self.grid_data[row][col] = self.selected_color.get()
        else:
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")
            self.grid_data[row][col] = "white"

    def end_draw_or_erase(self, event):
        self.save_canvas_state()
        self.create_grid()

    def save_canvas_state(self):
        self.undo_stack.append([row[:] for row in self.grid_data])
        if len(self.undo_stack) > 3:
            self.undo_stack.pop(0)

    def undo(self):
        if not self.undo_stack:
            return

        self.undo_stack.pop()
        self.grid_data = [row[:] for row in self.undo_stack[-1]]
        self.canvas.delete("all")
        self.create_grid()

        for row in range(len(self.grid_data)):
            for col in range(len(self.grid_data[row])):
                color = self.grid_data[row][col]
                if color != "white":
                    x1, y1 = col * self.cell_size, row * self.cell_size
                    x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def browse_save_path(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, folder_path)

    def save_image(self):
        folder_path = self.save_path_entry.get()
        if not folder_path:
            messagebox.showerror("에러", "경로를 지정하세요.")
            return

        if not os.path.isdir(folder_path):
            messagebox.showerror("오류", "유효하지 않은 경로")
            return

        # 그리드 데이터를 이미지로 저장
        image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        draw = ImageDraw.Draw(image)

        for row in range(len(self.grid_data)):
            for col in range(len(self.grid_data[row])):
                color = self.grid_data[row][col]
                if color != "white":
                    x1, y1 = col * self.cell_size, row * self.cell_size
                    x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                    draw.rectangle([x1, y1, x2, y2], fill=color)

        bbox = image.getbbox()
        if bbox:
            image = image.crop(bbox)

        image_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
        filepath = os.path.join(folder_path, f"image_{image_count + 1}.png")
        image.save(filepath)
        messagebox.showinfo("성공", f"{filepath}에 이미지를 저장했습니다.")

    def set_draw_mode(self, event):
        self.drawing_mode.set("draw")

    def set_erase_mode(self, event):
        self.drawing_mode.set("erase")

if __name__ == "__main__":
    root = tk.Tk()
    app = GridDrawingApp(root)
    root.mainloop()
