def main():
    testCases = int(input())

    for _ in range(testCases):
        arrayLength = int(input())  
        array = list(map(int, input().split()))         
        foundPalindromeSubsequence = False  # Flag to indicate if a palindrome subsequence is found

        # Check for each element if there is another element at least 2 positions away that is the same
        for i in range(arrayLength - 2):
            for j in range(i + 2, arrayLength):
                if array[i] == array[j]:  # If elements are equal and indices are at least 2 positions apart
                    print("YES")
                    foundPalindromeSubsequence = True  # Set flag to indicate palindrome subsequence found
                    break
            
            if foundPalindromeSubsequence:
                break
        
        if not foundPalindromeSubsequence:  # If no palindrome subsequence found, print "NO"
            print("NO")

if __name__ == "__main__":
    main()
