def two_multiple(lst,target):
    num_dict = {}

    for idx,num in enumerate(lst):
        num_dict[num] = idx

    for idx,num in enumerate(lst):
        if target/num in num_dict and idx!=num_dict[target/num]:
            return [idx,num_dict[target/num]]


result = two_multiple([2,4,3],8)
print(result)