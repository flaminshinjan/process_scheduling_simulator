def fcfs(process_list):
    n = len(process_list)
    wait_time = [0] * n
    turnaround_time = [0] * n
    total_wt = 0
    total_tat = 0

    # calculating waiting time for all processes
    for i in range(1, n):
        wait_time[i] = process_list[i - 1][1] + wait_time[i - 1]

    # calculating turnaround time by adding burst_time[i] + wait_time[i]
    for i in range(n):
        turnaround_time[i] = process_list[i][1] + wait_time[i]

    # calculating total waiting time and total turnaround time
    for i in range(n):
        total_wt = total_wt + wait_time[i]
        total_tat = total_tat + turnaround_time[i]

    return total_wt / n, total_tat / n

def sjn(process_list):
    n = len(process_list)
    wait_time = [0] * n
    turnaround_time = [0] * n
    total_wt = 0
    total_tat = 0

    # sorting processes by burst time
    process_list.sort(key=lambda x: x[1])

    # calculate waiting & turnaround time
    for i in range(1, n):
        wait_time[i] = process_list[i - 1][1] + wait_time[i - 1]
        turnaround_time[i] = process_list[i][1] + wait_time[i]

    # calculating total waiting time and total turnaround time
    for i in range(n):
        total_wt = total_wt + wait_time[i]
        total_tat = total_tat + turnaround_time[i]

    return total_wt / n, total_tat / n

def priority_scheduling(process_list):
    n = len(process_list)
    process_list.sort(key=lambda x: x[2])  # Sort by priority
    wait_time = [0] * n
    turnaround_time = [0] * n
    total_wt = 0
    total_tat = 0

    # calculating waiting time for all processes
    for i in range(1, n):
        wait_time[i] = process_list[i - 1][1] + wait_time[i - 1]

    # calculating turnaround time by adding burst_time[i] + wait_time[i]
    for i in range(n):
        turnaround_time[i] = process_list[i][1] + wait_time[i]

    # calculating total waiting time and total turnaround time
    for i in range(n):
        total_wt = total_wt + wait_time[i]
        total_tat = total_tat + turnaround_time[i]

    return total_wt / n, total_tat / n

def round_robin(process_list, quantum):
    n = len(process_list)
    burst_time = [process[1] for process in process_list]  # Extract burst time from process list
    wait_time = [0] * n
    t = 0  # Current time

    # Keep traversing processes in round-robin manner until all of them are not done
    while True:
        done = True

        for i in range(n):
            if burst_time[i] > 0:
                done = False
                if burst_time[i] > quantum:
                    t += quantum
                    burst_time[i] -= quantum
                else:
                    t = t + burst_time[i]
                    wait_time[i] = t - process_list[i][1]
                    burst_time[i] = 0
        if done:
            break

    turnaround_time = [wait_time[i] + process_list[i][1] for i in range(n)]
    return sum(wait_time) / n, sum(turnaround_time) / n

def get_processes(with_priority=False):
    num_processes = int(input("Enter number of processes: "))
    process_list = []

    for i in range(num_processes):
        process_id = input(f"Enter process ID for process {i+1}: ")
        burst_time = int(input(f"Enter burst time for process {i+1}: "))
        if with_priority:
            priority = int(input(f"Enter priority for process {i+1}: "))
            process_list.append((process_id, burst_time, priority))
        else:
            process_list.append((process_id, burst_time))

    return process_list

def main():
    print("Welcome to Process Scheduling Simulator\n")
    print("Enjoy a seamless experience with our simulator\n")

    # For First-Come, First-Serve Scheduling
    print("First-Come, First-Serve Scheduling")
    process_list = get_processes()
    avg_wt, avg_tat = fcfs(process_list)
    print(f"Average Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}\n")

    # For Shortest Job Next Scheduling
    print("Shortest Job Next Scheduling")
    process_list = get_processes()
    avg_wt, avg_tat = sjn(process_list)
    print(f"Average Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}\n")

    # For Priority Scheduling
    print("Priority Scheduling")
    process_list = get_processes(with_priority=True)
    avg_wt, avg_tat = priority_scheduling(process_list)
    print(f"Average Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}\n")

    # For Round Robin
    print("Round Robin Scheduling")
    process_list = get_processes()
    quantum = int(input("Enter time quantum: "))
    avg_wt, avg_tat = round_robin(process_list, quantum)
    print(f"Average Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}\n")

if __name__ == "__main__":
    main()
