#1, 2, 3을 계속 더해 나갈 때, 그 합이 입력한 정수 (0~1000)보다 같거나\
#작을 때까지 계속 더하는 프로그램

number = int(input())
total_number = 0
i = 0
while (True):
    i += 1
    total_number += i
    if (total_number == number) or (total_number > number):
        print(i)
        break
        