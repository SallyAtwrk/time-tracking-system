c = False
while c is False:
    a = input('test me')
    if a.isdigit():
        if len(a) == 6:
            if int(a[0:2]) in range(0,24):
                if int(a[2:4]) in range(0,60):
                    if int(a[4:6]) in range(0,60):
                        print('Congratulation')
                        c = True
                    else:
                        print('Try again boy')
                else:
                    print('Try again boy')
            else:
                print('Try again boy')
        else:
            print('Try again boy')
    else:
        print('Try again boy')