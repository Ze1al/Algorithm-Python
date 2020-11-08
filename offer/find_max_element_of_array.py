# 找出数组中最大的元素

def find_max_element_of_array(array):
    for i in array[::-1]:
        if i < array[0]:
            array.insert(0, i)
            array.pop()
    print(array)
    return array[0]

array = [3, 4, 5, 1, 2]
print(find_max_element_of_array(array))