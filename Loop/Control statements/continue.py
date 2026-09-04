n = int(input("Enter a number till which the loop will work : "))
for i in range(1,n+1):
    if i%2 == 0:
        continue
    print(i)
    
    