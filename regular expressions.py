#regular expressions is sequence of chars,numbers ans special charecters whis is validate the data and search substring in mainstring
#regular expressions deals with strings olny not with different datatypes
#"abjahgei123" this is called mainstring and "ab"is called substring or pattern number of instances is nothing but number paterns
#we can use numbers with base 10
#compile function is which create the pattern
#whenever we use regular expression we have to import regularexpressions
import re
str1="absdjkfheabksheab124ab@#$ab246883abjgkashdfuew"
p=re.compile("ab")#by using we create object and pattern
l1=p.findall(str1)#by using object we can find all pattern
print(l1)
print(re.findall("ab",str1))#this is another type to find all pattern inthat first argument is substring and second aru=gument is mainstring
l2=p.finditer(str1)#which gives the location of pattern and matching object finditer will give itarable
print(l2)#it will give itarable loacton
for i in l2:#finditer is iterable so we want to print we can use loop
    print(i)
l2=re.finditer("ab",str1)
for i in l2:
    print(i)
#start() ,end(),group()
l2=re.finditer("ab",str1)
for i in l2:
    print(i)
    print("starting index=",i.start())
    print("ending index=",i.end())
    print("matching =",i.group())
    print("**********************")
#match():it will search in the starting of the mainstring
str="abc123#$%kfshtrosnslftjkssbcssbcslkfdjoerisbc"
m=re.match("ab",str)
print(m)
if l1!="none":
    print("string matched in the first of main string")
else:
    print("no match")
#search()
m=re.search("abc",str)#Doubt
print(m)
#fullmatch():it will check each and every letter and space also if everything is match it will print other it wise will give none
str2="krishnatejamoturi@gmail.com"
l3=re.fullmatch("krishantejamoturi@gmail.com",str2)#it will give none cause instead of na  i gave an
print(l3)
l3=re.fullmatch("krishnatejamoturi@gmail.com",str2)
print(l3)
str1="abcABhijklaABbopabtuvwaABbx12345ab67AB891ab0abcAB!@##abc$%^&AB**"
k=re.findall("abc",str1)#['abc', 'abc', 'abc']it will find to give abc together
print(k)
k=re.findall("[abc]",str1)#['a', 'b', 'c', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'c', 'a', 'b', 'c']it will find each and every letter
print(k)
k=re.findall("[a-k]",str1)#it will find a to k
print(k)
k=re.findall("[a-z]",str1)#it will find a to z
print(k)
k=re.findall("[A-Z]",str1)#it will find CAPTILAS LETTERS
print(k)
k=re.findall("[0-9]",str1)#it will print number from 0 to 1
print(k)
k=re.findall("[a-z0-9]",str1)#it will find all small letters and numbers from 0 to 9
print(k)
k=re.findall("[a-zA-Z0-9]",str1)#it will find captial letters and small letters and number 0 to 9
print(k)
k=re.findall("[^a-zA-Z0-9]",str1)#it will print without letter and numbers
print(k)
k=re.finditer("[^a-zA-Z0-9]",str1)
for i in k:
    print(i)
print(str1)
str1=re.sub("ab","ABC",str1)#it will changes wherever ab in that it will change print ABC
print(str1)
str1=re.subn("ABC","ABCD",str1)#it will change substring and it will tell us how many times it will changes
print(str1)
str1="abcABhijklaABbopabtuvwaABbx12345ab67AB891ab0abcAB!@##abc$%^&AB**"
a=re.split("ab",str1)#it will split on the bases of a
print(a)#['', 'cABhijklaABbop', 'tuvwaABbx12345', '67AB891', '0', 'cAB!@##', 'c$%^&AB**']
str2="abscsdjaabsfkjdaaakjdfhkjaaaaajkhfkjfaaaaaaakjhfkjfnkjdaaaaaaa"
a=re.finditer("a+",str2)#it will take minmun one char and maximum n number of chars
for i in a:
    print(i)
a=re.finditer("a?",str2)#it will check each and every char and give matching
for i in a:
    print(i)
a=re.finditer("[a-z]+",str2)
for i in a:
    print(i)
a=re.findall("a+",str2)#it will take min 1 value and max n values
print(a)
a=re.findall("[a]+",str2)#we can use []for finding min 1 and max n numbers values
print(a)
#a*be the combination of +and?
a=re.finditer("a*",str2)
for i in a:
    print(i)
a=re.findall("[a-c]+",str2)
print(a)
a=re.findall("a{3}",str2)#it will take max value as3 so it willl print all 3a's
print(a)
a=re.findall("a{2,4}",str2)#here min2 and max is 4
print(a)
str3="abj333kdsfh3333eoiuj333333kds12333333333kdsjfj345233333333kjjnsd45639347k3333333333jhwei"
a=re.findall("[0-9]+",str3)
print(a)
a=re.findall("3{3,}",str3)
print(a)
str5 = "sdflj(*&#s0283728373dlf04745839382jksd111394837493fl9382728373ksj(*&sdl9382728373fkjdsflkj@9382728373((&9382728373$)kdslfkjsdkj#(*@&"
a=re.findall("[0-9]{10}",str5)
print(a)
a=re.findall("[6-9][0-9]{9}",str5)
print(a)
#pan number
a=input("enter ur pan number:")
b=re.fullmatch("[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}",a)
print(b)
#email id
a=input("enter ur email.id:")
b=re.fullmatch("[a-zA-Z0-9]+[@]{1}[a-zA-Z]+[.]{1}[a-z]+",a)
print(b)
#us number
a=input("enter ur us number:")
b=re.fullmatch("[(][0-9]{3}[)]\s[0-9]{3}[.]{1}[0-9]{4}",a) or("[0-9]{3}[-]{1}[0-9]{1}[0-9]{4}",a)
print(b)