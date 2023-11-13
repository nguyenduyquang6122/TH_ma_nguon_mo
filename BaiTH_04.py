import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
from tkinter import filedialog


def open_file_dialog():
    file_path = filedialog.askopenfilename(initialdir="/", title="Chọn file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if file_path:
        display_csv_data(file_path)

def display_csv_data(file_path):
    # Clear existing widgets in the frame
    for widget in frame_data.winfo_children():
        widget.destroy()

    # Read CSV data using pandas
    df = pd.read_csv(file_path)
    global in_data
    in_data = pd.read_csv(file_path, index_col = 0).values

    # Display header
    for col, header_value in enumerate(df.columns):
        label = Label(frame_data, text=header_value, padx=10, pady=5)
        label.grid(row=0, column=col)

    # Display data
    for row, (_, data) in enumerate(df.iterrows(), start=1):
        for col, value in enumerate(data):
            label = Label(frame_data, text=value, padx=10, pady=5)
            label.grid(row=row, column=col)

def create_repost():
    sv = in_data[:,1]
    tongsv = sv.sum()

    svF = in_data[:,10]
    svDat = np.subtract(sv,svF)
    svTruot = np.subtract(sv,svDat)
    sumDat = svDat.sum()
    sumTruot = svTruot.sum()
    tyle_dat = np.divide(np.sum(svDat),np.sum(sv))*100
    tyle_truot = 100 - tyle_dat

    svA_B = in_data[:,2:5+1]
    sumA_B = np.sum(svA_B)
    svC_D = in_data[:,6:9+1]
    sumC_D = np.sum(svC_D)
    sumF = np.sum(svF)

    svA = in_data[:,3]
    maxA = svA.max()
    i1 = np.where(svA == maxA)
    maxF = svF.max()
    minF = svF.min()
    i2 = np.where(svF == minF)
    i3 = np.where(svF == maxF)

    label_result.config(text="-Tổng sinh viên dự thi: "+f"{tongsv} sinh viên\n"
                        + "-Số sinh viên đạt: "+f"{sumDat} sinh viên\n"
                        + "-Số sinh viên trượt: "+f"{sumTruot} sinh viên\n" 
                        + "-Tỷ lệ sinh viên đạt: "+f"{tyle_dat} %\n"
                        + "-Tỷ lệ sinh viên trượt: "+f"{tyle_truot} %\n"
                        + "-Số sinh viên có điểm khá/giỏi là: "+f"{sumA_B} sinh viên\n"
                        + "-Số sinh viên có điểm TB/yếu là: "+f"{sumC_D} sinh viên\n"
                        + "-Số sinh viên có điểm kém (trượt) là: "+f"{sumF} sinh viên\n"
                        + "-Lớp có nhiều điểm A nhất là: {0} có {1} sinh viên đạt điểm A\n".format(in_data[i1,0],maxA)
                        + "-Lớp có ít điểm F nhất là: {0} có {1} sinh viên đạt điểm F\n".format(in_data[i2,0],minF)
                        + "-Lớp có nhiều điểm F nhất là: {0} có {1} sinh viên đạt điểm F\n".format(in_data[i3,0],maxF))
    
    plot_frame = Frame(w)
    plot_frame.pack()

    plt.plot(range(len(in_data[:, 3])), in_data[:, 3], 'r-', label="Diem A")
    plt.plot(range(len(in_data[:, 2:5+1])), in_data[:, 2:5+1], 'g-', label="Diem B +")
    plt.xlabel('Lớp')
    plt.ylabel('Số sv đạt điểm')
    plt.legend(loc='upper right')

    canvas = FigureCanvasTkAgg(plt.gcf(), master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

w = Tk()
w.title("Báo cáo học phần môn học")

button_file = Button(w, text="Chọn file", command=open_file_dialog)
button_file.pack()

frame_data = Frame(w)
frame_data.pack()

button_cre = Button(w, text="Tạo báo cáo", command=create_repost)
button_cre.pack()

label_result = Label(w, text="", justify='left', font=('Helvetica',10, 'bold'))
label_result.pack()

w.mainloop()

# diemA = in_data[:,3]
# diemBc = in_data[:,4]
# diemF = in_data[:,10]
# tongsvF = np.sum(diemF)
# SoSvQuaMon = (1 - tongsvF/SUMSV)*100
# print(f"So sinh vien truot mon la: {(tongsvF/SUMSV)*100}%")
# print(f"Trung binh so sv qua mon la: {SoSvQuaMon}%")
# print('Tong sv:',tongsv)
# maxa = diemA.max()
# i, = np.where(diemA == maxa)
# print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))

# #so sanh điểm A với B+
# tongA = diemA.sum()
# tongBc=diemBc.sum()
# print('so sv diem A ',tongA)
# print('so sv diem B+',tongBc)
# if tongA <= tongBc:
#     print('it sv diem A hon B+')
# else:
#     print('nhieu sv diem A hon B+')

# # Hiển thị thông tin về số SV thi, số SV đạt và số SV trượt
# # Lấy dữ liệu điểm từ DataFrame
# diem_data = df.iloc[:, 2:16]
# so_sv_thi = df.shape[0]
# so_sv_dat = (diem_data != 'F').sum().sum()
# so_sv_truot = so_sv_thi - so_sv_dat
# print('Tổng số sinh viên đi thi: {0}'.format(so_sv_thi))
# print('Tổng số sinh viên thi đạt: {0}'.format(so_sv_dat))
# print('Tổng số sinh viên thi trượt: {0}'.format(so_sv_truot))