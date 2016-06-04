count = 0
lst = []
with open('my_2.txt') as file:
    for string in file:
        string = string.strip().split(';')
        #print(string)
        for i in string[1::]:
            count += int(i)
        print(count/3)
        string.append(count/3)
        #print(string)
        lst.append(string)
        #print(lst)
        count = 0

math = 0
phys = 0
rus = 0
for i in lst:
    math += int(i[1])
    phys += int(i[2])
    rus += int(i[3])
print(math/len(lst), phys/len(lst), rus/len(lst))
