import cv2
import numpy as np
from tkinter import Tk, Button, Label, PhotoImage
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

def median_filter(image, kernel_size):
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

def calculate_mse(original_image, processed_image):
    mse = np.mean((original_image - processed_image) ** 2)
    return mse

def calculate_psnr(max_pixel_value, mse):
    psnr = 10 * np.log10((max_pixel_value ** 2) / mse)
    return psnr

# Fungsi untuk memilih gambar menggunakan file manager
def pilih_gambar():
    global original_image, original_image_label
    
    # Minta pengguna untuk memilih file gambar
    filename = askopenfilename()
    
    # Memuat gambar yang dipilih
    original_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    
    # Mengubah gambar menjadi format PIL
    original_image_pil = Image.fromarray(original_image)
    
    # Mengubah ukuran gambar agar sesuai dengan GUI
    original_image_pil = original_image_pil.resize((400, 400))
    
    # Mengubah gambar menjadi format PhotoImage untuk ditampilkan oleh Tkinter
    original_image_tk = ImageTk.PhotoImage(original_image_pil)
    
    # Memperbarui label dengan gambar yang dipilih
    original_image_label.configure(image=original_image_tk)
    original_image_label.image = original_image_tk

# Callback function untuk tombol "Terapkan Filter"
def terapkan_filter():
    global original_image, filtered_image, filtered_image_label, mse_label, psnr_label
    
    # Terapkan median filter
    kernel_size = 5
    filtered_image = median_filter(original_image, kernel_size)
    
    # Hitung nilai MSE dan PSNR untuk gambar hasil filter
    mse = calculate_mse(original_image, filtered_image)
    psnr = calculate_psnr(255, mse)
    
    # Memperbarui label MSE dan PSNR
    mse_label.configure(text="MSE: {:.2f}".format(mse))
    psnr_label.configure(text="PSNR: {:.2f}".format(psnr))
    
    # Mengubah gambar hasil filter menjadi format PIL
    filtered_image_pil = Image.fromarray(filtered_image)
    
    # Mengubah ukuran gambar hasil filter agar sesuai dengan GUI
    filtered_image_pil = filtered_image_pil.resize((400, 400))
    
    # Mengubah gambar hasil filter menjadi format PhotoImage untuk ditampilkan oleh Tkinter
    filtered_image_tk = ImageTk.PhotoImage(filtered_image_pil)
    
    # Memperbarui label dengan gambar hasil filter
    filtered_image_label.configure(image=filtered_image_tk)
    filtered_image_label.image = filtered_image_tk

# Inisialisasi Tkinter
root = Tk()
root.title("Mencari MSE dan PSNR Menggunakan Median Filter")

# Membuat label judul
judul_label = Label(root, text="Mencari MSE dan PSNR Menggunakan Median Filter")
judul_label.grid(row=0, column=0, columnspan=3, pady=10)

# Membuat tombol untuk memilih gambar
pilih_gambar_button = Button(root, text="Pilih Gambar", command=pilih_gambar)
pilih_gambar_button.grid(row=1, column=0, padx=10, pady=10)

# Membuat label untuk menampilkan gambar asli
original_image_label = Label(root)
original_image_label.grid(row=1, column=1, padx=10, pady=10)

# Membuat label untuk menampilkan gambar hasil filter
filtered_image_label = Label(root)
filtered_image_label.grid(row=1, column=2, padx=10, pady=10)

# Membuat label untuk menampilkan nilai MSE
mse_label = Label(root, text="MSE: ")
mse_label.grid(row=2, column=0, padx=10, pady=5)

# Membuat label untuk menampilkan nilai PSNR
psnr_label = Label(root, text="PSNR: ")
psnr_label.grid(row=3, column=0, padx=10, pady=5)

# Membuat tombol untuk menerapkan filter
terapkan_filter_button = Button(root, text="Terapkan Filter", command=terapkan_filter)
terapkan_filter_button.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

# Mulai event loop Tkinter
root.mainloop()
