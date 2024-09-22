def main():
    testCases = int(input())

    for test in range(testCases):
        templateLength = int(input())
        template = list(map(int, input().split()))

        numberOfStrings = int(input())

        for __ in range(numberOfStrings):
            isValid = True
            charToValueMap = {}
            usedValues = []

            inputString = input()

            # Condition 1: Check if the string length matches the template length
            if len(inputString) != templateLength:
                print("NO")
                continue

            # Condition 2 and 3: Check for one-to-one correspondence
            for i in range(templateLength):
                if inputString[i] not in charToValueMap:
                    # Map the character to the corresponding template value
                    charToValueMap[inputString[i]] = template[i]

                    # Ensure template value hasn't already been assigned to a different character
                    if template[i] in usedValues:
                        print("NO")
                        isValid = False
                        break
                    
                    usedValues.append(template[i])
                else:
                    # If the character was already mapped, check if it matches the template value
                    if charToValueMap[inputString[i]] != template[i]:
                        print("NO")
                        isValid = False
                        break

            # If all checks passed, print "YES"
            if isValid:
                print("YES")

if __name__ == "__main__":
    main()

