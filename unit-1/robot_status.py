robot = {"name": "Alpha", "battery": 78}

print(robot["name"])
print(robot["battery"])

robot["battery"] = 80
robot["speed"] = 2.5

print(robot)

print(robot.get("speed"))
print(robot.get("temperature", 0.0))
print("speed" in robot)

log = ["E2", "E7", "E2", "E1", "E7", "E2"]

freq = {}

for code in log:
    freq[code] = freq.get(code, 0) + 1

print(freq)

for code in sorted(freq, key=freq.get, reverse=True):
    print(f"{code} occurred {freq[code]} time(s)")

for key, value in robot.items():
    print(f"{key:<8} {value}")