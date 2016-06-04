def update_dict(diction, string):
    for i in string.split():
        if i in diction:
            diction[i] += 1
            #print('yes')
        else:
            diction.update({i:1})
            #print('no')

def find_max(diction):
    count = 0
    for i in diction:
        if count < diction[i]:
            count = diction[i]
    return count

def find_word(diction, maximum):
    lst = []
    for i in diction:
        if maximum == diction[i]:
            lst.append(i)
    lst.sort()
    return lst[0] + ' ' + str(maximum)
    

dic = {}
with open('my.txt') as file:
    for string in file:
        string = string.strip().lower()
        update_dict(dic, string)
        #print(string)
        #print(dic)
print(find_word(dic, find_max(dic)))
#count = find_max(dic)
#print(count)
