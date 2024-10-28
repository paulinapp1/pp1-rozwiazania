washing_product = "jacket"
rinse = False
spin = False
if washing_product=="shoes" and rinse==True and spin==True:
    print("Total washing time: ", 20+15+9)
elif washing_product=="shoes" and rinse==True and spin==False:
    print("Total washing time: ", 20+15)
elif washing_product=="shoes" and rinse==False and spin==True:
    print("Total washing time: ", 20+9)
elif washing_product=="shoes" and rinse==False and spin==False:
    print("Total washing time: ", 20)

if washing_product=="jacket" and rinse==True and spin==True:
    print("Total washing time: ", 40+15+9)
elif washing_product=="jacket" and rinse==True and spin==False:
    print("Total washing time: ", 40+15)
elif washing_product=="jacket" and rinse==False and spin==True:
    print("Total washing time: ", 40+9)
elif washing_product=="jacket" and rinse==False and spin==False:
    print("Total washing time: ", 40)

if washing_product=="underwear" and rinse==True and spin==True:
    print("Total washing time: ", 70+15+9)
elif washing_product=="underwear" and rinse==True and spin==False:
    print("Total washing time: ", 70+15)
elif washing_product=="underwear" and rinse==False and spin==True:
    print("Total washing time: ", 70+9)
elif washing_product=="underwear" and rinse==False and spin==False:
    print("Total washing time: ", 70)


