def function1(num):
    list = []
    for i in range(num):
        list1 = [0]*num
        list1[0] = 1
        list.append(list1)
    for n in range(len(list)-1):
        for i in range(len(list)-1):
            list[n+1][i+1]=list[n][i]+list[n][i+1]

    for row in list:
        print(row)

function1(5)
