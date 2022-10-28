"""
url = "http://sidechan.tonejc.de/PadOrc/112233445566778899AABBCC5F1C701D691C73953474644435223857473463CD93BCBBD91B371E60076501BE461A0E3D"

block0 = "112233445566778899AABBCC"
block1 = "5F1C701D691C739534746444"
block2 = "35223857473463CD93BCBBD9"
block3 = "1B371E60076501BE461A0E3D"
"""


import requests
from requests.exceptions import Timeout

#zw_erg = ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
zw_erg = []
erg = []
#hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
url = "http://sidechan.tonejc.de/PadOrc/"
bloecke = ['112233445566778899AABBCC', '5F1C701D691C739534746444', '35223857473463CD93BCBBD9', '1B371E60076501BE461A0E3D']
get_block = []
backup_block = ''




def main():
    block_index = 0
    for block in bloecke:
        print("Aktueller Block: ", block_index)
        backup_block = block
        #aktuellen Block in Bytes aufteilen
        for i in range(len(block)-2, -1, -2):
            get_block.append(block[i:i+2])

        b_index = 0
        for b in get_block:
            print("Aktuelles b: ", b)
            for i in range(0, i < b_index):
                #achtung: strings müssen zu hex konvertiert werden und umgekehrt
                get_block[i] = hex(int(zw_erg[i], 16) ^ (b_index+1))[2:]
                print(get_block)

            guess = 0
            while (True and guess < 256):
                b_strich = hex(guess)[2:]
                #if(guess < 16):
                #    b_strich = "0" + b_strich
                format_b_strich = hex(int(b_strich, 16))[2:]
                print("Länge von b_strich: ")
                print(len(format_b_strich))
                if(len(format_b_strich) == 1):
                    format_b_strich = '0' + format_b_strich
                req = request(b_index, format_b_strich, block_index)
                # timer start
                try:
                    status = requests.get(req, timeout = 3).status_code
                except Timeout:
                    print("Timeout expired")
                    guess -= 1

                if(status == 401):
                    print("----------------------Byte found!-----------------------------------")
                    break
                guess += 1
                status = 0
            
            
            zw_erg.append(format_b_strich)
            print("Zwischenergebnis:")
            print(zw_erg)
            z = int(b_strich, 16) ^ int(b, 16) ^ (b_index + 1)
            erg.insert(0, hex(z)[2:])
            print("Ergebnis:")
            print(erg)

            b_index += 1

        #remember: get_block am ende einer iteration leeren!
        get_block.clear()

        bloecke[block_index] = backup_block 
        block_index += 1

    for x in reversed(erg):
        print(x)



def request(b_index, b_strich, block_index):
    #print("Request called for b_strich =" + b_strich)
    b_string = ''
    get_block[b_index] = b_strich
    for b in reversed(get_block):
        b_string += b

    bloecke[block_index] = b_string
    my_req = url + bloecke[0] + bloecke[1] + bloecke[2] + bloecke[3]

    return my_req


if __name__=="__main__":
    main()

