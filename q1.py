'''
Created on 12/09/2014

@author: lee
'''

def main():
    
    cryp = '''QUEENS EUROS NINNIES SNEEZE FOX SISSIES FUROR SNIFF FIX
FLUBBED CUCUMBER RENT SNIP CURRY SINEW WORKOUT LOCKUP Y
MUCK UP COMFY RD YUCKY ROCOCO UP PERK HOW X TOLD CROP M
DODO UM DEDUCE COMFY DUKEDOM RUMORED ROW HOT LUCKY UM D
M MINICISE Q EGG MUD DECOY MINED CENSOR A V LOUD DESCRY
RAISING KOPECK PIP RHINESPENBINGESNEEP ROAST O RABIESTO'''
    
    map_str = '''+---+----+
                        | A | 5C |
                        +---+----+
                        | B | 5F |
                        +---+----+
                        | C | 7C |
                        +---+----+
                        | D | 7C |
                        +---+----+
                        | E | 5F |
                        +---+----+
                        | F | 20 |
                        +---+----+
                        | G | 7C |
                        +---+----+
                        | H | 5C |
                        +---+----+
                        | I | 5F |
                        +---+----+
                        | J | 2F |
                        +---+----+
                        | K | 20 |
                        +---+----+
                        | L | 2F |
                        +---+----+
                        | M | 7C |
                        +---+----+
                        | N | 5F |
                        +---+----+
                        | O | 20 |
                        +---+----+
                        | P | 7C |
                        +---+----+
                        | Q | 20 |
                        +---+----+
                        | R | 20 |
                        +---+----+
                        | S | 5F |
                        +---+----+
                        | T | 2F |
                        +---+----+
                        | U | 20 |
                        +---+----+
                        | W | 5C |
                        +---+----+
                        | X | 20 |
                        +---+----+
                        | Y | 7C |
                        +---+----+
                        | Z | 20 |
                        +---+----+'''
    mapping = {}
    for line in map_str.split('\n'):
        if '+' not in line:
            line = line.strip()
            cha1 = line[2]
            cha2 = line[6:8]
            mapping[cha1] = cha2
    
    decode = []
    for l in cryp:
        if l in mapping:
            decode.append(chr(int(mapping[l], 16)))
        else:
            decode.append(l)

    print ''.join(decode)

if __name__ == '__main__':
    main()
