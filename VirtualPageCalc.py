import math

virtualAddressSize = int(input('Virtual Address Size (bits):       '))
addressPhysicalMemory = int(input('Address of Physical Memory (bits): '))
virtualPageSize = int(input('Virtual Page Size (KB):            '))*1024
virtualPageNumber = int(virtualAddressSize-math.log(virtualPageSize,2))
print('---------------------------')
print(f'Virtual Page Number (Bits): {virtualPageNumber}')
while True:
    print('---------------------------')
    temp = input('Virtual Address for Split: ')
    temp = str(bin(int(temp,0)))[2:]
    if len(temp) != virtualAddressSize:
        temp1 = '0' * (virtualAddressSize-len(temp))
        temp = temp1 + temp
    
    print(f"Address Given:        {hex(int(temp,2))} or {temp}")
    print(f"Virtual Page Number:  {hex(int(temp[0:virtualPageNumber],2))} or {temp[0:virtualPageNumber]}")
    print(f"Page Offset:          {hex(int(temp[virtualPageNumber:],2))} or {temp[virtualPageNumber:]}")

