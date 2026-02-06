
#Activity 11

list1 = [1, 2, 3, 4]
list2 = [item**2 for item in list1]
print ("previous list ", list1)
print ("new list ", list2)

str_list = ['Winken', 'Blinken', 'Nod']
len_list = [len(s) for s in str_list]
print("number of chars in each string in the list is: ", len_list)

list1 = [1, 12, 2, 20, 3, 15, 4]
list2 = []
for n in list1:
    if n < 10:
        list2.append(n)
print ("list2 has all numbers that are less than 10:", list2)
