test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

filtered_results =list( filter(lambda student: 50 <= student['result'] <= 70, test_results))
print(filtered_results)