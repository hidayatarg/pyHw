import math
# implement a dot product function for 
# matrix multiplication


# a function to transform given values of a list

# Input will be your student number which consists 
# of 11 integers and this information will be held 
# in a list

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

studentNumber = [1, 1, 0, 7, 0, 0, 0, 1, 0, 2, 6]

# X = [1, 2, 3, 4, 5, 6]
# print(studentNumber)
# print(w)



def list_shift(my_list, shift):
    assert shift < len(my_list)
    return my_list[shift:] + my_list[:shift]
c=[]
counter1 = 1
def dotMultiplication(v, w):
    a = sum([x*y for (x, *x2), y in zip(w, v)])
    b = round(a, 6)
    print(counter1,":",b)
    c.append(1/(1+math.exp(-b)))
    

dotMultiplication(studentNumber, w)
for i in range(len(studentNumber)-1):
    studentNumber = list_shift(studentNumber, 1)
    dotMultiplication(studentNumber, w)

print("outfunction")
counter=1
for cs in c:
    print("Output for shift",counter,":", round(cs, 6))
    counter += 1




