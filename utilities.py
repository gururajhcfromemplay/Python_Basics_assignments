def list_average(list1):
    if list1.count(0) == len(list1):
        return 0
    elif len(list1) == 0:
        return 0
    else:
        return (sum(list1)/len(list1))   