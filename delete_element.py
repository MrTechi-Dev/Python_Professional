def del_duplicates(lista):
    w_duplicates = list(set(lista))
    return w_duplicates

def del_duplicates2(lista):
    new_list = []
    for x in lista:
        if not x in new_list:
            new_list.append(x)
    return new_list
    
def run():
    duplicates = [1, 2, 3, 3, 2, 1]
    print (del_duplicates(duplicates))
    print (del_duplicates2(duplicates))


if __name__ == "__main__":
    run()
