N = int(input())

def opcode(opcoder):
    if opcoder == 'ADD':
        return '0000'
    elif opcoder == 'SUB':
        return '0001'
    elif opcoder == 'MOV':
        return '0010'
    elif opcoder == 'AND':
        return '0011'
    elif opcoder == 'OR':
        return '0100'
    elif opcoder == 'NOT':
        return '0101'
    elif opcoder == 'MULT':
        return '0110'
    elif opcoder == 'LSFTL':
        return '0111'
    elif opcoder == 'LSFTR':
        return '1000'
    elif opcoder == 'ASFTR':
        return '1001'
    elif opcoder == 'RL':
        return '1010'
    elif opcoder == 'RR':
        return '1011'

for _ in range(N):
    result = ''
    opcoder, D, A, B = map(str, input().split())
    if opcoder[-1] == 'C':
        result += opcode(opcoder[:-1]) + '10'
    else:
        result += opcode(opcoder) + '00'
    result += format(int(D), 'b').zfill(3)
    if opcode(opcoder) == '0010' or opcode(opcoder) == '0101':
        result += '000'
    else:
        result += format(int(A), 'b').zfill(3)
    if opcoder[-1] == 'C':
        result += format(int(B), 'b').zfill(4)
    else:
        result += format(int(B), 'b').zfill(3) + '0'
    print(result)
