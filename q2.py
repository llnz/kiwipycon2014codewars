'''
Created on 12/09/2014

@author: lee
'''
# coding: utf-8
from __future__ import unicode_literals

if __name__ == '__main__':
    value = u'111111100010101111111100000100000101000001101110101010001011101101110100000101011101101110100101101011101100000100111001000001111111101010101111111000000001010000000000111011111010111000100010010011111011101000011110110101011111011001010010111110100010000111111101001110111000000001100001100001111111101110100111101100000101010001110010101110101010101001100101110100001010001110101110101001011110001100000101011110000010111111101101011111111'
    offset = 0
    dalist = []
    value = value.replace(u'1', u"\u2B88")
    value = value.replace(u'0', u'\u')
    while offset < len(value):
        #dalist.append(chr(int(value[offset:offset + 8], 2)))
        print(value[offset:offset+21])
#         for char in value[offset:offset+21]:
#             print('<tr>')
#             if char == '0':
#                 print('<td class="white"></td>')
#             else:
#                 print('<td class="black"></td>')
        offset += 21
    #print ''.join(dalist)