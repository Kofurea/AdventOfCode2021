def day3b():
    '''

    '''
    with open('Day03_input.txt') as f:
        lines = f.readlines()
    commands = [i.rstrip() for i in lines]

    N = 12 #the length of the bits

    oxygen_bin = ''
    for i in range(N):
        total = 0
        N_working = 0
        for j in commands:
            if i==0:
                total += int(j[i])
                N_working += 1
            else:
                if j[:i] == oxygen_bin:
                    total += int(j[i])
                    N_working += 1
        if total/N_working >= 0.5:
            oxygen_bin += '1'
        else:
            oxygen_bin += '0'

    co2_bin = ''
    for i in range(N):
        total = 0
        N_working = 0
        for j in commands:
            if i == 0:
                total += int(j[i])
                N_working += 1
            else:
                if j[:i] == co2_bin:
                    total += int(j[i])
                    N_working += 1
                    j_end = j
        if N_working == 1:
            break
        if total / N_working >= 0.5:
            co2_bin += '0'
        else:
            co2_bin += '1'

    print('\nDay3b\n--------')
    print('The life support rating is: ',int(oxygen_bin,2)*int(j_end,2))

day3b()