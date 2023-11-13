import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog




def open_file_dialog():
    file_path = filedialog.askopenfilename(initialdir="/", title="Chọn file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if file_path:
        display_csv_data(file_path)
    global in_data
    in_data = pd.read_csv(file_path, index_col = 0).values
    print(in_data)

def display_csv_data(file_path):
    # Clear existing widgets in the frame
    for widget in frame_data.winfo_children():
        widget.destroy()

    # Read CSV data
    csv_reader = pd.read_csv(file_path)
    print(csv_reader)
    header = next(csv_reader)  # Read the header
    for col, header_value in enumerate(header):
        label = tk.Label(frame, text=header_value, padx=10, pady=5)
        label.grid(row=0, column=col)

    for row, data in enumerate(csv_reader, start=1):
        for col, value in enumerate(data):
            label = tk.Label(frame, text=value, padx=10, pady=5)
            label.grid(row=row, column=col)

w = Tk()
w.title("Báo cáo học phần môn học")

button_file = Button(w, text="Chọn file", command=open_file_dialog)
button_file.pack()

frame_data = Frame(w)
frame_data.pack(pady=20)

w.mainloop()

print('Tong so sinh vien di thi :')
sv = in_data[:,1]
tongsv = sv.sum()
print(tongsv)
print("Ty le % sinh vien dat :") #thêm tỷ lệ phần trăm
svF = in_data[:,10]
svDat = np.subtract(sv,svF)
tyle = np.divide(np.sum(svDat),np.sum(sv))*100
print(str(tyle) + "%")

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

# plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
# plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
# plt.xlabel('Lơp')
# plt.ylabel(' So sv dat diem ')
# plt.legend(loc='upper right')
# plt.show()
      