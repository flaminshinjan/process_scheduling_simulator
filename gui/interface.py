# File: gui/interface.py
import tkinter as tk
from tkinter import ttk, messagebox
from scheduling import algorithms

class SchedulingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title('Process Scheduling Simulator')
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Number of Processes:").grid(column=0, row=0, sticky=tk.W)
        self.num_processes = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.num_processes).grid(column=1, row=0)

        ttk.Label(self.root, text="Scheduling Algorithm:").grid(column=0, row=1, sticky=tk.W)
        self.algorithm = tk.StringVar()
        ttk.Combobox(self.root, textvariable=self.algorithm, values=('FCFS', 'SJN', 'Priority', 'Round Robin')).grid(column=1, row=1)

        ttk.Button(self.root, text="Setup Processes", command=self.setup_processes).grid(column=0, row=2, columnspan=2)

        # Additional input for Priority and Round Robin
        self.priority_entries = []
        self.time_quantum = tk.StringVar()
        self.time_quantum_entry = None

        self.process_entries = []

    def setup_processes(self):
        try:
            num = int(self.num_processes.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid number of processes.")
            return

        # Clear previous entries if they exist
        for entry in self.process_entries:
            entry[0].destroy()  # Label
            entry[1].destroy()  # Entry

        for entry in self.priority_entries:
            entry[0].destroy()  # Label
            entry[1].destroy()  # Entry

        if self.time_quantum_entry:
            self.time_quantum_entry.destroy()

        self.process_entries = []
        self.priority_entries = []

        for i in range(num):
            label = ttk.Label(self.root, text=f"Process {i+1} Burst Time:")
            entry = ttk.Entry(self.root)

            label.grid(row=i+4, column=0, sticky=tk.W)
            entry.grid(row=i+4, column=1)

            self.process_entries.append((label, entry))

            if self.algorithm.get() == 'Priority':
                priority_label = ttk.Label(self.root, text=f"Process {i+1} Priority:")
                priority_entry = ttk.Entry(self.root)

                priority_label.grid(row=i+4, column=2, sticky=tk.W)
                priority_entry.grid(row=i+4, column=3)

                self.priority_entries.append((priority_label, priority_entry))

        if self.algorithm.get() == 'Round Robin':
            ttk.Label(self.root, text="Time Quantum:").grid(column=0, row=num+4, sticky=tk.W)
            self.time_quantum_entry = ttk.Entry(self.root, textvariable=self.time_quantum)
            self.time_quantum_entry.grid(column=1, row=num+4)

        ttk.Button(self.root, text="Start Simulation", command=self.start_simulation).grid(column=0, row=num+5, columnspan=4)

    def start_simulation(self):
        burst_times = []
        for _, entry in self.process_entries:
            try:
                burst_time = int(entry.get())
                if burst_time <= 0:
                    raise ValueError("Burst time must be greater than 0.")
                burst_times.append(burst_time)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return

        selected_algorithm = self.algorithm.get()
        if selected_algorithm == 'FCFS':
            avg_wt, avg_tat = algorithms.fcfs(burst_times)
        elif selected_algorithm == 'SJN':
            avg_wt, avg_tat = algorithms.sjn(burst_times)
        elif selected_algorithm == 'Priority':
            priorities = []
            for _, entry in self.priority_entries:
                try:
                    priority = int(entry.get())
                    if priority < 0:
                        raise ValueError("Priority must be 0 or greater.")
                    priorities.append(priority)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
                    return
            avg_wt, avg_tat = algorithms.priority_scheduling(burst_times, priorities)
        elif selected_algorithm == 'Round Robin':
            try:
                time_quantum = int(self.time_quantum.get())
                if time_quantum <= 0:
                    raise ValueError("Time Quantum must be greater than 0.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return
            avg_wt, avg_tat = algorithms.round_robin(burst_times, time_quantum)
        else:
            messagebox.showerror("Error", "Selected algorithm is not implemented.")
            return

        messagebox.showinfo("Result", f"Average Waiting Time: {avg_wt}\nAverage Turnaround Time: {avg_tat}")

