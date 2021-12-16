import time

def day16():
    start = time.time()

    with open('Day16_input.txt') as file:
        input_file = [line.strip() for line in file]

    testing = True
    if testing:
        input_file = 'D2FE28'
        #input_file = '36006F45291200'

    input_file = [letter for substring in input_file for letter in substring]

    bitmap = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
              '4': '0100', '5': '0101', '6': '0110', '7': '0111',
              '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
              'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    binary = []

    for letter in input_file:
        binary.extend(bitmap[letter])

    version = []

    while len(binary) > 0:
        length_packet = 0
        list_of_packet_contents = []

        # Retrieve and remove the packet version
        packetversion = ''.join(binary[:3])
        version.append(int(packetversion, 2))
        del binary[:3]
        length_packet += 3

        # Retrieve and remove the packet id
        packetid = int(''.join(binary[:3]), 2)
        del binary[:3]
        length_packet += 3

        # ID 4 : Literal value
        if packetid == 4:
            packet = []
            # If the next chunk is not the final chunk
            while binary[0] == '1':
                # Delete the prefix
                del binary[0]
                packet.append(binary[:4])
                del binary[:4]
                length_packet += 5
            # When its the last chunk, repeat this one more time
            del binary[0]
            packet.append(binary[:4])
            del binary[:4]
            length_packet += 5
            list_of_packet_contents.append(''.join([item for sublist in packet for item in sublist]))

        # Remove padding 0s
        while binary[0] == '0' and length_packet % 4 != 0:
            del binary[0]
            if binary == []:
                break
    print(list_of_packet_contents)

    print("The answer to part 1 is:", sum(version))

    end = time.time()

    print("The elapsed time is:", end-start)