def myFunc(myList):
 print("List received: ",myList)
 myList.append(3)
 myList.extend([7,1])
 print("List after adding some elements:", myList)
 myList.remove(7)
 myList1=myList
 print("Address within function:")
 print((id(myList1)))
 print("List within called function:", myList)
 return
 
List1=[1]
print("Address before calling:",(id(List1)))
print("List before function call :",List1)
myFunc(List1)
print("List after function call: ",List1)
print("Address after calling:",(id(List1)))