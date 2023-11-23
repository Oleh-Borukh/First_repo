# Realization of Cezar's Cypher
# to_encrypt() function encrypt text
# to_decrypt() function decrypt text 

def to_encrypt(text: str(), key: int()):
    encrypted_text = ""
    for char in text:
        new_pos = ord(char) + key
        encrypted_text += chr(new_pos)
    return encrypted_text


def to_decrypt(encrypted_text: str(), key: int()):
    decrypted_text = ""
    for char in encrypted_text:
        new_pos = ord(char) - key
        decrypted_text += chr(new_pos)
    return decrypted_text


if __name__ == "__main__":
    cypher_key = int(input("Enter an encryption key (must be an integer): "))
    text = input("Enter a text, you want to encrypt: ")
    enc_text = to_encrypt(text, cypher_key)
    dec_text = to_decrypt(enc_text, cypher_key)
    print(f"Text: {text}\nCypher: {enc_text}\nDecrypted text: {dec_text}")