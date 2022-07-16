from typing import List


List1 = ["Hello1",'Python1',["Hi","Python2"]]
List2 = ["Hello",'World',10,5.0,List1]
print(List2[0])

a = List2[2] + List2[3]
print(a)


List3 = List1 + List2
print(List3[2][1])