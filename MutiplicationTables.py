
def multiplicationTables(a):
    for i in range(1,11,1):
        print(f"{a} * {i} = {a * i}")
        

a = int(input("Enter the number you would like to see multiplication tables\n"))

multiplicationTables(a)
