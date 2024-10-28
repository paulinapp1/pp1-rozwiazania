def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        return "No second largest element"
    else:
        return second

def minmax(array):
    maxi=max(array)
    mini=min(array)
    return maxi-mini

def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if n % 2 == 0:  
        mid = n // 2
        median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:  
        mid = n // 2
        median = sorted_arr[mid]
    
    return median

def twoelement(arr):
    maxi=max(arr)
    mini=min(arr)
    result=[maxi,mini]
    return result

def array_to_string(arr):
    result = str(arr[0])
    for i in range(1, len(arr)):
        result += '-' + str(arr[i])
    return result


