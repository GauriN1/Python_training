temperature = int(input("Enter temperature: "))

if temperature < 0:
    print("below freezing")

elif temperature < 10:
    print("very cold")

elif temperature < 20:
    print("chilly")

elif temperature < 30:
    print("warm")

elif temperature < 40:
    print("hot")

else:
    print("too hot")
