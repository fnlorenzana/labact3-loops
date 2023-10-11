k=int(input("How many rows?: "))
for i in range(k):
    for j in range(k-i):
        print(j+1, end=" ")
    print()