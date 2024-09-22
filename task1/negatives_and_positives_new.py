def main():
    testCases = int(input())
    
    for test in range(testCases):
        arraySize = int(input())
        array = list(map(int, input().split()))
        
        negativeCount = 0
        
        # Iterate through the array to count negatives and convert them to positive
        for i in range(arraySize):
            if array[i] < 0:
                negativeCount += 1  # Count the negative number
                array[i] = -array[i]  # Make the number positive
        
        if negativeCount % 2 == 0:
            print(sum(array))  # If the count of negative numbers is even, print the total sum
        else:
            # If odd, subtract twice the smallest value to get the maximum sum
            print(sum(array) - 2 * min(array))

if __name__ == "__main__":
    main()
