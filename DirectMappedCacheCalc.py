import math

class colors:
    HIGHLIGHT = '\033[93m'
    ENDC = '\033[0m'

if int(input('Mode: ')) == 1:
    cacheLines = int(input('No. Cache Lines: '))
    words = int(input('Words per Line: '))
    wordBytes = int(input('Bytes per Word: '))
    addressBus = int(input('Address Bus (bits): '))
    print('---------------------------')
    offset = int(math.log(words*wordBytes,2))
    index = int(math.log(cacheLines,2))
    tag = int(addressBus - index - offset)
    print(f'Offset (bits):         {offset}')
    print(f'Index (bits):          {index}')
    print(f'Tag (bits):            {tag}')
    print(f'Data in Cache (bytes): {cacheLines*words*wordBytes} or 2^{math.log(cacheLines*words*wordBytes,2)}')
else:
    addressBus = int(input('Address Bus (bits): '))
    offset = int(input('Offset: '))
    index = int(input('Index: '))
    tag = int(input('tag: '))
    cacheLines = 2**index


cache = []
for i in range(cacheLines):
    cache.append(None)

def printCache(data = -1):
    for no,i in enumerate(cache):
        if no == data:
            # print('this Ran')
            print(colors.HIGHLIGHT + f"Line {no}: [{hex(i[0])},{hex(i[1])}]" + bcolors.ENDC)
        elif i:
            print(f"Line {no}: [{hex(i[0])},{hex(i[1])}]")
        else:
            print(f"Line {no}: {i}")
    print()

while True:
    try:
        temp = str(bin(int(input('Input Memory Address: '),0)))[2:]
        if len(temp) < addressBus:
            temp1 = '0' * (addressBus-len(temp))
            binary = temp1 + temp
        else:
            binary = temp
        addressTag = binary[:tag]
        addressIndex = binary[tag:tag+index]
        addressOffset = binary[tag+index:]

        print(f'Address Binary: {binary} or {int(binary,2)}')
        print(f'Tag:            {addressTag} or {int(addressTag,2)}')
        print(f'Index:          {addressIndex} or {int(addressIndex,2)}')
        print(f'Offset:         {addressOffset} or {int(addressOffset,2)}')
        temp = int(addressIndex,2)
        if not cache[temp]:
            print('Miss')
            temp2 = int(binary,2)
            if offset == 0:               
                cache[temp] = [temp2-1,temp2]
            else:
                cache[temp] = [temp2-int(addressOffset,2),temp2]
        else:
            temp2 = int(binary,2)
            if temp2 >= cache[temp][0] and temp2 <= cache[temp][1]:
                print('Hit')
            else:
                print('Miss')
                cache[temp] = [temp2-int(addressOffset,2),temp2]
        printCache(temp)
    except Exception as e:
        print(e)
