oceans = ["Pacific", "Atlantic", "Indian", "Soutrhern", "Arcitec"]

with open('oceans.txt', "w") as f:
    for ocean in oceans:
        print(ocean,file=f)

with open('oceans.txt', "a") as f:
    print(23*"=",file=f)
    print("These are the 5 oceans.",file=f)

