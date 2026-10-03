waypoints = [(1, 2), (3, 4), (5, 6)]

waypoints.append((7, 8))
waypoints.insert(1, (2, 3))
waypoints.remove((3, 4))

print("waypoints:", waypoints)
print("length:", len(waypoints))
print("sorted:", sorted(waypoints))