def basic_fun(first,second,third):
    
    if first > second and first > third:
        print(f"The first value you entered {first} is the largest one.")
    elif second > first and second > third:
        print(f"The second value you entered {second} is the largest one.")
    elif third > first and third > second:
        print(f"The third value you entered {third} is the largest one.")
    else:
        print("Smth is wrong with the numbers you entered")

n1 = float(input("Introduce the first value: "))
n2 = float(input("Introduce the second value: "))
n3 = float(input("Introduce the third value: "))

basic_fun(n1,n2,n3)