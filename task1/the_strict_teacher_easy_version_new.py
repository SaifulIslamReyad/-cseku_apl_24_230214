def main():
    testCases = int(input())

    for test in range(testCases):
        classroomSize, teacherCount, queryCount = map(int, input().split())
        teachersPositions = list(map(int, input().split()))
        davidsPosition = list(map(int, input().split()))
        
        # Since teacherCount is always 2 and queryCount is always 1 in this problem
        teacher1 = teachersPositions[0]
        teacher2 = teachersPositions[1]
        davidPosition = davidsPosition[0]

        if teacher1 < classroomSize and teacher2 < classroomSize:
            print(davidPosition - max(teacher1, teacher2))
        elif teacher1 > classroomSize and teacher2 > classroomSize:
            print(min(teacher1, teacher2) - 1)
        else:
            print(abs(teacher1 - teacher2) // 2)

if __name__ == "__main__":
    main()
