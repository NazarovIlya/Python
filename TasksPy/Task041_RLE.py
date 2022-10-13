# Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


from unittest import result


def encrypt(text):
    chr = text[0]
    enc_str = ''
    counter = 0
    for c in text:
        if c == chr:
            counter += 1
            continue
        enc_str += str(counter)
        enc_str += str(chr)
        chr = c
        counter = 1
    enc_str += str(counter)
    enc_str += chr
    return enc_str


def decrypt(text):
    new_str = ''
    index = ''
    for c in text:
        if c.isdigit():
            index += c
        else:
           new_str += c * int(index)
           index = ''
    return new_str


source_uncopressed_file_path = 'Task041_RLE/uncompressed_for_RLE.txt'
encrypt_result = 'Task041_RLE/compress_result.txt'
source_compressed_file_path = 'Task041_RLE/compressed_for_RLE.txt'
decrypt_result = 'Task041_RLE/decompress_result.txt'

with open(source_uncopressed_file_path, 'r') as source:
    uncompressed_info = source.read()
    
compressed_result = encrypt(uncompressed_info)  

with open(encrypt_result, 'w') as compressed:
    compressed.write(compressed_result)
    

with open(source_compressed_file_path, 'r') as source:
    compressed_info = source.read()
    print(compressed_info)

decompressed_result = decrypt(compressed_info)
print(decompressed_result)

with open(decrypt_result, 'w') as decompressed:
    decompressed.write(decompressed_result)
    
    

