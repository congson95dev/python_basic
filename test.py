def create_double():
    def double(x):
        return x*2
    return double

double_10 = create_double()
result = double_10(10)
print(result)