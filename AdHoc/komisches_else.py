def check_list_for_even_element(l):
    for e in l:
        if e % 2 == 0:
            print("list contains an even number")
            break
    else:
        print("list does not contain an even number")

l1 = [1,3,5]
check_list_for_even_element(l1)

l2 = [1,2,5]
check_list_for_even_element(l2)


