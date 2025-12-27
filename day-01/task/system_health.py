import psutil
from concurrent.futures import ThreadPoolExecutor

cpu_threshold = int(input("Enter the CPU Threshold"))
disk_threshold = int(input("Enter the disk Threshold"))
memory_threshold = int(input("Enter the memory Threshold"))

def check_cpu_threshold():
    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU %: ",current_cpu)
    if current_cpu > cpu_threshold: 
        return "CPU Alert Email sent..."
    else:
        return "CPU in Safe state..."

def check_disk_threshold():
    current_disk =  psutil.disk_usage('/').percent
    print("Current disk %: ",current_disk)
    if current_disk > disk_threshold: 
        return "disk Alert Email sent..."
    else:
        return "disk in Safe state..."

def check_memory_threshold():
    current_memory =  psutil.virtual_memory().percent
    print("Current memory %: ",current_memory)
    if current_memory > memory_threshold: 
        return "memory Alert Email sent..."
    else:
        return "memory in Safe state..."


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {
        "check_cpu_threshold": executor.submit(check_cpu_threshold),
        "check_disk_threshold": executor.submit(check_disk_threshold),
        "check_memory_threshold": executor.submit(check_memory_threshold),
    }

results = {name: f.result() for name, f in futures.items()}

print(results)
