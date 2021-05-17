A = input("input scores serially after by after a space = ").split()
# input().split() for take list input inline
A = list(map(int, A))
# list declare A variable's Datatype
# i used map() method for convert list element's datatype to integer
A = (dict.fromkeys(A)) # remove duplicate data
# print(type(A))
A = list(A) # after remove duplicate data list become dictionary, so covert dictionary to list
A.sort(reverse = True)
print("The Runner-Up Score is = ",A[1])