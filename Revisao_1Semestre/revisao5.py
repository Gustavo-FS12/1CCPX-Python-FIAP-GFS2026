for i in range (2 , 2000):
    primo = True
    for j in range (2, i):
        if i % j == 0:
            primo = False
            break

    if primo == True:
        print(i)