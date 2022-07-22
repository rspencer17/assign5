import caesar
import atbash

plaintext = input('what is the message you want to share?')
key = int(input('what will the key be?'))
cipher_type = input("what type of cipher would you like to use (select c or a)?")
enc_or_dec = input("will this be message be encrypted (select e) or decrypted (select d)?")

if cipher_type == 'a' and enc_or_dec == 'e':
    print(atbash.encode(plaintext))
    
if cipher_type == 'a' and enc_or_dec == 'd':
    print(atbash.decode(plaintext))

if cipher_type == 'c' and enc_or_dec == 'e':
    print(caesar.encode(plaintext, key))

if cipher_type == 'c' and enc_or_dec == 'd':
    print(caesar.decode(plaintext, key))