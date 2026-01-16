import math
import random

# =========================
# FUNKCJE POMOCNICZE
# =========================

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def nearest_neighbor_route(base, points):
    route = [base]
    current = base
    remaining = points[:]

    while remaining:
        next_point = min(remaining, key=lambda p: distance(current, p))
        route.append(next_point)
        remaining.remove(next_point)
        current = next_point

    route.append(base)  # powrót do bazy
    return route

def route_distance(route):
    return sum(
        distance(route[i], route[i + 1])
        for i in range(len(route) - 1)
    )

# =========================
# PARAMETRY
# =========================

BASE = (0, 0)
DRIVERS = 3
ADDRESS_COUNT = 30

# losowe punkty (symulacja adresów)
ADDRESSES = [
    (random.randint(-20, 20), random.randint(-20, 20))
    for _ in range(ADDRESS_COUNT)
]

# =========================
# PODZIAŁ NA KIEROWCÓW
# =========================

ADDRESSES.sort(key=lambda p: distance(BASE, p))
drivers_points = [[] for _ in range(DRIVERS)]

for i, point in enumerate(ADDRESSES):
    drivers_points[i % DRIVERS].append(point)

# =========================
# WYLICZANIE TRAS
# =========================

def run():
    print(":truck: OPTYMALIZACJA TRAS\n")

    for idx, points in enumerate(drivers_points, start=1):
        route = nearest_neighbor_route(BASE, points)
        total = route_distance(route)

        print(f"Kierowca {idx}")
        for step in route:
            print(f"  {step}")
        print(f"Łączny dystans: {round(total, 2)}\n")

# =========================
# START
# =========================

if __name__ == "__main__":
    run()
