name = "Rover"
battery = 18
speed = 2.5
active = True

print(name, type(name))
print(battery, type(battery))
print(speed, type(speed))
print(active, type(active))

if battery < 20:
    print("Low battery!")