#program code

#  (# are comments)

print("hello world")


count = 3



"""multi line string"""
multi_text = """sadfsdfsdf
fsdfsd"""




#inside quotation
text = "adcsa \" sfsdfsd \" dsfdsfsdf"

print(text)



#Boolean
booli = bool(count)

print(booli)



#NoneType

print(None)

print(type(None))

print(bool(None))



#Merging text

text1 = "I am"

text2 = "here"

print(text1 + " " + text2)




#f-string

print(f'hi, {text1} {text2}')




#Index

print(text[4])

print(text[6:10])

print(text[-9:-4])



#uppercase
print(text.upper())

#lowercase
print(text.lower())




#count

text3 = "count number"

print(text3.count("t"))




#replace
text4 = "Replace this"

print(text4.replace("this", "that"))




#length

print(len(text4))


#Strip

text5 = "      ajdklsad     "

print(text5)
print(text5.strip())
print(text5.lstrip())
print(text5.rstrip())




#Ismethods

text6 = "swsqwDFS12"

print(text6.isalnum())

print(text6.isalpha())

print(text6.isdigit())

print(text6.isupper())

print(text6.islower())




#text conversions of data type

text7 = 23

textc1 = str(text7)
textc2 = int(text7)
textc3 = float(text7)

print(textc1, textc2, textc3)



#list (mutable - changable)

list1 = ["a", "b", "c"]

print(list1[2])



#tuple (immutable - unchangable)

tuple1 = ("a", "b", "c")

print(tuple1[2])




#dictonary

weather = {"paris" :15, "tokyo" : 15}

#delete key from weather

del weather["paris"]

#adding new weather

weather["shangai"] = 15

print(weather)




#Sets - don't have key and value pair and index


fruit = {"apple", "pears"}

fruit.add("pineapples")

fruit.remove("pears")

print(fruit)




#identify operators

num1 = 10


print("is and  is not")

print(type(num1) is int)

print(type(num1) is not int)




#membership operators


text8 = "Hello world"

text9 = "Hello"

text10 = "hello"

print("in and not in")

print(text9 in text8)

print(text10 not in text8)




#conditions


a = 10

b = 13

if a>b:
	print("a is big")
elif a==b:
	print("a and b equal")
else:
	print("b is big")




#loops

#while loop
print("while loop")
count1 = 1

while count1 <= 10:
	print(count1)
	count1 += 1



#for loop
print("for loop")
for count1 in range (2, 12, 2):
	print(count1)


#function

def add_num (num1, num2, num3, num4):
	total_a = num1 + num2
	total_b = num3 + num4
	print("function")
	print(total_a, total_b)


add_num(1,2,3,4)




#python uses LEGB

#Global and Local Variable
print("Local and global Variable")

X = 1

def printme():
	global X
	X = X + 3
	print(X)

printme()

print(X)


print("without global keyword")
def printme1(y):
	y = y + 3
	print(y)
	return y

X = printme1(X)

print(X)





#logical and physical line of code

#logical

a0 = 10
b0 = 20


#physical

a1 = 10; b2 = 20;






#file operations


f = open("my_file.txt", "w")

a = "Jack"
b = "US"
f.write(a + "\n")
f.write(b + "\n")
f.close()


f = open("my_file.txt", "r")


text10 = f.read()
print(text10)

text11 = f.readlines()
print(text11)
f.close()



import os 
os.remove("my_file.txt")




