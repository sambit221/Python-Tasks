def A():
    # defined A for task 3.1
    import random
    NumList = ['9', '3', '1', '8', '7', '5', '4', '6', '2']
    # taken a random list of numbers
    NumList.sort()
    # sorted in accending order
    a = int(NumList[0])
    b = int(NumList[1])
    c = int(NumList[2])
    d = int(NumList[3])
    # after sorting tken 4 smallest values
    e = a * c
    if e < 0:
        print('no rectangle will be possible')
    # from those 4 values 2 will represent width and 2 will length
    # so i am taking smallest of each length and width (here it will be 'a' and 'c') to form possible rectangle
    else:
        print(e)


def c():
    # task3.3
    print("A team gets:- \n 2 points for a win \n 1 point for a tie \n points for a loss")
    # shown points tally

    x = input("Enter minimum points VSSUT needs to qualify for playoffs: ")
    a = int(x)
    # stored the amoount of points required by vssut to qualify in x variable and its int in a
    y = input("Enter number of remaining matches")
    b = int(y)
    # number of remaining matches stored in y and its int in b
    # if number of points required is even
    if (a % 2) == 0:
        c = int(a / 2)
        if b >= c:
            print("the minimum number of matches VSSUT requirs to win is:")
            print(c)
        if c > b:
            print("invalid input because VSSUT will definitely go into playoff if he wins all matches ")
    # if number of points required is odd
    if (a % 2) != 0:
        if b >= (a + 1):
            d = a - 1
            e = d / 2
            print("the minimum number of matches VSSUT requirs to win is:")
            print(e)
        if (a + 1) > b:
            print("invalid input because VSSUT will definitely go into playoff if he wins all matches ")


def d():
    # task 3.4
    print("movie list A B C D")

    # movie list
    def list():
        list = ['l1=2, r1=1', 'l2=4, r2=3', 'l3=3,r3=1', 'l4=1, r4=2']

    l = ['1', '2', '3', '4']
    r = ['1', '2', '3', '4']
    # length and ratings respective tally

    l.sort()
    r.sort()
    a = int(l[3])
    b = int(r[3])
    c = a * b
    # highest value of length is stored in a and of rating in b
    # c shows l*r in integer

    print('The movie to be watched have output:')
    print(c)
    # here is the output


def e():
    # task 3.5
    from array import *
    # imported all fxn of array
    arr = array('i', [])
    n = int(input("enter the length of array"))
    # taken length of array from user along with elements
    for i in range(n):
        x = int(input("enter the next value"))
        arr.append(x)
        while (n > 2):
            # if array contains more than 2 elements
            arr.sort()
            print('output')
            print(arr[0])
            arr.pop(0)
            n = n - 1
            break
    while (n <= 2):
        # if array contains exactly 2 elements
        arr.sort
        print('output')
        print(arr[0])


A()
c()
d()
e()