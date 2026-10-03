def add_waypoint(wp, route=[]):
    route.append(wp)
    return route


r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))

print("r1 =", r1)
print("r2 =", r2)
print("same object?", r1 is r2)

#  the default list is shared between calls, so both routes contain both waypoints.