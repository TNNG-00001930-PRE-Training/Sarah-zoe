
def gen_squared_dict(n):
    
    squared_dict = {}
    for i in range(1, n+1):
        squared_dict[i] = i*i
    return squared_dict

n = int(input("Enter an integral number: "))

result_dict = gen_squared_dict(n)

print(result_dict)


