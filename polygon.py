from math import *

def polygon_work (n,s):
    """
    Input: n - number of sides, s - length of each side
    Returns the sum of area of polygon and square of the perimiter of polygon
    """
    area_polygon = (0.25 * n * s ** 2) / tan(pi / n)
    perimeter_polygon_squared = (n * s) ** 2
    sum_result = area_polygon + perimeter_polygon_squared
    return round(sum_result, 4)