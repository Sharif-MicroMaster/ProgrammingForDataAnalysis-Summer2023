import numpy as np

np.set_printoptions(precision=4)

get_A=input().split(' ')
get_B= input().split(' ')
get_C = input().split(' ')

for i in range (0,3) :
    get_A[i]= (int)(get_A[i])
    get_B[i] = (int) (get_B[i])
    get_C[i] = (int) (get_C[i])

vector_A = np.array(get_A)
vector_B = np.array(get_B)
vector_C = np.array(get_C)

dot = np.inner(vector_A,vector_B)
norm = np.linalg.norm(vector_A , ord=2)*np.linalg.norm(vector_B , ord = 2)
zavieh = np.arccos(dot/norm)

print("{0:.2f}".format(zavieh))

Afloat = np.array(vector_A, dtype=np.float32)
Bfloat = np.array(vector_B, dtype=np.float32)
Cfloat = np.array(vector_C, dtype=np.float32)

print(np.cross(Afloat, Cfloat) / np.linalg.norm(np.cross(Afloat, Cfloat)))
print ("{0:.2f}".format(np.linalg.norm(np.cross(vector_A, vector_B))))
print(np.block([vector_A, vector_B, vector_C]))
print(np.block([[vector_A], [vector_B], [vector_C]]))