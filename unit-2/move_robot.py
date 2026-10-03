def move_robot(x, y, speed=1.0):
    print(f"moving to ({x}, {y}) at {speed} m/s")


move_robot(3, 4)
move_robot(y=4, x=3)
move_robot(3, speed=2.0, y=4)