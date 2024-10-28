bottle_capacity = 500
filling_tolerance = 2
filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

incorrectly_filled = list(filter(lambda x: x <= 510 and x >= 490, filled_bottles))

correctly =  (len(incorrectly_filled) / len(filled_bottles)) * 100
result=100-correctly
print(result)
