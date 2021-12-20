import time

def get_version(binary_list):
    version.append(''.join(binary_list[:3]))
    del binary_list[:3]
    return binary_list

def get_id(binary_list):
    id = int(''.join(binary_list[:3]), 2)
    del binary_list[:3]
    return binary_list, id

def interpret_literal(binary_list):
    unpacked, stop, bits_processed = [], False, 6

    # Interpret
    while not stop:
        if binary_list[0] == '0':
            stop = True
        del binary_list[0]
        for bit in range(4):
            unpacked.append(binary_list[bit])
        del binary_list[:4]
        bits_processed += 5

    # Remove tailing 0s
    if bits_processed % 4 != 0:
        del binary_list[:4 - bits_processed % 4]

    return binary_list, unpacked

def process_chunk(binary_list):
    binary_list = get_version(binary_list)
    binary_list, id = get_id(binary_list)
    if id == 4:
        binary_list, unpacked = interpret_literal(binary_list)
        packages.append(int(''.join(unpacked), 2))
    if id != 4:
        len_type_id = binary_list[0]
        del binary_list[0]
        if len_type_id == '1':
            num_subpackets = int(''.join(binary_list[:11]))
            del binary_list[:11]
            for i in range(num_subpackets):
                binary_list = process_chunk(binary_list)
        if len_type_id == '0':
            len_subpackets = int(''.join(binary_list[:15]))
            del binary_list[:15]
            counter = len(binary_list)
            while len(binary_list) != counter - len_subpackets:
                process_chunk(binary_list)

    return binary_list

def day16():
    start = time.time()

    testing = True
    if testing:
        input_file = "D2FE28" # Example one
        input_file = "38006F45291200" # Example two

    bitmap = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
              '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
              'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    binary = []
    for letter in input_file:
        binary.extend(bitmap[letter])

    global version
    version = []
    global packages
    packages = []

    print(process_chunk(binary))

    print(packages)

    print("The answer to part 1 is:")

    end = time.time()

    print("The elapsed time is:", end-start)