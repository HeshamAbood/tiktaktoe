try:
    with open('sells.log') as file:
        pizza_col = (line[3] for line in file)
        per_hour = (int(x) for x in pizza_col if x != 'N/A')
        print("Total pizzas sold = ",sum(per_hour))
except FileNotFoundError :
    print("File not exists")
