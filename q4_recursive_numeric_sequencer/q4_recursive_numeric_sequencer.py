def recursive_numeric_sequencer(num, max_num, max_num_cnt):
    if num == 0:
        print(f' The max num is: {max_num} and it appears: {max_num_cnt} times')
        return 1
    if num == max_num:
        max_num_cnt += 1
    if num > max_num:
        max_num = num
    recursive_numeric_sequencer(int(input('Enter num, (to stop enter : 0): ')), max_num, max_num_cnt)


recursive_numeric_sequencer(int(input('Enter num, (to stop enter : 0): ')), 0, 1)
