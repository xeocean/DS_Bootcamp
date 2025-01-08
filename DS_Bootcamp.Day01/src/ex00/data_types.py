def data_types():
    integer = 21
    string = "Hello world!"
    floating = 3.14
    boolean = True
    my_list = [1, 0]
    my_dict = {1: "0"}
    my_tuple = (1, 0)
    my_set = {1, 0}

    types = [
        type(integer), type(string), type(floating), type(boolean),
        type(my_list), type(my_dict), type(my_tuple), type(my_set)
    ]

    type_names = [t.__name__ for t in types]

    print(f"[{', '.join(type_names)}]")


if __name__ == '__main__':
    data_types()
