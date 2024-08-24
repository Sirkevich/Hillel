def read_data():
    data = None
    ...
    return data


def operate_data(data):
    res = None
    ...
    return res


def print_data(data):
    def prepare_data(data):
        res = None
        ...
        return res

    def cat_data(data):
        res = None
        ...
        return res

    def print_data(data):
        ...

    new_data = prepare_data(data)
    new_data = cat_data(new_data)
    print_data(new_data)


def input_data():
    ...


def pass_data(x, y):
    ...


def main():
    data = read_data()
    new_data = operate_data(data)
    print_data(new_data)
    choice = input_data()
    pass_data(choice, new_data)


main()
