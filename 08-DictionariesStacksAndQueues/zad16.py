def hotel_list(hotels):
    for hotel in hotels:
        return ','.join([hotel["name"]])
  

def avg_price(hotels):
    for hotel in hotels:
        total_price=sum(hotel["price"])
    return round(total_price/len(hotels))


hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]
hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

# Calculating average prices and hotel lists for Krakow and Sopot
avg_price_krakow = avg_price(hotels_in_Krakow)
avg_price_sopot = avg_price(hotels_in_Sopot)
hotels_list_krakow = hotel_list(hotels_in_Krakow)
hotels_list_sopot = hotel_list(hotels_in_Sopot)

# Displaying the results
print(f"Hotels in Krakow: {hotels_list_krakow}")
print(f"Average hotel price in Krakow: {avg_price_krakow}")
print(f"Hotels in Sopot: {hotels_list_sopot}")
print(f"Average hotel price in Sopot: {avg_price_sopot}")

# Comparing average prices to find cheaper hotels
if avg_price_krakow < avg_price_sopot:
    print("Cheaper hotels in: Krakow")
elif avg_price_krakow > avg_price_sopot:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotel prices are equal in both cities")
