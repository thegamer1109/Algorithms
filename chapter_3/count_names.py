def count_names(list_of_lists, target_name):
    count = 0
    
    for n in list_of_lists:
        for m in n:
            if m == target_name:
                count += 1
    
    return count