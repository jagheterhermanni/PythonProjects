# osInfo.py
# Created 19.2.2026

#This script displays some infomation about the current Operating System you're using.

import platform as pl
import subprocess
import psutil
import cpuinfo


def linux_distribution():
	"""Returning distro info using /etc/os-release(no external depencies)"""
	try:
		data = {}
		with open("/etc/os-release", "r", encoding="utf-8") as f:
			for line in f:
				line = line.strip()
				if not line or "=" not in line or line.startswith("#"):
					continue
				k, v = line.split("=", 1)
				data[k] = v.strip().strip('"')
		return (
			data.get("NAME", ""),
			data.get("VERSION_ID", ""),
			data.get("VERSION", ""),
		)
	except FileNotFoundError:
		return ("", "", "")

def cpu_model():
	if cpuinfo:
		return cpuinfo.get_cpu_info().get("brand_raw", "Unknown CPU")
	return "cpuinfo failed"

def cpu_cores():
	if psutil:
		return psutil.cpu_count(logical=True)
	return "psutil failed"

def cpu_usage():
	if psutil:
		return f"{psutil.cpu_percent(interval=1)}%"
	return "psutil failed"

def ram_info():
	if psutil:
		mem = psutil.virtual_memory()
		return f"{round(mem.used / 1e9, 2)}GB / {round(mem.total / 1e9, 2)}GB"
	return "psutil failed"

def disk_info():
	if psutil:
		disk = psutil.disk_usage('/')
		return f"{round(disk.used / 1e9,2)}GB / {round(disk.total / 1e9, 2)}GB"
	return "psutil failed"

def gpu_info():
	"""Linux GPU detection using lspci"""
	try:
		output = subprocess.getoutput("lspci | grep -i 'vga\\|3d'")
		return output if output else "No GPU found"
	except Exception:
		return "GPU detection failed"

def uname_clean():
	u = pl.uname()
	return f"{u.system} {u.release} ({u.machine})"

def print_item(name, value):
	print(f"{bcolors.OKBLUE}{name:<18}{bcolors.ENDC}: {bcolors.BOLD}{value}{bcolors.ENDC}")

profile = [
	"architecture",
	"linux_distribution", # Not in modern python anymore so we do own function
	"machine",
	"node",
	"platform",
	"python_build",
	"python_compiler",
	"python_version",
	"release",
	"system",
	"uname",
	"version",

	"cpu_models",
	"cpu_cores",
	"cpu_usage",
	"ram_info",
	"disk_info",
	"gpu_info",
]

class bcolors:
	HEADER ="\033[95m"
	OKBLUE = "\033[94m"
	OKGREEN = "\033[92m"
	WARNING = "\033[93m"
	FAIL = "\033[91m"
	ENDC = "\033[0m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"

locals_map = {
	"linux_distribution": linux_distribution,
	"cpu_model": cpu_model,
	"cpu_cores": cpu_cores,
	"cpu_usage": cpu_usage,
	"ram_info": ram_info,
	"disk_info": disk_info,
	"gpu_info": gpu_info,
}

for key in profile:
	fn = getattr(pl, key, None) or locals_map.get(key)
	if callable(fn):
		try:
			value = fn()
		except Exception as e:
			value = f"Error: {e}"
		print_item(key, value) 
		#print(f"{bcolors.OKBLUE}{key}{bcolors.ENDC}: {bcolors.BOLD}{value}{bcolors.ENDC}")
