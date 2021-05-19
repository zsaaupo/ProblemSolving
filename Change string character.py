string_01 = "Bangladeshi"
print("Before change = ", string_01)
list_01 = list(string_01) # convert string to list datatype
list_01[string_01.index("i")] = " " # change 'i' to 'space' by index number
string_01 = "".join(list_01) # join all element of list as string
print("After change = ", string_01)