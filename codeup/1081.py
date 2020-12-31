# 주사위 2개 던져서 나올 수 있는 모든 경우 출력
# 조건 : 주사위 2개의 면의 개수는 공백을 두고 입력됨. (10이하의 자연수)

number = input().split(" ")
for i in range(1,int(number[0])+1):
    for j in range(1, int(number[1])+1):
        print(i, j)