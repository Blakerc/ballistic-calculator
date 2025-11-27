import math

G = 9.81  # m/s^2

def trajectory_no_drag(v0: float, angle_deg: float, step: float = 10.0):
    """
    Compute (x, y) points for a projectile (flat Earth, no drag).
    v0: muzzle velocity (m/s)
    angle_deg: launch angle in degrees
    step: distance step in meters
    """
    angle_rad = math.radians(angle_deg)
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)

    points = []
    x = 0.0
    while True:
        t = x / v0x
        y = v0y * t - 0.5 * G * t**2
        if y < 0:
            break
        points.append((x, y))
        x += step
    return points

def drop_at_distance(v0: float, angle_deg: float, distance: float) -> float:
    """
    Returns bullet height (y) at a given horizontal distance x.
    Positive y is above muzzle line, negative is below.
    """
    angle_rad = math.radians(angle_deg)
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)

    t = distance / v0x
    y = v0y * t - 0.5 * G * t**2
    return y
