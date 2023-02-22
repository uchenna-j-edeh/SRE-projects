import csv
import subprocess
from datetime import datetime
from tabulate import tabulate

# Collect Metrics
cpu = subprocess.check_output(["top", "-n", "1", "-b"]).decode("utf-8")
memory = subprocess.check_output(["free", "-m"]).decode("utf-8")
disk = subprocess.check_output(["df", "-h"]).decode("utf-8")

# Store Metrics
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("server_metrics.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, cpu, memory, disk])

# Generate Report
with open("server_metrics.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    headers = ["Timestamp", "CPU Usage", "Memory Usage", "Disk Usage"]
    report = tabulate(data, headers=headers, tablefmt="grid")

print(report)

