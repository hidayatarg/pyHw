import math

# Input will be your student number which consists of 11 integers and this 
# information will be held in a list
studentNumber = [1, 1, 0, 7, 0, 0, 0, 1, 0, 2, 6]

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

# Lists to store the Raw outputs and shift outputs
c = []
d = []

# List shifting function
def shiftList(my_list, shift):
    assert shift < len(my_list)
    return my_list[shift:] + my_list[:shift]

#implement a dot product function for matrix multiplication
def dotMultiplication(v, w):
    a = sum([x*y for (x, *x2), y in zip(w, v)])
    b = round(a, 6)
    # print(counter1,":",b)
    d.append(b)
    c.append(1/(1+math.exp(-b)))

# Printing the list    
print("input=[{}]".format(studentNumber))
# Sending the intial list to dot product
dotMultiplication(studentNumber, w)

# Output after each shift by 1
for i in range(len(studentNumber)-1):
    studentNumber = shiftList(studentNumber, 1)
    print("input=[{}]".format(studentNumber))
    dotMultiplication(studentNumber, w)

# Print Raw Output for shift
# print("Raw Output for shift")
counter = 1
for cs in d:
    print("Raw Output for shift", counter, ":", round(cs, 6))
    counter += 1

# Output for shift
# print("Output for shift")
counter=1
for cs in c:
    print("Output for shift",counter,":", round(cs, 6))
    counter += 1




