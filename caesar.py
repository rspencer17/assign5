def encode(plaintext, key):
    str1 = ''
    
    for i in plaintext:
        if ord(i) in range(65,91):
            i_index = ord(i) 
            i_shifted = (i_index + key)
            if i_shifted >= 91:
                i_shifted = i_index - 26 + key
            i_new = chr(i_shifted)
            str1 += i_new
        
        elif ord(i) in range(97,123):
            i_index = ord(i)
            i_shifted = (i_index + key)
            if i_shifted >= 123:
                i_shifted = i_index - 26 + key
            i_new = chr(i_shifted)
            str1 += i_new
        elif ord(i) < 65:
            str1 += i
        else:
            str1 += i
    return str1
# print(encode('z3bra2[!]', 4))
def decode(ciphertext, key):
    str2 = ''
    
    for j in ciphertext:
        if ord(j) in range(65, 91):
            j_index = ord(j)
            j_shifted = j_index - key
            if j_shifted < 65:
                j_shifted = j_index + 26 - key
            j_new = chr(j_shifted)
            str2 += j_new
        if ord(j) in range(97, 123):
            j_index = ord(j)
            j_shifted = j_index - key
            if j_shifted < 97:
                j_shifted = j_index + 26 - key
            j_new = chr(j_shifted)
            str2 += j_new
        if ord(j) >= 123:
            str2 += j
        if ord(j) < 65:
            str2 += j
    
    return str2
# print(decode('d3fve', 4))