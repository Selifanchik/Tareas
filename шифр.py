import sys
n = int(sys.stdin.readline())
encrypted_list = []
decrypted_list = []
decrypted_elem = 0
for item in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    encrypted_list.append(a)
for elem in encrypted_list:
    for term in elem:
        if term >= 0:
            decrypted_elem = decrypted_elem | term
    decrypted_list.append(str(decrypted_elem))
    decrypted_elem = 0
print(' '.join(decrypted_list))
#for item in range(n):
#    for jtem in range(n):
#        if item == jtem:
#            encrypted_list1[item][jtem] = -1
#        else:
#            encrypted_list1[item][jtem] = decrypted_list[item] & decrypted_list[jtem]
#print(encrypted_list1)

