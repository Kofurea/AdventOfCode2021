import time

def bin_to_int(binary_list):
    return int(''.join(binary_list),2)

def get_version_id(binary_list):
    if len(binary_list) < 6:
        raise ValueError
    version = bin_to_int(binary_list[:3])
    id = bin_to_int(binary_list[3:6])
    return version, id

def process_literal(binary_list):
    # The version and id bits are already removed
    packet_contents = []
    bits_processed = 0

    for index, number in enumerate(binary_list):
        packet_contents.append(''.join(binary_list[index+bits_processed+1:index+bits_processed+4]))
        bits_processed += 5
        if binary_list[index+bits_processed] == 0:
            break

    packet_contents = ''.join(packet_contents)

    return packet_contents, bits_processed

def process_operant():
    pass

def day16():
    start = time.time()

    with open('Day16_input.txt') as file:
        input_file = [line.strip() for line in file]

    testing = True
    if testing:
        input_file = 'D2FE28'
        #input_file = '38006F45291200'
        #input_file = 'EE00D40C823060'
        #input_file = '8A004A801A8002F478'

    input_file = [letter for substring in input_file for letter in substring]

    bitmap = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
              '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
              'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    binary = []
    for letter in input_file:
        binary.extend(bitmap[letter])

    # Part 1 answers
    version = []

    while binary != []:
        # Start processing the next chunk
        chunk_version, chunk_id = get_version_id(binary)
        del binary[:6]
        version.append(chunk_version)
        packet_content, bits = process_literal(binary)



    print("The answer to part 1 is:", sum(version), version)

    end = time.time()

    print("The elapsed time is:", end-start)