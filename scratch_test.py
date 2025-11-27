from physics import drop_at_distance

v0 = 800.0        # m/s
angle = 1.5       # degrees
distance = 100.0  # meters

drop = drop_at_distance(v0, angle, distance)
print(f"Drop at {distance} m: {drop:.3f} m")
