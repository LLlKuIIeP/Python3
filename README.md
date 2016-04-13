# Python

## Файловый ввод/вывод

1)  Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

#### Sample Input:

a3b4c2e10b1

#### Sample Output:

aaabbbbcceeeeeeeeeeb

```
def find(s, i):
    j = i + 1
    print(s[i], s[j], j)

    while '0' <= s[j] <= '9' and j < len(s) - 1:
        j += 1
    print(s[i + 1:j])
    print()



file = open('dataset_3363_2.txt', 'r')
s = file.readline()
#print(s)

list = []
count = -1

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        list.append([s[i]])
        count += 1
    elif 'A' <= s[i] <= 'Z':
        list.append([s[i]])
        count += 1
    elif '0' <= s[i] <= '9':
        list[count].append(s[i])
#print(list)

for i in range(len(list)):
    #print(list[i][1::])
    str2 = ''
    for j in list[i][1::]:
        str2 = str2 + j
    print(list[i][0]*int(str2), end='')
print()
```

2)  Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

#### Sample Input:

abc a bCd bC AbC BC BCD bcd ABC

#### Sample Output:

abc 3

```
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
```

3)  Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 
```
print('First;Second-1 Second-2;Third'.split(';'))
['First', 'Second-1 Second-2', 'Third']
```
#### Sample Input:

Петров;85;92;78

Сидоров;100;88;94

Иванов;58;72;85

#### Sample Output:

85.0

94.0

71.666666667

81.0 84.0 85.666666667

```
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
```
