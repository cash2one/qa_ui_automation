#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import codecs
if __name__ == '__main__':
#     str ='\xe6\xb5\xb7\xe5\x8d\x97'
#     print str.encode('utf-8')
    name = [[],[],[]]
    citys = []
    lists =[]
    with open('aate.txt') as f:
        for line in f:
            for each in enumerate(line.split(',')):
                name[each[0]].append(each[1])
#         print name
#         print name[1]
        citys = name[1]
        for city in citys:
            city.encode('utf-8')
#             print city
        lists.append(name[0])
        lists.append(citys)
        lists.append(name[2])
#         print lists
        for s in lists:
            print s
#         S='\n'.join(str(num)[1:-1] for num in list)
#         file =open(r'test.txt','w').write(S)
#         file.close()  
#     f = open("aate.txt","r")  
#     line= []
#     line2=[]
#     for eachline in f:
# #         print eachline
#         array =  eachline.split(',')
#         line.append(array[1])
#     print line
#     for i in line:
#         i=i.decode('utf-8')
#         line2.append(i)
#     print line2


f.close()