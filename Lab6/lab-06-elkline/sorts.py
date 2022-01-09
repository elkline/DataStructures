import random
import time


def selection_sort(alist):
    count = 0
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            count += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return count


def insertion_sort(alist):
    swapsmade = 0
    checksmade = 0
    for f in range(len(alist)):
        value = alist[f]
        valueindex = f
        checksmade += 1
        # moving the value
        while valueindex > 0 and value < alist[valueindex - 1]:
            alist[valueindex] = alist[valueindex - 1]
            valueindex -= 1
            checksmade += 1
            swapsmade += 1  # Move inside the while loop
        alist[valueindex] = value
    return checksmade


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    # randoms = random.sample(range(1000000), 32000)
    # start_time = time.time()
    # comps = selection_sort(randoms)
    # stop_time = time.time()
    # print(comps, stop_time - start_time)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time()
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()
