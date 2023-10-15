FILE_HEADER_SIZE = 12

message = input("Message to hide: ")
# message = "A SUPER SECRET MESSAGE"

infile = open("LAND2.BMP", "rb")
raw_bytes = infile.read()
file_bytes = bytearray(raw_bytes)

bin_message = bytearray(message, 'ascii')

# Signature 0-1
# File Size 2-3
# Reserved 4-7
# Data Offset 8-B
data_offset = int.from_bytes(file_bytes[0xA:0xD], "little")
print(data_offset)

print(len(file_bytes))

new_offset = data_offset + len(message) + 4  # extra  bytes required for original offset
print(new_offset)

new_offset_bytes = new_offset.to_bytes(4, "little")

old_bytes = file_bytes

file_bytes[0xA] = new_offset_bytes[0]
file_bytes[0xB] = new_offset_bytes[1]
file_bytes[0xC] = new_offset_bytes[2]
file_bytes[0xD] = new_offset_bytes[3]

bin_message.extend(data_offset.to_bytes(4, "little"))

i = data_offset
while i != new_offset:
    file_bytes.insert(i, bin_message[i - data_offset])
    print(f"Inserted {bin_message[i - data_offset]} at {i}")
    i = i + 1

print(len(file_bytes))

infile.close()

outfile = open("OUTPUT.BMP", "wb")
outfile.write(file_bytes)
outfile.close()
