import psutil

def get_system_info():
    current_cpu = psutil.cpu_percent(interval=1)
    current_disk =  psutil.disk_usage('/').percent
    current_memory =  psutil.virtual_memory().percent

    return {
       "CPU Usage" : current_cpu,
        "DIsk Usage" : current_disk,
        "Memory Usage" : current_memory
    }