from utilities import list_average


if __name__ == "__main__":
    print('Enter the elements of the list to find thier average : ')
    list1 = [x for x in input().split()]
    try:
        list2 = [float(x) for x in list1]
        avg = list_average(list2)
        print(avg)
    except:
        print('Enter only numbers')
    