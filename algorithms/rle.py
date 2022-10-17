

def encode(path: str) -> None:
    with open(path, 'r') as file:
        contents = file.readline()
        print(contents, '\n')
        final_string = ''

        noRepeatStr = ''
        length = 1
        for i in range(1, len(contents)):
            if contents[i-1] == contents[i]:
                if noRepeatStr != '':
                    noRepeatStr = contents[i-len(noRepeatStr)-1] + noRepeatStr
                    noRepeatStr = noRepeatStr[:-1]
                    print(length, noRepeatStr, i, 'no repeat ended')
                    final_string += toHelpByte(len(noRepeatStr), False)
                    for char in noRepeatStr:
                        final_string += toByte(ord(char))
                    noRepeatStr = ''
                    length = 1
            elif contents[i-1] != contents[i]:
                if length > 1 and noRepeatStr == '':
                    print(length, contents[i-1], i, 'repeat ended')
                    final_string += toHelpByte(length, True)
                    final_string += toByte(ord(contents[i-1]))
                    length = 0
                if length == 1:
                    noRepeatStr += contents[i]
                    length = 0
            length += 1
        
        if length > 1:
            print(length, contents[i-1], i, 'repeat ended')
            final_string += toHelpByte(length, True)
            final_string += toByte(ord(contents[i-1]))
            length = 0
        else:
            noRepeatStr = contents[len(contents)-len(noRepeatStr)-1] + noRepeatStr
            length = len(noRepeatStr)
            print(length, noRepeatStr, 'no repeat ended')
            final_string += toHelpByte(len(noRepeatStr), False)
            for char in noRepeatStr:
                final_string += toByte(ord(char))
            noRepeatStr = ''
            length = 1

        open(f"{path.replace('.txt', '')}_encoded.txt", 'w').write(final_string) 


def decode(path: str) -> None:
    with open(path, 'r') as file:
        contents = file.readline()
        print(contents)
        decoded_string = ''
        
        counter = 0
        while counter < len(contents):
            helpByte = contents[counter:counter+8]
            print('helpByte', helpByte)
            if helpByte[0] == '1':
                print('byte to add', contents[counter+8:counter+8+8], chr(int(contents[counter+8:counter+8+8], 2)), int(helpByte[1:], 2))
                for i in range(int(helpByte[1:], 2)):
                    decoded_string += chr(int(contents[counter+8:counter+8+8], 2))
                counter += 16
            else:
                for i in range(counter, counter + 8 * (int(helpByte[1:], 2) + 1), 8):
                    decoded_string += chr(int(contents[i:i+8], 2))
                counter += 8 * (int(helpByte[1:], 2) + 1) 
                    
        print(decoded_string)
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
