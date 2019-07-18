def list_of_odd_numbers(numbers):
    list_of_odd_numbers = []
    for item in numbers: 
        if item % 2 == 1:
            list_of_odd_numbers.append(item)
    return sum(list_of_odd_numbers)
        
print(list_of_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))