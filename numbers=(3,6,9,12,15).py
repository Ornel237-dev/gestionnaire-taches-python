numbers=(3,6,9,12,15)
total=0
for num in numbers:
    if num%3==0 and num>6:
        total+=num
print(total)

x=10
print(x>5)

numbers=[[1,2],[3,4]]
copy=numbers.copy()
copy[0].append(5)
print(numbers)
print(copy)