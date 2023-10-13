n2=int(input("Input: "))
sum=0
formula=""

for i in range(1, n2+1):
    sum=sum+i
    formula =formula + str(i)
    if i != n2:
        formula=formula+"+"
print("Formula:", formula)
print("Output:", sum)