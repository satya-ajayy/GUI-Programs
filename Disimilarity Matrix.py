from tkinter import Tk, Frame, Text, Button, StringVar, OptionMenu, END
from scipy.spatial import distance_matrix
import numpy as np

def GetMatrix():
    metric_map = {
        "Manhattan Distance": 1, "Euclidean Distance": 2,
        "Mahalanobis Distance": "mahalanobis"
    }

    try:
        rows = T1.get("1.0", END).strip().split("\n")
        mat = [list(map(int, row.split())) for row in rows if row.strip()]

        selected_metric = menu.get()
        if selected_metric not in metric_map:
            T2.delete("1.0", END)
            T2.insert(END, "Please select a valid distance metric!")
            return

        metric = metric_map[selected_metric]

        if metric == "mahalanobis":
            mat = np.array(mat)
            VI = np.linalg.inv(np.cov(mat.T))
            dist_mat = distance_matrix(mat, mat, VI=VI)
        else:
            dist_mat = distance_matrix(mat, mat, p=metric)

        T2.delete("1.0", END)
        for row in np.round(dist_mat, 2):
            T2.insert(END, "  ".join(f"{val:5.2f}" for val in row) + "\n")

    except Exception as e:
        T2.delete("1.0", END)
        T2.insert(END, f"Error: {e}")


root = Tk()
root.geometry("800x400")
root.title("Distance Matrix Calculator")

menu = StringVar(value="Select Any Metric")
option_menu = OptionMenu(root, menu, "Manhattan Distance", "Euclidean Distance", "Mahalanobis Distance")
option_menu.config(font=("Courier", 14))
option_menu.pack(pady=10)

frame = Frame(root)
T1 = Text(frame, height=10, width=22, font=("Courier", 14))
T1.grid(row=0, column=0, padx=10, pady=10)
T2 = Text(frame, height=10, width=22, font=("Courier", 14))
T2.grid(row=0, column=1, padx=10, pady=10)

Button(frame, text="Get Matrix", font=("Courier", 14), command=GetMatrix).grid(row=1, column=0, columnspan=2, pady=10)
frame.pack()
root.mainloop()
