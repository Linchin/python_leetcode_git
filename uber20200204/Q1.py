def evenSubarray(numbers, k):

    # save all tuples that qualify in a dict

    qualified = {}

    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)+1):
            temp = numbers[i:j]
            temp_t = tuple(numbers[i:j])
            odd = [item % 2 for item in temp]
            if sum(odd) <= k and temp_t not in qualified:
                qualified[temp_t] = 1

    return len(qualified)



print(evenSubarray([1,2,3,4], 1))




