#Thêm nút chọn ảnh, xóa ảnh kết quả khi chọn ảnh mới, nút lưu ảnh vừa tạo
#Chọn 3 chế độ: nét ảnh, nét ảnh quá mữa, cải thiện ảnh
#Thêm chế độ làm mờ, nhập mức mờ

import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


img = None
img_save = None

def open_file_img():
    global img
    if img is not None:
        # Destroy the image-related components
        label_img_re.config(image="")
        label_img_re.image = None
        img = None

    file_path = filedialog.askopenfilename(filetypes=[("JPEG", "*.jpeg"), ("PNG", "*.png"), ("All file", "*.*")])
    if file_path:
        label_text_re.config(text="Ảnh kết quả")
        try:
            img = cv2.imread(file_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(img_pil)

            label_img_or.config(image=img_tk)
            label_img_or.image = img_tk
        except:
            messagebox.showerror("Lỗi", "Không đọc được ảnh")
            label_text_re.config(text="Hãy chọn ảnh")


def choice_button_1():
    if img is not None:
        entry.pack_forget()
        button_entry.pack_forget()
        button_lv1.pack(anchor='w')
        button_lv2.pack(anchor='w')
        button_lv3.pack(anchor='w')
    else:
        messagebox.showwarning("Cảnh báo", "Không có ảnh")
        label_text_re.config(text="Hãy chọn ảnh")


def choice_button_2():
    if img is not None:
        button_lv1.pack_forget()
        button_lv2.pack_forget()
        button_lv3.pack_forget()
        entry.pack(anchor='w')
        button_entry.pack(anchor='w')
    else:
        messagebox.showwarning("Cảnh báo", "Không có ảnh")
        label_text_re.config(text="Hãy chọn ảnh")

def lv1():
    label_text_re.config(text="Ảnh Sharpening")
    kernel_sharpen_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
    display_image(output_1)

def lv2():
    label_text_re.config(text="Ảnh Excessive Sharpening")
    kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
    output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
    display_image(output_2)

def lv3():
    label_text_re.config(text="Ảnh Egde Enhancement")
    kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                                  [-1,2,2,2,-1],
                                  [-1,2,8,2,-1],
                                  [-1,2,2,2,-1],
                                  [-1,-1,-1,-1,-1]])/8.0
    output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)
    display_image(output_3)

def entry_button():
    if img is not None:
        try:
            n = int(entry.get())
            kernel = np.ones((n,n), np.float32) / float(n*n)
            output = cv2.filter2D(img, -1, kernel)
            display_image(output)
        except:
            label_text_re.config(text="Hãy nhập số nguyên")
    else:
        messagebox.showwarning("Cảnh báo", "Không có ảnh")
        label_text_re.config(text="Hãy chọn ảnh")


def display_image(output_image):
    global img_save
    img_save = output_image
    img_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    label_img_re.config(image=img_tk)
    label_img_re.image = img_tk

def save_image():
    if img_save is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=[".png", ".jpeg"], filetypes=[("PNG", "*.png"), ("JPEG", "*.jpeg")])
        if file_path:
            cv2.imwrite(file_path, img_save)
            print("Lưu ảnh thành công.")
    else:
        messagebox.showwarning("Cảnh báo", "Không có ảnh để lưu")
        label_text_re.config(text="Không có ảnh để lưu")

w = Tk()
w.title("Chỉnh sửa ảnh")

frame_input = Frame(w)
frame_input.pack()

button_file = Button(frame_input, text="Chọn ảnh", command=open_file_img)
button_file.pack(side=LEFT)

frame_button_lv = Frame(frame_input)
frame_button_lv.pack(side=LEFT)

button_1 = Button(frame_button_lv, text="Chọn chế độ", command=choice_button_1)
button_1.pack()

button_lv1 = Button(frame_button_lv, text="Sharpening", command=lv1)
button_lv2 = Button(frame_button_lv, text="Excessive Sharpening", command=lv2)
button_lv3 = Button(frame_button_lv, text="Egde Enhancement", command=lv3)

frame_button_en = Frame(frame_input)
frame_button_en.pack(side=LEFT)


button_2 = Button(frame_button_en, text="Nhập mức làm mờ", command=choice_button_2)
button_2.pack()

entry = Entry(frame_button_en)
button_entry = Button(frame_button_en, text="Xác nhận", command=entry_button)

button_save = Button(frame_input, text="Lưu ảnh", command=save_image)
button_save.pack(side=LEFT)

frame_output = Frame(w)
frame_output.pack()

frame_origin = Frame(frame_output)
frame_origin.pack(side=LEFT)

label_text = Label(frame_origin, text="Ảnh gốc:")
label_text.pack()

label_img_or = Label(frame_origin)
label_img_or.pack()

frame_resutl = Frame(frame_output)
frame_resutl.pack(side=LEFT)

label_text_re = Label(frame_resutl, text="Ảnh kết quả:")
label_text_re.pack()

label_img_re = Label(frame_resutl)
label_img_re.pack()

w.mainloop()

# img = cv2.imread('haui.jpeg')
# cv2.imshow('Original', img)
# kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
# kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
#                              [-1,2,2,2,-1],
#                              [-1,2,8,2,-1],
#                              [-1,2,2,2,-1],
#                              [-1,-1,-1,-1,-1]])/8.0
# output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
# output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
# output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)
# cv2.imshow('Sharpening', output_1)
# cv2.imshow('Excessive Sharpening', output_2)
# cv2.imshow('Egde Enhancement', output_3)
# cv2.waitKey(0)
