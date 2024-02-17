import tkinter as tk
from tkinter import filedialog
from ModelReader import ModelReader
from ModelAnalyzer import ModelAnalyzer
from OCC.Display.SimpleGui import init_display

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("3D Model Analyzer")
        self.window.geometry("800x600")  # Set initial size of the window

        self.buttons = []
        self.text_fields = []

        self.create_text_field()
        self.create_buttons()

    def create_text_field(self):
        self.text_field = tk.Text(self.window, wrap=tk.WORD)
        self.text_field.pack(expand=True, fill=tk.BOTH)

    def create_buttons(self):
        load_model_button = tk.Button(self.window, text="Load Model", command=self.load_model)
        load_model_button.pack()
        self.buttons.append(load_model_button)

        analyze_model_button = tk.Button(self.window, text="Analyze Model", command=self.analyze_model)
        analyze_model_button.pack()
        self.buttons.append(analyze_model_button)

    def load_model(self):
        file_path = filedialog.askopenfilename(filetypes=[("STEP files", "*.stp;*.step")])
        if file_path:
            self.model_reader = ModelReader(file_path)
            self.model_analyzer = ModelAnalyzer(self.model_reader)
            self.model_analyzer.load_model()
            self.display_model()

            self.log_message("Model loaded successfully.")

    def analyze_model(self):
        if hasattr(self, 'model_analyzer'):
            self.model_analyzer.analyze_model()
            self.display_model()

    def display_model(self):
        if hasattr(self, 'model_analyzer') and self.model_analyzer.model:
            display, start_display, _, _ = init_display()
            display.DisplayShape(self.model_analyzer.model, update=True)
            start_display()

    def log_message(self, message):
        self.text_field.insert(tk.END, message + "\n")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
