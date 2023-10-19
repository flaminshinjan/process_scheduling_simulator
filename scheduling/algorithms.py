# File: scheduling/algorithms.py

def calculate_wait_time(burst_time, wait_time):
    n = len(burst_time)
    for i in range(1, n):
        wait_time[i] = burst_time[i - 1] + wait_time[i - 1]

def calculate_turnaround_time(burst_time, wait_time, turnaround_time):
    n = len(burst_time)
    for i in range(n):
        turnaround_time[i] = burst_time[i] + wait_time[i]

def fcfs(burst_time):
    n = len(burst_time)
    wait_time = [0] * n
    turnaround_time = [0] * n
    
    calculate_wait_time(burst_time, wait_time)
    calculate_turnaround_time(burst_time, wait_time, turnaround_time)

    avg_wt = sum(wait_time) / n
    avg_tat = sum(turnaround_time) / n

    return avg_wt, avg_tat

def sjn(burst_time):
    n = len(burst_time)
    wait_time = [0] * n
    turnaround_time = [0] * n

    burst_time.sort()  # Sort processes by burst time
    calculate_wait_time(burst_time, wait_time)
    calculate_turnaround_time(burst_time, wait_time, turnaround_time)

    avg_wt = sum(wait_time) / n
    avg_tat = sum(turnaround_time) / n

    return avg_wt, avg_tat

def priority_scheduling(burst_time, priority):
    n = len(burst_time)
    wait_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by priority
    paired_list = list(zip(burst_time, priority))
    paired_list.sort(key=lambda x: x[1])
    sorted_burst_time, _ = zip(*paired_list)

    calculate_wait_time(sorted_burst_time, wait_time)
    calculate_turnaround_time(sorted_burst_time, wait_time, turnaround_time)

    avg_wt = sum(wait_time) / n
    avg_tat = sum(turnaround_time) / n

    return avg_wt, avg_tat

def round_robin(burst_time, time_quantum):
    n = len(burst_time)
    wait_time = [0] * n
    turnaround_time = [0] * n
    remaining_burst_time = list(burst_time)

    t = 0  # Current time
    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > time_quantum:
                    t += time_quantum
                    remaining_burst_time[i] -= time_quantum
                else:
                    t += remaining_burst_time[i]
                    wait_time[i] = t - burst_time[i]
                    remaining_burst_time[i] = 0
        if done:
            break

    calculate_turnaround_time(burst_time, wait_time, turnaround_time)

    avg_wt = sum(wait_time) / n
    avg_tat = sum(turnaround_time) / n

    return avg_wt, avg_tat
