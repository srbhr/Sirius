string = input().strip()

n = len(string)

c = 0

for i in range(n):

    flag = 0

    if string[i] == ')':

        continue

    for j in range(i, n+i):

        if string[j % n] == '(':

            flag += 1

        else:

            flag -= 1

        if flag < 0:

            break

    if flag == 0:

        c += 1

print(c)
