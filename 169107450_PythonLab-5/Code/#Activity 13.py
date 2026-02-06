# Activity 13.

t = (10, 20, [97, 98, 99])

print("Original tuple:", t)

mutable_list = t[2]
mutable_list.append(100) 

print("Modified tuple:", t)
