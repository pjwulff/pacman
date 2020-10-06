import math

## Normalises an angle so that it lies between [-pi, pi).
#
# @param angle The angle to be normalised.
# @return An angle between [-pi, pi).
def normalise(angle):
    while angle >= math.pi:
        angle = angle - 2*math.pi
    while angle < -math.pi:
        angle = angle + 2*math.pi
    return angle

## A predicate to decide if two angles are `close' according to some
## threshold.
#
# @param a The first angle.
# @param b The second angle.
# @param threshold The threshold to decide how close two angles need to be.
# Defaults to pi/8.
# @return A boolean value to indicate if the two angles are close according to
# the threshold.
def close(a, b, threshold = math.pi / 8.0):
    error = abs(normalise(a) - normalise(b))
    flip = 2*math.pi - error
    if error <= threshold or flip <= threshold:
        return True
    return False

## A predicate to decide if two angles are pointing in sufficiently opposite
## directions according to some threshold. That is, the two angles do not need
## to be exactly pi radians apart, but close enough to pi radians apparent
## within the threshold.
#
# @param a The first angle.
# @param b The second angle.
# @param threshold The threshold.
#
# @return A boolean value indicating if the two angles are pointing in
# sufficiently opposite directions.
def opposite(a, b, threshold = None):
    if threshold is not None:
        return close(a, b + math.pi, threshold)
    else:
        return close(a, b + math.pi)

## Flips an angle by pi radians so that it points in the opposite direction.
#
# @param angle The input angle.
#
# @return The input angle flipped by pi radians.
def flip(angle):
    return normalise(angle + math.pi)

## Returns the angle between two other angles (or equivalently between two
## unit length vectors). The order of the two input arguments is not important,
## as the absolute value of the angle is taken.
#
# @param a The first angle.
# @param b The second angle.
#
# @return The angle between them as a value between [0, pi]
def angle(a, b):
    error = abs(a - b)
    if error > math.pi:
        return 2*math.pi - error
    else:
        return error
