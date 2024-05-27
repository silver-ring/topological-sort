
# Task Scheduling and Visualization

This project demonstrates a task scheduling algorithm using multiple resources and visualizes the schedule using a Gantt chart. The scheduling algorithm is designed to minimize the total completion time while respecting task dependencies.

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `json`
  - `collections`
  - `heapq`
  - `matplotlib`

You can install the required Python libraries using the following command:

```bash
pip install matplotlib
```

## Files

- `task_scheduler.py`: The main script containing the task scheduling and visualization logic.
- `tasks.json`: Example JSON file with task definitions (if using file input, modify the script to read from this file).

## Running the Script

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Prepare the JSON Input**

   Ensure you have a valid JSON input for the tasks. You can use the example provided in the script or create your own. The JSON should have the following structure:

   ```json
   {
       "T1": {"timeRequired": 3, "dependencies": []},
       "T2": {"timeRequired": 2, "dependencies": ["T1"]},
       "T3": {"timeRequired": 4, "dependencies": ["T1"]},
       "T4": {"timeRequired": 1, "dependencies": ["T2", "T3"]}
   }
   ```

3. **Run the Script**

   Execute the script using Python:

   ```bash
   python task_scheduler.py
   ```

   The script will print the total completion time and the start times of each task. It will also display a Gantt chart visualizing the task schedule.

## Example Output

```
Total completion time: 7
Task Start Times:
T1: 0
T2: 3
T3: 3
T4: 7
```

A Gantt chart will be displayed showing the task schedule.

## Customization

You can modify the `tasks_json` variable in the script to use different task definitions. Additionally, you can adapt the script to read the JSON input from a file by replacing the `tasks_json` string with file reading logic.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

Inspired by task scheduling algorithms and visualization techniques.
