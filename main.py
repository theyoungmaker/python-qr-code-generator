import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    website = url_entry.get()
    filename = filename_entry.get()
    if website and filename:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(website)
        qr.make()
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = filename + ".png"
        img.save(img_path)
        show_qr_code(img_path, website)
    else:
        messagebox.showerror("Error", "Please enter both website URL and filename.")

        
def show_qr_code(img_path, website):
    qr_window = tk.Toplevel(window)
    qr_window.title("Generated QRCode")
    
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(qr_window, image=img)
    img_label.image = img
    img_label.pack()

    message = tk.Label(qr_window, text=f"Your website: {website}\nYour QR Code file name: {img_path}")
    message.pack()

window = tk.Tk()
window.title("QR Code Generator")

tk.Label(window, text="Website:").pack()
url_entry = tk.Entry(window)
url_entry.pack(padx=20)

tk.Label(window, text="File name of QR Code:").pack()
filename_entry = tk.Entry(window)
filename_entry.pack(padx=20)

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr)
generate_button.pack()

window.mainloop()
