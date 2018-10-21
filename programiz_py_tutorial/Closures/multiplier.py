def make_multiplier_of(n):
    print("Clouser n:",n)
    def multiplier(x):
        print("From nested n:",n)
        print("From nested x:",x)
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))
print(type(times3))
# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))