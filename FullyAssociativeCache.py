from math import inf
class colors:
    HIGHLIGHT = '\033[93m'
    ENDC = '\033[0m'

def printCache(data,cache):
        for no,i in enumerate(cache):
            if i and data.lower() == i[0].lower():
                print(colors.HIGHLIGHT + f"Line {no}: {i}" + colors.ENDC)
            else:
                print(f"Line {no}: {i}")
        print()
    

def FullyAssociativeCache():
    cacheLines = int(input('No. Cache Lines: '))
    print('---------------------------')
    cache = [None for i in range(cacheLines)]

    localGlobalCounter = 1
    while True:    
        try:
            temp = input('Enter Address: ')
            if temp.lower() == 'exit':
                return
            lowest_counter = [0,inf]
            flag = True
            
            for i in range(len(cache)):
                if cache[i] == None:
                    print('Miss')
                    cache[i] = [temp,localGlobalCounter]
                    localGlobalCounter +=1
                    flag = False
                    break
                elif cache[i][0].lower() == temp.lower():
                    print('Hit')
                    cache[i][1] = localGlobalCounter
                    localGlobalCounter +=1
                    flag = False
                    break
                elif lowest_counter[1] > cache[i][1]:
                    lowest_counter = [i,cache[i][1]]
            if flag:
                print('Miss')
                cache[lowest_counter[0]] = [temp,localGlobalCounter]
                localGlobalCounter +=1
            printCache(temp,cache)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    FullyAssociativeCache()
