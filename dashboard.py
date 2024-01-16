import tkinter as tk
from tkinter import ttk
from admin import open_admin_window
from mahasiswa import open_mahasiswa_window
from dosen import open_dosen_window
from FrmPersegi import FrmPersegi

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("300x300")

        self.content_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
        self.content_frame.grid(row=0, column=0, sticky="nsew")

        self.inner_frame = ttk.Frame(self.content_frame)
        self.inner_frame.pack(expand=True, fill=tk.BOTH)

        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Admin", command=self.open_admin_window)
        file_menu.add_command(label="Mahasiswa", command=self.open_mahasiswa_window)
        file_menu.add_command(label="Dosen", command=self.open_dosen_window)
        file_menu.add_command(label="FrmPersegi", command=self.open_frm_persegi_window)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_program)

        menu_bar.add_cascade(label="Menu", menu=file_menu)
        root.config(menu=menu_bar)

    def open_admin_window(self):
        self.clear_content_frame()
        open_admin_window(self.inner_frame)

    def open_mahasiswa_window(self):
        self.clear_content_frame()
        open_mahasiswa_window(self.inner_frame)

    def open_dosen_window(self):
        self.clear_content_frame()
        open_dosen_window(self.inner_frame)

    def open_frm_persegi_window(self):
        self.clear_content_frame()
        FrmPersegi(self.inner_frame, "Program Luas Persegi Panjang")

    def exit_program(self):
        root.destroy()

    def clear_content_frame(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
