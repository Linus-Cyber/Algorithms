def encode( message: str ) -> str:

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = 'ab'
    output = ''
    password_index = 0
    password_length = len(password)
    for i in range(len(message)):
        #!Not in alphabet
        if message[i] not in alphabet:
            #print('Not in alpha')
            output += message[i]
            if password_index != password_length - 1:
                password_index += 1
            else:
                password_index = 0
            continue

        #print('Some letter', str(i))
        buchstabe = message[i]
        #print(password_index)
        output += alphabet[alphabet.index(message[i]) + alphabet.index(password[password_index])]
        if password_index != password_length - 1:
                password_index += 1
        else:
            password_index = 0
    return output
    
print(encode('Entwicklerhelden are having fun while coding.'))