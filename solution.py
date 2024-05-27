import json
from collections import deque, defaultdict
import heapq
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def parse_json(file_path):
    with open(file_path, 'r') as f:
        tasks = json.load(f)
    return tasks


def topological_sort(tasks):
    indegree = {task: 0 for task in tasks}
    graph = defaultdict(list)

    for task, info in tasks.items():
        for dep in info['dependencies']:
            graph[dep].append(task)
            indegree[task] += 1

    queue = deque([task for task, deg in indegree.items() if deg == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order


def schedule_tasks(tasks, N):
    topo_order = topological_sort(tasks)
    task_duration = {task: info['timeRequired'] for task, info in tasks.items()}
    start_time = {task: 0 for task in tasks}

    available_resources = [(0, i) for i in range(N)]
    heapq.heapify(available_resources)

    for task in topo_order:
        if tasks[task]['dependencies']:
            earliest_start = max(start_time[dep] + task_duration[dep] for dep in tasks[task]['dependencies'])
        else:
            earliest_start = 0
        current_time, resource = heapq.heappop(available_resources)
        actual_start = max(current_time, earliest_start)
        end_time = actual_start + task_duration[task]
        start_time[task] = actual_start
        heapq.heappush(available_resources, (end_time, resource))

    total_completion_time = max(start_time[task] + task_duration[task] for task in tasks)
    return total_completion_time, start_time


def visualize_schedule(tasks, start_time):
    fig, ax = plt.subplots()

    # Create a list of colors for different tasks
    colors = plt.get_cmap('tab20', len(tasks))

    for i, task in enumerate(tasks):
        start = start_time[task]
        duration = tasks[task]['timeRequired']
        ax.barh(task, duration, left=start, color=colors(i), edgecolor='black')

    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Task Schedule Gantt Chart')

    # Create custom legend
    patches = [mpatches.Patch(color=colors(i), label=task) for i, task in enumerate(tasks)]
    ax.legend(handles=patches)

    plt.show()


tasks = parse_json('tasks.json')
N = 2  # Number of resources

total_time, schedule = schedule_tasks(tasks, N)
print(f"Total completion time: {total_time}")
print("Task Start Times:")
for task, start in schedule.items():
    print(f"{task}: {start}")

# Visualize the schedule
visualize_schedule(tasks, schedule)
