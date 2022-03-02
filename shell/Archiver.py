byte_arr = [65,66,67,68]
some_bytes = bytearray(byte_arr)

some_bytes.append(33)

immutable_bytes=bytes(some_bytes)

with open("my_file.txt", "wb")as binary_file:
    binary_file.write(immutable_bytes)
#________________________________________________
inp_string = "{b:05d}"
bytes_encode = inp_string.encode()
print(type(bytes_encode))


decoded_string = bytes_encode.decode()
print(type(decoded_string))
print(decoded_string)

#--------------------------------------------------
str = "345"
mybytes = str.encode('utf-8')
print(mybytes)
myint = int.from_bytes(mybytes,'little')
print(myint)

decodeBytes = myint.to_bytes((myint.bit_length()+7)//8,'little')
print(decodeBytes)