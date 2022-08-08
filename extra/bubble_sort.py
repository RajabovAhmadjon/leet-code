old_list = [10, 75, 43, 15, 25, -4, 27]

def bubble_sort(my_list):
    last_index = len(my_list) - 1
    for i in range(0, last_index):
        for j in range(0, last_index - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                
    return my_list

print("Old List", old_list)
new_list = bubble_sort(old_list).copy()
print("New List", new_list)
