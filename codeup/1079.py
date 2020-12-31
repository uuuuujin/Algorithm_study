# 'q'가 입력될 때까지 입력한 문자를 게속 출력하는 프로그램 만들기

word = input()

for i in word:
    print(i)
    if i=='q':
        break