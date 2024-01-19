from string import printable


def encrypt_messege(messege: str, shift: int) -> str:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += printable
    encrypted_messege = ''
    for char in messege:
        index = alphabet.find(char)
        encrypted_messege += alphabet[index + shift]
    return encrypted_messege


messege = encrypt_messege(Вася)
print(messege)


