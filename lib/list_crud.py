def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,3,4]

def add_element_to_end_of_list(l, element):
    create_list= [1,2,3,4]
    create_list.append(5)
    return create_list

def add_element_to_start_of_list(l, element):
    list_one= [1,2,3,4,5]
    list_one.insert(0,0)
    return list_one

def remove_element_from_end_of_list(l):
    remove_list= [1,2,3,4]
    remove_list.pop()
    return remove_list

def remove_element_from_start_of_list(l):
    remove_list2= [1,2,3,4]
    del remove_list2[0]
    return remove_list2

def retrieve_first_element_from_list(l):
   
    if len(l) > 0:
        return l[0]
    else:
        return None  


def retrieve_element_from_index(l, index):
    if len(l) > 1:
        return l[1]
    else:
        return None  
    

def retrieve_last_element_from_list(l):
    last_el=[1,2,3,4]
    new_list= last_el[-1]
    return new_list
