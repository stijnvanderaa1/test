import psutil
import platform
import os
import datetime
import socket


def get_cpu_info():
    # CPU-informatie
    cpu_count = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU-gebruik in procenten
    cpu_freq = psutil.cpu_freq()
    cpu_freq_current = cpu_freq.current if cpu_freq else None
    return cpu_count, cpu_usage, cpu_freq_current


def get_memory_info():
    # Geheugeninformatie
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return memory.total, memory.available, memory.used, memory.percent, swap.total, swap.used, swap.percent


def get_disk_info():
    # Schijfgebruik
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            "total": partition_info.total,
            "used": partition_info.used,
            "free": partition_info.free,
            "percent": partition_info.percent
        }
    return disk_info


def get_network_info():
    # Netwerkinformatie
    network = psutil.net_if_addrs()
    net_info = {}
    for interface, addrs in network.items():
        for addr in addrs:
            # Controleer het familie type van het IP-adres
            if addr.family == socket.AF_INET:  # IPv4 adres
                net_info[interface] = {
                    "ip_address": addr.address,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast
                }
            elif addr.family == socket.AF_INET6:  # IPv6 adres
                net_info[interface] = {
                    "ip_address": addr.address,
                    "netmask": addr.netmask
                }
    return net_info


def get_system_info():
    # Algemene systeeminformatie
    system_info = {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "platform_release": platform.release(),
        "architecture": platform.architecture(),
        "hostname": platform.node(),
        "processor": platform.processor(),
        "uptime": str(datetime.timedelta(seconds=int(psutil.boot_time())))
    }
    return system_info


def gather_system_info():
    # Verzamel alle systeeminformatie
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    network_info = get_network_info()

    # Verzamel alle informatie in een enkele tekstvariabele
    system_data = ""

    system_data += "System Information:\n"
    for key, value in system_info.items():
        system_data += f"{key}: {value}\n"

    system_data += "\nCPU Information:\n"
    system_data += f"CPU Count: {cpu_info[0]}\n"
    system_data += f"CPU Usage Percent: {cpu_info[1]}%\n"
    system_data += f"CPU Frequency: {cpu_info[2]} MHz\n"

    system_data += "\nMemory Information:\n"
    system_data += f"Total Memory: {memory_info[0] / (1024 ** 3):.2f} GB\n"
    system_data += f"Available Memory: {memory_info[1] / (1024 ** 3):.2f} GB\n"
    system_data += f"Used Memory: {memory_info[2] / (1024 ** 3):.2f} GB\n"
    system_data += f"Memory Percent: {memory_info[3]}%\n"
    system_data += f"Total Swap: {memory_info[4] / (1024 ** 3):.2f} GB\n"
    system_data += f"Used Swap: {memory_info[5] / (1024 ** 3):.2f} GB\n"
    system_data += f"Swap Percent: {memory_info[6]}%\n"

    system_data += "\nDisk Information:\n"
    for device, info in disk_info.items():
        system_data += f"{device}:\n"
        system_data += f"  Total: {info['total'] / (1024 ** 3):.2f} GB\n"
        system_data += f"  Used: {info['used'] / (1024 ** 3):.2f} GB\n"
        system_data += f"  Free: {info['free'] / (1024 ** 3):.2f} GB\n"
        system_data += f"  Percent: {info['percent']}%\n"

    system_data += "\nNetwork Information:\n"
    for interface, info in network_info.items():
        system_data += f"{interface}:\n"
        system_data += f"  IP Address: {info['ip_address']}\n"
        system_data += f"  Netmask: {info['netmask']}\n"
        if "broadcast" in info:
            system_data += f"  Broadcast: {info['broadcast']}\n"

    return system_data


def main():
    # Verzamel systeeminformatie en sla op in een bestand
    gather_system_info()



if __name__ == "__main__":
    main()
