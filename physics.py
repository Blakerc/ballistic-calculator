def trajectory_with_drag(v0: float, weight_grains: float, step: float = 1.0, initial_height: float = 4.0, Cd: float = 0.3, diameter_in: float = 0.308):
    """
    Compute (x, y) points for a projectile with drag, in feet.
    v0: muzzle velocity (ft/s)
    weight_grains: bullet weight in grains
    step: distance step in feet
    initial_height: height above ground in feet
    Cd: drag coefficient (default 0.3)
    diameter_in: bullet diameter in inches (default .308)
    """
    import math
    # Constants
    rho = 0.0023769  # air density (slugs/ft^3)
    g = G
    # Convert bullet weight to slugs
    weight_lb = weight_grains / 7000.0
    mass_slugs = weight_lb / 32.174
    # Cross-sectional area (ft^2)
    diameter_ft = diameter_in / 12.0
    area = math.pi * (diameter_ft / 2) ** 2

    # Initial conditions
    x, y = 0.0, initial_height
    vx, vy = v0, 0.0
    points = [(x, y)]
    dt = 0.01  # time step (s)
    while y >= 0:
        v = math.sqrt(vx ** 2 + vy ** 2)
        Fd = 0.5 * Cd * rho * area * v ** 2
        ax = -Fd * vx / (v * mass_slugs) if v != 0 else 0
        ay = -g - (Fd * vy / (v * mass_slugs) if v != 0 else 0)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        if len(points) == 0 or abs(x - points[-1][0]) >= step:
            points.append((x, y))
    return points

import math

# Gravity in ft/s^2
G = 32.174  # ft/s^2

def trajectory_no_drag(v0: float, angle_deg: float, step: float = 10.0, initial_height: float = 3.0, weight_grains: float = 150.0):
    """
    Compute (x, y) points for a projectile (flat Earth, no drag), in feet.
    v0: muzzle velocity (ft/s)
    angle_deg: launch angle in degrees
    step: distance step in feet
    initial_height: height above ground in feet
    weight_grains: bullet weight in grains (currently unused)
    """
    angle_rad = math.radians(angle_deg)
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)

    points = []
    x = 0.0
    while True:
        t = x / v0x
        y = initial_height + v0y * t - 0.5 * G * t**2
        if y < 0:
            break
        points.append((x, y))
        x += step
    return points

def drop_at_distance(v0: float, angle_deg: float, distance: float, initial_height: float = 3.0) -> float:
    """
    Returns bullet height (y) at a given horizontal distance x, in feet.
    Positive y is above muzzle line, negative is below.
    initial_height: height above ground in feet
    """
    angle_rad = math.radians(angle_deg)
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)

    t = distance / v0x
    y = initial_height + v0y * t - 0.5 * G * t**2
    return y
