def f(d):
    parked_cars = []
    exited_cars = []
    
    for car, status in d:
        if status == "in":
            parked_cars.append(car)
        elif status == "out":
            if car in parked_cars:
                parked_cars.remove(car)
                exited_cars.append(car)
    
    parked_cars = [car for car in parked_cars]
    return sorted(parked_cars)

# Test cases
cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))  # Output: ["BA111", "GX444", "KR234"]

cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))  # Output: []
