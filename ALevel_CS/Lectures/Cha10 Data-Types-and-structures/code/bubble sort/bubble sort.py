def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
# parameter
# return value


arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array is:")
print(arr)

bubble_sort(arr)

print("Sorted array is:")
print(arr)


# Procedure bubble_sort(arr)
#     n <- length of arr

#     FOR i FROM 0 TO n-1 DO
#         FOR j FROM 0 TO n-i-2 DO
#             IF arr[j] > arr[j+1] THEN
#                 // Swap the elements
#                 temp <- arr[j]
#                 arr[j] <- arr[j+1]
#                 arr[j+1] <- temp
#             ENDIF
#         ENDFOR
#     ENDFOR
# End Procedure
