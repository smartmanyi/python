
def drop_first_last(list):
    first, *middle, last = list
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([14, 12, 13, 15, 17, 18, 19])
drop_first_last([15, 14, 12, 13, 15, 17, 18, 16, 15, 1])
