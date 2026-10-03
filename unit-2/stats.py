def stats(values):
    """Return mean, minimum and maximum of a list."""
    return sum(values) / len(values), min(values), max(values)


readings = [22.5, 23.1, 21.8, 24.0, 22.9]

mean, lo, hi = stats(readings)

print(f"mean={mean:.2f} min={lo} max={hi}")

packed = stats(readings)

print("as a tuple:", packed, type(packed))