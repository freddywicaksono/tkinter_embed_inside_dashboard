import tkinter as tk

def open_mahasiswa_window(parent_frame):
    # Clear the content of the parent frame
    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Create widgets directly inside the parent frame
    admin_label = tk.Label(parent_frame, text="Mahasiswa Dashboard Content", font=("Helvetica", 14))
    admin_label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    content_frame = tk.Frame(root)
    inner_frame = tk.Frame(content_frame)
    inner_frame.pack(expand=True, fill=tk.BOTH)
    open_mahasiswa_window(inner_frame)
    content_frame.pack(expand=True, fill=tk.BOTH)
    root.mainloop()
