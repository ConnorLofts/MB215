# Activity 14

t = (10, 20, [97, 98, 99])

list_from_tuple = list(t)

print("List from tuple:", list_from_tuple)

list_from_tuple[2].append(100) 

tuple_from_list = tuple(list_from_tuple)

print("Tuple from modified list:", tuple_from_list)

