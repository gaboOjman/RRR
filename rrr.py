def int_to_byte(num):
    byte = ""
    for i in range(7,-1,-1):
        if num >= pow(2,i):
            byte += "1"
            num -= pow(2,i)
        else:
            byte += "0"
    return byte

def dec_to_bin(dec):
    bin = ""
    for i in range(31,-1,-1):
        if dec >= pow(2,i):
            bin += "1"
            dec -= pow(2,i)
        else:
            bin += "0"
    return bin

def bin_to_dec(bin):
    dec = 0
    for i in range(len(bin)):
        if bin[i] == "1":
            dec += pow(2,len(bin)-i-1)
    return dec

def ip_to_bin(ip):
    lst = ip.split('.')
    bin_ip = ""
    for i in range(4):
        bin_ip += int_to_byte(int(lst[i]))
    return bin_ip

def bin_to_ip(bin):
    ip = [bin_to_dec(bin[i:i+8]) for i in range(0,32,8)]
    return ip


def segments(ip_init,ip_end):
    Segments = [] # [origin,dest,wildcard]
    ip_init = ip_to_bin(ip_init)
    ip_end = ip_to_bin(ip_end)
    ip_next_end = ip_init

    while True:
        Step = [bin_to_ip(ip_init),0,0]
        for i in range(len(ip_init)):
            check = list(ip_init)
            check[len(ip_init)-i-1] = "1"
            check = "".join(check)
            
            if bin_to_dec(check) > bin_to_dec(ip_end) or ip_init[len(ip_init)-i-1] == "1":
                wc = "".join(["0" for o in range(32-i)]) + "".join(["1" for o in range(i)])
                break
            else:
                ip_init = check

        ip_next_end = dec_to_bin(bin_to_dec(ip_init) + 1)

        Step[1] = bin_to_ip(ip_init)
        Step[2] = bin_to_ip(wc)
        if ip_init > ip_end:
            break
        ip_init = ip_next_end
        Segments.append(Step)
    return Segments

origin_ip = input("Ingresá la ip de origen (ej: 10.48.0.0): ")
destination_ip = input("Ingresá la ip de destino (ej: 10.179.255.255): ")      
    
for s in (seg:=segments(origin_ip,destination_ip)):
    print(f"Segmento {seg.index(s)+1}: \n   IP origen: {'.'.join(map(str, s[0]))}\n   IP destino: {'.'.join(map(str, s[1]))}\n   Wildcard: {'.'.join(map(str, s[2]))}")

