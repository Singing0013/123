def factR(x):
    if x<=1:
        return 1 
    else:
        return(x*factR(x-1))
fac = int(input())
print(f"{fac}!={factR(fac)}")