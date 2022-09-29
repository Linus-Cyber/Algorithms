def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

        [1, 1, 'adfasf', True, 1<5]

#print(quick_sort([2, 5,3 , 6, 7, 3, 2]))
def count_clinking_glasses_for_variable_number_of_guests(number_of_guests):
    sequence = [0]
    zaehler = 1
    for _ in range(2000):
        sequence.append(sequence[-1] + zaehler)
        zaehler += 1
    print(sequence[0:10])
count_clinking_glasses_for_variable_number_of_guests(5)