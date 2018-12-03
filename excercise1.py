#program preverja, katere stevilke med 2000 in 3200 so deljive s 5 in se mnozi s 7
def deljivo_s_5_ne_s_7():
    all_nums = []
    for num in range(2000, 3201):
        if num % 5 == 0 and num % 7 != 0:
            all_nums.append(num)
    all_nums = map(str, all_nums)
    print ", ".join(all_nums)
    print len(all_nums)


if __name__ == '__main__':
    deljivo_s_5_ne_s_7()