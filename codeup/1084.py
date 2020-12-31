#빛 섞어서 색 만들기

color = input().split(" ")
color = [int(i) for i in color]
total = 0

for i in range(color[0]):
    for j in range(color[1]):
        for k in range(color[2]):
            print(i, j, k)
            total += 1
print(total)