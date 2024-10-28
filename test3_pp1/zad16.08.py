def hotel_list(hotels):
    return  ", ".join([hotel["name"] for hotel in hotels])
def avg_price(hotels):
    return round((sum([hotel["price"]for hotel in hotels])/len(hotels)))

Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

print(hotel_list(Hotels_in_Krakow))
print(avg_price(Hotels_in_Krakow))
