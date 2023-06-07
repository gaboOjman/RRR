origin_ip = '10.48.0.0'
destination_ip = '10.179.255.255'

def int_to_byte(num):
    byte = ""
    for i in range(7,-1,-1):
        if num >= pow(2,i):
            byte += "1"
            num -= pow(2,i)
        else:
            byte += "0"
    return byte

def ip_to_bin(ip):
    lst = ip.split('.')
    bin_ip = ""
    for i in range(4):
        bin_ip += int_to_byte(int(lst[i]))
    return bin_ip

def wildcards(ip_init,ip_end):
    ip_init = ip_to_bin(ip_init)
    ip_end = ip_to_bin(ip_end)
    ceros_iniciales = 0
    for i in range(32):
        if ip_init[i] == ip_end[i]:
            ceros_iniciales += 1
        else:
            break
    print(ip_init)
    print(ip_to_bin("10.63.255.255"))
    print(ip_to_bin("10.127.255.255"))
    print(ip_to_bin("10.159.255.255"))
    print(ip_to_bin("10.175.255.255"))
    print(ip_end)
    print(ceros_iniciales)

#wildcards(origin_ip,destination_ip)

print(ip_to_bin("10.0.0.0"))
print(ip_to_bin("10.127.255.255"))
print(ip_to_bin("10.159.255.255"))
print(ip_to_bin("10.175.255.255"))
print(ip_to_bin("10.179.255.255"))
