import math

def normalise(angle):
    if angle > math.pi:
        return angle - 2*math.pi
    if angle < -math.pi:
        return angle + 2*math.pi
    return angle

def close(a, b, threshold = math.pi / 8.0):
    error = abs(normalise(a) - normalise(b))
    flip = 2*math.pi - error
    if error <= threshold or flip <= threshold:
        return True
    return False

def opposite(a, b, threshold = None):
    if threshold is not None:
        return close(a, b + math.pi, threshold)
    else:
        return close(a, b + math.pi)

def flip(angle):
    return normalise(angle + math.pi)

def angle(a, b):
    error = abs(a - b)
    if error > math.pi:
        return 2*math.pi - error
    else:
        return error
