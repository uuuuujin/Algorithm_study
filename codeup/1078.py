# 정수(1~100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자!

number = int(input("1~100사이의 정수를 입력하세요 : "))
total = 0
for i in range(1,number):
    if i % 2 == 0:
        total += i
print(total)