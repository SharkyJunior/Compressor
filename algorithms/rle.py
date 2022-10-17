

def encode(path: str) -> None:
    with open(path, 'r') as file:
        contents = file.readline()
        final_string = ''

        noRepeatStr = ''
        length = 1
        for i in range(1, len(contents)):
            if contents[i-1] == contents[i]:
                if noRepeatStr != '':
                    noRepeatStr = contents[i-len(noRepeatStr)-1] + noRepeatStr[:-1]  # formatting sequence so it is written right
                    final_string += toHelpByte(len(noRepeatStr), False)  # appending help byte (0.......)
                    for char in noRepeatStr:  # adding sequence one by one
                        final_string += toByte(ord(char))
                    noRepeatStr = ''
                    length = 1
            elif contents[i-1] != contents[i]:
                if length > 1 and noRepeatStr == '':
                    final_string += toHelpByte(length, True) + toByte(ord(contents[i-1]))  # appending help byte (1.......) and symbol which was repeating
                    length = 0
                if length == 1:
                    noRepeatStr += contents[i]
                    length = 0
            length += 1
        
        
        # handling last sequence which is not handled in the previous loop
        if length > 1:
            final_string += toHelpByte(length, True) + toByte(ord(contents[i-1]))   # appending help byte (1.......) and symbol which was repeating
        else:
            noRepeatStr = contents[len(contents)-len(noRepeatStr)-1] + noRepeatStr  # formatting sequence so it is written right
            length = len(noRepeatStr)  
            final_string += toHelpByte(len(noRepeatStr), False)  # appending help byte (0.......)
            for char in noRepeatStr:  # adding last sequence one by one
                final_string += toByte(ord(char))

        open(f"{path.replace('.txt', '')}_encoded.txt", 'w').write(final_string)  # dumping all in the file


def decode(path: str) -> None:
    with open(path, 'r') as file:
        contents = file.readline()
        decoded_string = ''
        
        counter = 0
        while counter < len(contents):
            helpByte = contents[counter:counter+8]
            if helpByte[0] == '1':  # if the following sequence is repeating symbols
                for i in range(int(helpByte[1:], 2)):  # getting repeat count out of the help byte and adding that amount of repeating symbols
                    decoded_string += chr(int(contents[counter+8:counter+8+8], 2))  # getting the byte right after the help byte 
                counter += 16
            else:  # if the following sequence is non-repeating symbols
                for i in range(counter, counter + 8 * (int(helpByte[1:], 2) + 1), 8):  # going through bytes from (helpByte + 1) to (helpByte + unigueSymbolsLen + 1)
                    decoded_string += chr(int(contents[i:i+8], 2))  # adding particular symbol (converted from byte)
                counter += 8 * (int(helpByte[1:], 2) + 1)
                    
        open(f"{path.replace('_encoded.txt', '')}_decoded.txt", 'w').write(decoded_string)


def toByte(int: int) -> str:
    byte = format(int, 'b')
    while len(byte) < 8:
        byte = '0' + byte
    return byte


def toHelpByte(int: int, repeating: bool) -> str:
    byte = format(int, 'b')
    while len(byte) < 7:
        byte = '0' + byte
   
    if repeating:
        byte = '1' + byte
    else:
        byte = '0' + byte
    return byte
