numbers = [10,9,8,7,6,5,4,3,2,1,0]

for j in range(0,len(numbers)-1):
    swap = False
    for i in range(0,len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            swap = True
    if not swap:
        break



print(numbers)
