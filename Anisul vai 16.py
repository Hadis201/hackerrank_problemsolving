#Detecting the largest number among 3 using if elif
'''num1= 3422222
num2= 33222
num3= 342
if num1>num2:
    if num1>num3:
        print(num1, "is the largest number")

if num2>num3:
    if num2>num1:
        print(num2,"is the largest number")
else:
        print(num3, "is the largest number")
'''

#Detecting the largest number among 3 using if elif and logical operator
'''
num1 = 34
num2 = 24
num3 = 44
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
'''

#or related problem
'''
x = str("u")
if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
    print("vowel")
else:
    print("constant")
'''


'''
#this is so much powerful tool of python

num=int(input())

if 80 <= num <=100:
    print("A+")
if 70<=num<=79:
    print("A")
if 60 <= num <= 69:
        print("A-")
if 50<=num<=59:
    print("B")
if 40<=num<=49:
    print("C")
if 33<=num<=39:
    print("D")
else:
    print("fail")
'''
'''
i=100000000000000000000
while i<=1000000000000000000000000000000:
    print(i, end="")
    i=i+0000000000
'''

#while boy
'''
n=int(input("enter the number "))
i=1
sum=0
while i <= n :
    sum = sum + i
    i = i + 1

print(sum)
'''

'''
i=1
n= int(input())
while i <=n:

    print(i)
    i = i + 1
    if i == 5:
        break

'''
'''num1= 34
num2= 33
max = num1 if num1 > num2 else num2
print("Maximum = ", max  )'''
'''
subjects=["C", "C++","java", "Python"]
subjects.insert(2, "C#")
print(subjects)

subjects.remove("C#")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects2=subjects.copy()
print(subjects2)

pos=subjects2.count ("java")
print(pos)

subjects.clear( )
print(subjects)
''''''
list=list(range(1,19,2))
print(list)'''

num=[10,20,30,40]
for x in num:
    print(x)