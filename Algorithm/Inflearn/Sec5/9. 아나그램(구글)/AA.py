# solution 1
import sys
word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()
dic1 = {}
dic2 = {}
for i in word1:
    dic1[i]=dic1.get(i, 0)+1
for i in word2:
    dic2[i]=dic2.get(i, 0)+1

# case 1)
if dic1==dic2:
    print("YES")
else:
    print("NO")

# # case 2)
# for i in dic1.keys():
#     if i in dic2.keys():
#         if dic1[i]!=dic2[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")




# solution 2
# import sys
# word1 = sys.stdin.readline().strip()
# word2 = sys.stdin.readline().strip()
# dic = {}
# for i in word1:
#     dic[i]=dic.get(i, 0)+1
# for i in word2:
#     dic[i]=dic.get(i, 0)-1

# for i in dic:
#     if(dic.get(i)>0):
#         print("NO")
#         break
# else:
#     print("YES")




# solution 3
# import sys
# word1 = sys.stdin.readline().strip()
# word2 = sys.stdin.readline().strip()
# str1 = str2=[0]*52
# for x in word1:
#     if x.isupper():
#         str1[ord(x)-65] += 1
#     else:
#         str1[ord(x)-71] += 1
# for x in word2:
#     if x.isupper():
#         str2[ord(x)-65] += 1
#     else:
#         str2[ord(x)-71] += 1

# for i in range(52):
#     if str1[i]!=str2[i]:
#         print("NO")
#         break
# else:
#     print("YES")
