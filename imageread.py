filename = input("Enter file name: ")
# filename = "OUTPUT.BMP"

infile = open(filename, "rb")

raw_bytes = infile.read()
file_bytes = bytearray(raw_bytes)

modified_offset = int.from_bytes(file_bytes[0xA:0xD], "little")
original_offset = int.from_bytes(file_bytes[modified_offset - 4:modified_offset], "little")

# print(f"Modified Offset: {modified_offset} - Original: {original_offset}")

message_bytes = file_bytes[original_offset:modified_offset - 4]
message = str(message_bytes, "ascii")

print(f"Message: {message}")
