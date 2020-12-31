#3 6 9 게임 

number = int(input())

for i in range(1, number+1):
    if i % 3 == 0:
        print("X", end=" ")
    else:
        print(i, end=" ")