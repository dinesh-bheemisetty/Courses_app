def countingSort(arr):
    # Create a frequency array to store the count of each element
    frequency = [0] * 100
    
    # Count the occurrences of each element in the input array
    for num in arr:
        frequency[num] += 1
    
    # Print the frequency array as space-separated values
    for count in frequency:
        print(count, end=" ")

# Read the number of items
n = int(input().strip())

# Read the array of integers
arr = list(map(int, input().strip().split()))

# Call the countingSort function
countingSort(arr)
