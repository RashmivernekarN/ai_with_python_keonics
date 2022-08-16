from typing import List


List1 = ["Hello1",'Python1',["Hi","Python2"]]
List2 = ["Hello",'World',10,5.0,List1]
print(List2[0])

a = List2[2] + List2[3]
print(a)


List3 = List1 + List2
print(List3[2][1])

def sqr(str1,str2):
    result = str1 + str2
    print("Result of ", str1, " * ", str2, "= ",result)
    
    f1num =2.5
    f2num=2
    result = str1 * f2num
    print("Result of ", f1num, " * ", f2num, "= ",result)
sqr("hemanth","J")
   a-z,A_Z,0-9,_,.   @ a-z,0-9,.,  . a-z
     var validRegex = /^[a-zA-Z0-9.! # $%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;


name="tahir"


