def begin_bloc(func):
    def wraper():
        print('Это стартовая часть.')
        func()
        print('Это заключительная часть.')

    return wraper


@begin_bloc
def insert_block():
    print('Это повторная вставка в наш декоратор.')


# insert_block()

# def insert_block():
#     print('Это вставка в наш декоратор.')
#
#
# start_decorators = begin_bloc(insert_block)
# start_decorators()
