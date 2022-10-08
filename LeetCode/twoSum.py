def two_sum(num_list,target):
    num_dict = {}
    for idx,num in enumerate(num_list):
        num_dict[num] = idx

    for idx,num in enumerate(num_list):
        if target-num in num_dict and idx!=num_dict[target-num]:
            return [idx,num_dict[target-num]]
            

index = two_sum([1,2,3,4],3) 
print(index)