def create_an_empty_list():
    some_list =[]
    return some_list


def create_a_list():
    i = 0
    list = []
    while i < 4:
        list.append(i)
        i += 1
    return list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l


def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    return None

def remove_element_from_start_of_list(l):
    return None

def retrieve_first_element_from_list(l):
    return None

def retrieve_element_from_index(l, index):
    return None

def retrieve_last_element_from_list(l):
    return None
