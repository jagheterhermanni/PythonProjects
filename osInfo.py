# osInfo.py
# Created 19.2.2026

#This script displays some infomation about the current Operating System you're using.

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

import platform as pl

profile = [
	"architecture",
	"linux_distribution", # Not in modern python anymore so we do own function
	"machine",
	"node",
	"platform",
	"processor",
	"python_build",
	"python_compiler",
	"python_version",
	"release",
	"system",
	"uname",
	"version",
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
}

for key in profile:
	fn = getattr(pl, key, None) or locals_map.get(key)
	if callable(fn):
		print(key + bcolors.BOLD + ": " + str(fn()) + bcolors.ENDC)
