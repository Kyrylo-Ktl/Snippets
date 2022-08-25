from math import atan2, cos, radians, sin, sqrt

EARTH_RADIUS = 6373.0


def haversine(a_coords: tuple, b_coords: tuple) -> float:
    lat1, lon1 = map(radians, a_coords)
    lat2, lon2 = map(radians, b_coords)

    lon_diff = lon2 - lon1
    lat_diff = lat2 - lat1

    angle = sin(lat_diff / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lon_diff / 2) ** 2
    c = 2 * atan2(sqrt(angle), sqrt(1 - angle))

    return EARTH_RADIUS * c


if __name__ == '__main__':
    kharkiv = (49.9935, 36.2304)
    kiev = (50.4501, 30.5234)
    dist = haversine(kharkiv, kiev)
    real = 410.9

    print(f'Distance: {dist}km')
    print(f'Real distance: {real}km')

    print(f'Error: {abs(1 - real / dist) * 100:0.2f}%')
