# implement a dot product function for 
# matrix multiplication


# a function to transform given values of a list

# Input will be your student number which consists 
# of 11 integers and this information will be held 
# in a list

studentNumber = [1, 1, 0, 7, 0, 0, 0, 1, 0, 2, 6]

# X = [1, 2, 3, 4, 5, 6]
print(studentNumber)



def list_shift(my_list, shift):
    assert shift < len(my_list)
    return my_list[shift:] + my_list[:shift]
    

for i in range(len(studentNumber)-1):
    studentNumber = list_shift(studentNumber, 1)
    print(studentNumber)


# another matrix 
w = [[0.03370361335647359],
     [0.07661115022886011],
     [0.04666099316268933],
     [0.0038889918178373803],
     [0.08421628276143776],
     [0.011537130067313111],
     [0.10048178370703198],
     [0.07406232623223129],
     [0.003752479172986443],
     [0.038102552367237044],
     [0.029275344822365088]]


# Tasks
# In this task you will shift your input student number 
# 1 element to left each time for 11 times.



# After each shift you will calculate dot product of it 
# with the w that has given to you.



