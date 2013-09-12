'''
purpose
	encrypt P using substitution cipher with key K
preconditions
	P: possibly empty string of A..Z
	K: permutation of A..Z
'''
def substitution_encrypt(P,K):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	rString = ''
	for cha in P:
		rString += K[alphabet.index(cha)]
	#print 'Encryption: ' + P + ' --> ' + rString
    	return rString

'''
purpose
	decrypt C using substitution cipher with key K
preconditions
	C: possibly empty string of A..Z
	K: permutation of A..Z
'''
def substitution_decrypt(C,K):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	rString = ''
	for cha in C:
		rString += alphabet[K.index(cha)]
	#print 'Decryption: ' + C + ' --> ' + rString
	return rString


# test
#    ABCDEFGHIJKLMNOPQRSTUVWXYZ
K = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
C = substitution_encrypt('CAT',K)
if not C == 'DBU':
	print 'test_0 failed'
P = substitution_decrypt('DBU',K)
if not P == 'CAT':
	print 'test_1 failed'
