with open('data.txt') as f:


    # for line in f:
        # print(line)
        # print(f.read())
        print(f.read(10))
        f.seek(0)
        print(f.read(10))
        print('Seeking Pointer \n')
        f.seek(20)
        print(f.read(10))