from tkinter import *
import numpy as np

def update_n():
    global n
    n = int(entry_n.get())

    label_A = Label(frame_A, text="Nhập ma trận hệ số A:")
    label_A.pack()

    global  entry_A
    entry_A = []
    for i in range(n):
        row = Frame(frame_A)
        row.pack()
        entry_A.append([])
        for j in range(n):
            entry_A[i].append(Entry(row))
            entry_A[i][j].pack(side=LEFT)

    label_B = Label(frame_B, text="Nhập vector kết quả B:")
    label_B.pack()

    global entry_B
    entry_B = []
    for i in range(n):
        entry_B.append(Entry(frame_B))
        entry_B[i].pack()

def solve_equations():
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(n):
        for j in range(n):
            A[i][j] = float(entry_A[i][j].get())

    for i in range(n):
        B[i] = float(entry_B[i].get())

    try:
        # Kiểm tra trường hợp ma trận A và vector kết quả B đều toàn số 0
        # toàn bộ các giá trị đã nhập
        if np.all(A == 0) and np.all(B == 0):
            print("Hệ phương trình vô số nghiệm.")
        else:
            # Tính bậc thang của ma trận A
            rref_A, _ = np.linalg.qr(A)

            # Số cột (hoặc hàng) độc lập tương ứng với bậc thang

            num_independent_columns = np.sum(np.abs(np.diag(rref_A)) > 1e-10)

            # Số biến tự do
            # phụ thuộc vào các thuộc tính của ma trận
            num_free_variables = A.shape[1] - num_independent_columns

            # Kiểm tra và in kết quả
            if num_free_variables > 0:
                result_label.config(text="Nghiệm của hệ phương trình:\n")
            elif num_free_variables == 0:
                X = np.linalg.solve(A, B)
                result = []
                for i in range(n):
                    result.append([])
                    result[i].append(f"x[{i + 1}] = {X[i]}")
            result_label.config(text="Nghiệm của hệ phương trình:\n" + str(result))
    except np.linalg.LinAlgError:
        result_label.config(text="Hệ phương trình vô nghiệm...")

app = Tk()
app.title("Giải hệ phương trình")

frame_n = Frame(app)
frame_n.pack()

label_n = Label(frame_n, text="Nhập số phương trình và số ẩn (n):")
label_n.pack(side=LEFT)

entry_n = Entry(frame_n)
entry_n.pack(side=LEFT)

button_update = Button(app, text="Cập nhật n", command=update_n)
button_update.pack()

frame_A = Frame(app)
frame_A.pack()

frame_B = Frame(app)
frame_B.pack()

button_solve = Button(app, text="Giải", command=solve_equations)
button_solve.pack()

result_label = Label(app, text="")
result_label.pack()

app.mainloop()
