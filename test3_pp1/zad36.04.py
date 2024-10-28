def f(detector):
    people_changes = list(map(lambda x: 1 if x == '+' else -1, detector))
    cumulative_sum = 0

    for change in people_changes:
        cumulative_sum += change
        if cumulative_sum >= 3:
            return True

    return False

print(f("+-+++-+---") )
print(f("+-+-+-+-"))
print(f("+-++-+--") )
print(f("+-++-++-+---") )

