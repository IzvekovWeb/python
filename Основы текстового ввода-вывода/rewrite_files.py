def write_files():
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
    for i, line in enumerate(input_file, 1):
        output_file.write(f"{i}) {line}")
    input_file.close()
    output_file.close()


def write_files_safe():
    ''' Использовать фалу безопаснее с помощью менеджера контекста with

    Даже в случае возникновения ошибки в телде блока, файл будет закрыт
    '''
    with open("input.txt", "r") as input_file:
        with open("output.txt", "w") as output_file:
            for i, line in enumerate(input_file, 1):
                output_file.write(
                    f"{i}) {line}"
                )