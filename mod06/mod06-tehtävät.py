#Tehtävä 2
numbers=[]
while True:
    input_number=input('Anna luku:')
    if input_number=='':
        break
    int(input_number)
    numbers.append(int(input_number))
numbers.sort(reverse=True)
for input_number in range(5):
    print(numbers[input_number])
