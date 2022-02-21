def mid(middle):
    if len(middle)%2 == 0:
        print('""')
    else:
        return middle[(len(middle)-1)//2:(len(middle)+2)//2]

print(mid("baayukjgjh"))