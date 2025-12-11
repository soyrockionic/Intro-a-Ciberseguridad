ips = [
    "85.78.76.80",
    "123.67.48.118",
    "51.114.84.95",
    "95.99.104.52",
    "110.78.101.124",
    "95.85.115.49",
    "110.103.95.68",
    "78.83.33.33",
    "125.192.180.219"
]

flag = ""
for ip in ips:
    for octet in ip.split('.'):
        if 32 <= int(octet) <= 126:  # solo caracteres imprimibles
            flag += chr(int(octet))
print(flag)