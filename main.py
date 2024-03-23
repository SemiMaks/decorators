from decorators import begin_bloc


@begin_bloc
def insert_new():
    print('Я вставка в импортированный блок.')


insert_new()
