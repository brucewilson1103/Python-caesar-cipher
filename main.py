alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Direction determines if you are reading or encrypting
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
# The shift is the agreed upon value between the sender and reciever
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_output = ""
#   shift each letter in message
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_output += new_letter
  print(f"The encoded text is {cipher_output}")
   
encrypt(plain_text=text, shift_amount=shift)