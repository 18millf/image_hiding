FILE_HEADER_SIZE = 12

##message = input("Message to hide: ")
message = "A SUPER SECRET MESSAGE"

infile = open("LAND2.BMP", "rb")
raw_bytes = infile.read()
bytes = bytearray(raw_bytes)

bin_message = bytearray(message, 'ascii')

# Signature 0-1
# File Size 2-3
# Reserved 4-7
# Data Offset 8-B
data_offset = int.from_bytes(bytes[8:11], "big")
print(data_offset)

new_offset = data_offset + len(message) + 4 # extra  bytes required for original offset
new_offset_bytes = bytearray(new_offset, "big")

bytes[8] = new_offset_bytes[0]
bytes[9] = new_offset_bytes[1]
bytes[10] = new_offset_bytes[2]
bytes[10] = new_offset_bytes[3]

