'''
Created on 12/09/2014

@author: lee
'''

def winner(con_a, con_b):
    
    if con_a == con_b:
        return 0
    
    if (con_a == 'scissors' and con_b == 'paper') \
        or (con_a == 'paper' and con_b == 'rock') \
        or (con_a == 'rock' and con_b == 'scissors'):
        return -1
    return 1

    

def main():
    contestants = []
    con_name = []
    name_id = {}
    for i in range(1, 65):
        c_str = open('contestants/contestant%02d' % i).readlines()
        contestants.append([w.strip() for w in c_str[1:]])
        con_name.append(c_str[0])
        name_id[c_str[0]] = i - 1
    
    print contestants
    
    play0 = 0
    play1 = 0
    
    bit_out = []
    
    while len(contestants) > 1:
        
        result = 0
        while result == 0:
            result = winner(contestants[0][play0], contestants[1][play1])
            play0 += 1
            play1 += 1
        if result == -1:
            print con_name[1]
            bit_out.append(name_id[con_name[1]])
            contestants.pop(1)
            con_name.pop(1)
            play1 = 0 #missing line of code, would have got answer
            
        else:
            print con_name[0]
            bit_out.append(name_id[con_name[0]])
            contestants.pop(0)
            con_name.pop(0)
            play0 = play1
            play1 = 0
    
    print con_name[0]
    print ''.join(str(bit_out))



if __name__ == '__main__':
    main()