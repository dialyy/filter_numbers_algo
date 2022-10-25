def multiple_of_3_numbers(numbers):
    return_data = []
    for num in numbers:
        if(num % 3 is 0):
            return_data.append(num)

    return sorted(return_data, reverse=True)


def is_multiple_of_3(n):
     
    odd_count = 0
    even_count = 0
 
    # Make no positive if + n is multiple of 3
    # then is -n. We are doing this to avoid
    # stack overflow in recursion
    if(n < 0):
        n = -n
    if(n == 0):
        return 1
    if(n == 1):
        return 0
 
    while(n):
         
        # If odd bit is set then
        # increment odd counter
        if(n & 1):
            odd_count += 1
 
        # If even bit is set then
        # increment even counter
        if(n & 2):
            even_count += 1
        n = n >> 2
 
    return is_multiple_of_3(abs(odd_count - even_count))

