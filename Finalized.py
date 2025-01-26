import tkinter as tk
from tkinter import *
import customtkinter as Ctk
from customtkinter import CTkFrame, CTkLabel, CTkFont
import random
import time


class SortingWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm")

        self.master.geometry("1200x650")
        self.master.resizable(False,False)
        self.master.configure(background="black")

        font1 = CTkFont(family="Candara", size=50, weight="bold", slant="italic")

        self.header_frame = CTkFrame(master, corner_radius=1, fg_color="#f04245", height=90, border_color="#000000", border_width=5)
        self.header_frame.pack(fill=tk.X)

        self.header_label = CTkLabel(self.header_frame, text="SORTING", font=font1, text_color="#FFFFFF")
        self.header_label.place(relx=0.40, rely=0.5, anchor="w")

        self.footer_frame = CTkFrame(master, corner_radius=1, fg_color="#f04245", height=40, border_color="#000000", border_width=5)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.output_frame = tk.Frame(master, borderwidth=3, relief="groove", bg="#f04245")
        self.output_frame.place(relx=0.62, rely=0.5, relwidth=0.7, relheight=0.6, anchor="center")

        self.button_frame = tk.Frame(master, borderwidth=3, relief="groove", bg="#f04245")
        self.button_frame.place(relx=0.13, rely=0.54, relwidth=0.18, relheight=0.68, anchor="center")

        self.canvas_frame = CTkFrame(self.output_frame, corner_radius=10, fg_color="#FFFFFF", border_width=3)
        self.canvas_frame.pack(side=RIGHT, fill=BOTH, expand=False, padx=10, pady=10)

        self.canvas = Canvas(self.canvas_frame, bg="white", height=800, width=800)
        self.canvas.pack(fill=BOTH, expand=True)

        self.current_sort_window = None 
        self.current_canvas = None  
        self.data = []

        self.create_buttons()

    def create_buttons(self):
        self.generate_button = tk.Button(self.master, text="Generate Array", command=self.generate_array, font=("Lucida Console", 12), bg="#FFFFFF", height=5, width=20,)
        self.generate_button.place(relx=0.62, rely=0.85, relwidth=0.7, relheight=0.07, anchor="center")

        self.bubble_sort_button = tk.Button(self.button_frame, text="Bubble Sort", command=lambda: self.run_sort("bubble"), font=("Lucida Console", 10), fg="black",bg="#FFFFFF", width=20, height=2)
        self.bubble_sort_button.place (relx=0.5, rely=0.08, anchor="center")

        self.insertion_sort_button = tk.Button(self.button_frame, text="Insertion Sort", command=lambda: self.run_sort("insertion"), font=("Lucida Console", 10), bg="#FFFFFF", width=20, height=2)
        self.insertion_sort_button.place (relx=0.5, rely=0.22, anchor="center")

        self.selection_sort_button = tk.Button(self.button_frame, text="Selection Sort", command=lambda: self.run_sort("selection"), font=("Lucida Console", 10), bg="#FFFFFF", width=20, height=2)
        self.selection_sort_button.place (relx=0.5, rely=0.36, anchor="center")

        self.generate_button = tk.Button(self.button_frame, text="Merge Sort", command=lambda: self.run_sort("merge"), font=("Lucida Console", 10), bg="#FFFFFF", width=20, height=2)
        self.generate_button.place (relx=0.5, rely=0.50, anchor="center")

        self.bubble_sort_button = tk.Button(self.button_frame, text="Shell Sort", command=lambda: self.run_sort("shell"), font=("Lucida Console", 10), bg="#FFFFFF", width=20, height=2)
        self.bubble_sort_button.place (relx=0.5, rely=0.64, anchor="center")

        self.insertion_sort_button = tk.Button(self.button_frame, text="Quick Sort", command=lambda: self.run_sort("quick"), font=("Lucida Console", 10), bg="#FFFFFF", width=20, height=2)
        self.insertion_sort_button.place (relx=0.5, rely=0.78, anchor="center")

        self.insertion_sort_button = tk.Button(self.button_frame, text="Heap Sort", command=lambda: self.run_sort("heap"), font=("Lucida Console", 10), bg="#FFFFFF", width=20, height=2)
        self.insertion_sort_button.place (relx=0.5, rely=0.92, anchor="center")


    def generate_array(self):
        self.data = [random.randint(1, 100) for _ in range(20)]
        self.draw_data(self.data, ["red" for _ in self.data])

    def draw_data(self, data, color_array):
        self.canvas.delete("all")
        c_width = 785
        c_height = 350
        x_width = c_width / (len(data) + 1)
        offset = 30
        spacing = 10
        normalized_data = [i / max(data) for i in data]

        for i, height in enumerate(normalized_data):
            x0 = i * x_width + offset
            y0 = c_height - height * 300
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            self.canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

        self.master.update_idletasks()

    def run_sort(self, algorithm):
        if algorithm == "bubble":
            self.bubble_sort(self.data, self.draw_data, 0.1)
        elif algorithm == "insertion":
            self.insertion_sort(self.data, self.draw_data, 0.1)
        elif algorithm == "selection":
            self.selection_sort(self.data, self.draw_data, 0.1)
        elif algorithm == "merge":
            self.merge_sort(self.data, self.draw_data, 0.1)
        elif algorithm == "shell":
            self.shell_sort(self.data, self.draw_data, 0.1)
        elif algorithm == "quick":
            self.quick_sort(self.data, self.draw_data, 0.1)
        elif algorithm == "heap":
            self.heap_sort(self.data, self.draw_data, 0.1)

    def bubble_sort(self, data, draw_data, time_tick):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ["yellow" if x == j or x == j + 1 else "red" for x in range(len(data))])
                time.sleep(time_tick)
        draw_data(data, ["green" for _ in range(len(data))])

    def insertion_sort(self, data, draw_data, time_tick):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
                draw_data(data, ["yellow" if x == j + 1 else "red" for x in range(len(data))])
                time.sleep(time_tick)
            data[j + 1] = key
        draw_data(data, ["green" for _ in range(len(data))])

    def selection_sort(self, data, draw_data, time_tick):
        for i in range(len(data)):
            min_idx = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            draw_data(data, ["yellow" if x == i or x == min_idx else "red" for x in range(len(data))])
            time.sleep(time_tick)
        draw_data(data, ["green" for _ in range(len(data))])

    def merge_sort(self, data, draw_data, time_tick):
        def merge(data, left, mid, right):
            L = data[left:mid + 1]
            R = data[mid + 1:right + 1]
            i = j = 0
            k = left
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1
                draw_data(data, ["yellow" if x == k else "red" for x in range(len(data))])
                time.sleep(time_tick)
            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1
                draw_data(data, ["yellow" if x == k else "red" for x in range(len(data))])
                time.sleep(time_tick)
            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1
                draw_data(data, ["yellow" if x == k else "red" for x in range(len(data))])
                time.sleep(time_tick)

        def merge_sort_recursive(data, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort_recursive(data, left, mid)
                merge_sort_recursive(data, mid + 1, right)
                merge(data, left, mid, right)
                draw_data(data, ["green" for _ in range(len(data))])

        merge_sort_recursive(data, 0, len(data) - 1)

    def shell_sort(self, data, draw_data, time_tick):
        n = len(data)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = data[i]
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    j -= gap
                    draw_data(data, ["yellow" if x == j or x == j + gap else "red" for x in range(len(data))])
                    time.sleep(time_tick)
                data[j] = temp
                draw_data(data, ["yellow" if x == j else "red" for x in range(len(data))])
                time.sleep(time_tick)
            gap //= 2
        draw_data(data, ["green" for _ in range(len(data))])

    def quick_sort(self, data, draw_data, time_tick):
        def partition(data, low, high):
            pivot = data[high]
            i = low - 1
            for j in range(low, high):
                if data[j] <= pivot:
                    i += 1
                    data[i], data[j] = data[j], data[i]
                    draw_data(data, ["yellow" if x == i or x == j else "red" for x in range(len(data))])
                    time.sleep(time_tick)
            data[i + 1], data[high] = data[high], data[i + 1]
            draw_data(data, ["yellow" if x == i + 1 else "red" for x in range(len(data))])
            time.sleep(time_tick)
            return i + 1

        def quick_sort_recursive(data, low, high):
            if low < high:
                pi = partition(data, low, high)
                quick_sort_recursive(data, low, pi - 1)
                quick_sort_recursive(data, pi + 1, high)

        quick_sort_recursive(data, 0, len(data) - 1)
        draw_data(data, ["green" for _ in range(len(data))])

    def heap_sort(self, data, draw_data, time_tick):
        def heapify(data, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and data[l] > data[largest]:
                largest = l
            if r < n and data[r] > data[largest]:
                largest = r
            if largest != i:
                data[i], data[largest] = data[largest], data[i]
                draw_data(data, ["yellow" if x == i or x == largest else "red" for x in range(len(data))])
                time.sleep(time_tick)
                heapify(data, n, largest)

        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            draw_data(data, ["yellow" if x == 0 or x == i else "red" for x in range(len(data))])
            time.sleep(time_tick)
            heapify(data, i, 0)
        draw_data(data, ["green" for _ in range(len(data))])

if __name__ == "__main__":
    import random
    import time

root = tk.Tk()
app = SortingWindow(root)
root.mainloop()