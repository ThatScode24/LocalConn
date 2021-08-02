import psutil
import platform
from datetime import datetime
import os


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)

cpufreq = psutil.cpu_freq()
uname = platform.uname()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()

if os.path.isfile('data.txt'):
    os.remove('data.txt')

file_object = open(r"data.txt", "a")

file_object.write(f"""======================================== System Information ========================================
System: {uname.system}
Node Name: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}
Processor: {uname.processor}

======================================== Boot Time ========================================

Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}

======================================== CPU Info ========================================

Max Frequency: {cpufreq.max:.2f}Mhz
Min Frequency: {cpufreq.min:.2f}Mhz
Current Frequency: {cpufreq.current:.2f}Mhz 
Total CPU Usage: {psutil.cpu_percent()}%

======================================== Memory Information ========================================

Total: {get_size(svmem.total)}
Available: {get_size(svmem.available)}
Used: {get_size(svmem.used)}
Percentage: {svmem.percent}%

==================== SWAP ====================

Total: {get_size(swap.total)}
Free: {get_size(swap.free)}
Used: {get_size(swap.used)}
Percentage: {swap.percent}%

======================================== Disk Information ========================================

Total read: {get_size(disk_io.read_bytes)}
Total write: {get_size(disk_io.write_bytes)}

======================================== Network Information ========================================

Total Bytes Sent: {get_size(net_io.bytes_sent)}
Total Bytes Received: {get_size(net_io.bytes_recv)}
""")