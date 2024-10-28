#w slowniku jest lista liczb zwrocic sume liczb ktore sa wieksze od jakiegos n
def f(d, n):
    sum = 0
    for key, value in d.items():
        for number in value:
            if number > n:
                sum += number
    return sum








print(f({"b": [5,4,3,2]}, 2))
print(f({"b": [5,2], "x": [1,2,1], "c": [4,1,2,1,2]}, 3))
print(f({"b": [5,4,3,2], "x": [1,2,1]}, 1))
print(f({"b": [5,2], "x": [1,2,1], "c": [4,1,2,1,2]}, 0))