# Algorithm
#Binary Search takes start and end of list and will divide it to 2, then it will compare middle element
#with searching element if it is higher/lower then middle it will move start position to middle and repeat action
#untill finding proper element

def binary_search(my_list, index_search, start, stop):
    if start > stop:
        return False, "Not found!"
    else:
        index_mid = (start + stop) // 2 #// returns integer of division
        if index_search == my_list[index_mid]:
            return index_mid
        elif index_search < my_list[index_mid]:
            return binary_search(my_list, index_search, start, index_mid - 1)
        else:
            return binary_search(my_list, index_search, index_mid + 1, stop)

my_list = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 81]
index_to_search = 23
print(binary_search(my_list, index_to_search, 0, len(my_list)))