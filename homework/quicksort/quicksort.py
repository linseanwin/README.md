numbers = [98, 39, 88, 11, 29, 85, 21, 6, 36] 

def quick_sort(numbers): 
    if len(numbers) <= 1:
        return numbers
    
    left= [] 
    right = [] 
    mid = []    
    pivot = numbers[0] 

    for number in numbers:
        if number == pivot:
            mid.append(number)
        elif number < pivot:
            left.append(number)
        else:
            right.append(number) 
    return quick_sort(left) + mid + quick_sort(right)
  print(quick_sort(numbers))
