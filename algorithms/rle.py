def encode(path: str) -> None:
    with open(path, 'r') as file:
        contents = file.readline()
        final_string = ''
        i: int = 0
        while i < len(contents):
            count: int = 1
            j: int = i

            while j < len(contents) - 1:
                if contents[j] == contents[j + 1]:
                    count += 1
                    j += 1
                else:
                    break

            count_bin = bin(count)[2:]
            contents_bin = bin(ord(contents[i]))[2:]

            final_string += '0' * (8 - len(count_bin)) + count_bin
            final_string += '0' * (8 - len(contents_bin)) + contents_bin

            i = j + 1

    open(f"{path.replace('.txt', '')}_encoded.txt", 'w').write(final_string)


def decode(path: str) -> None:
    with open(path, 'r') as file:
        contents = file.readline()
        decoded: str = ""
        i: int = 0
        while i < len(contents) - 1:
            count: int = int(contents[i:i + 8], 2)
            contents_bin: str = contents[i + 8:i + 16]
            decoded += chr(int(contents_bin, 2)) * count
            i += 16
        with open(f"{path.replace('_encoded.txt', '')}_decoded.txt", 'w') as file_decode:
            file_decode.write(decoded)
