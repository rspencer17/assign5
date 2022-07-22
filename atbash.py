def encode(plaintext):
    encoded = ''
    
    for i in range(len(plaintext)):
        index_i = ord(plaintext[i])
        
        if (65 <= index_i and index_i <= 90):
            i_shifted = 90 - index_i
            encoded += chr(65 + i_shifted)
            
        if (97 <= index_i and index_i <= 122):
            i_shifted = 122 - index_i
            encoded += chr(97 + i_shifted)
            
        if int(index_i) < 65:
            encoded += chr(index_i)

            
    return encoded

def decode(ciphertext):
    decoded = ''
    
    for j in range(len(ciphertext)):
        j_index = ord(ciphertext[j])
        
        if (65 <= j_index and j_index <= 90):
            j_shifted = 90 - j_index
            decoded += chr(65 + j_shifted)
        if (97<= j_index and j_index <= 122):
            j_shifted = 122 - j_index
            decoded += chr(97 + j_shifted)
        if int(j_index) < 65:
            decoded += chr(j_index)
            
    return decoded
            