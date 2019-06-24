#Written by wojtekw0703

array = [10,15,3,7]
k = 17
first_number = 0
second_number = 0

for i in range(len(array)):
    for z in range(len(array)):
        temp = array[i]+array[z]
        if temp == k:
            first_number = array[i]
            second_number = array[z]


print(first_number)
print(second_number)
