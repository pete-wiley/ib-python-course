import os

""" Helper Functions """
""" reverse_string() takes in a string as an argument and returns a reversed version of it. """
def reverse_string(str):
    """
    Strip string of newlines, then convert string to list, then reverse list, then join list 
    back into a string and return. 
    """
    stripped_str = str.strip('\n')
    str_list = list(stripped_str)
    reversed_list = reversed(str_list)
    reversed_str = f'{"".join(reversed_list)}'
    return reversed_str

""" delete_file_if_exists takes in a file path and deletes the file at the specified location if it exists. """
def delete_file_if_exists(file_path):
    """ If file specified by file_path exists, delete it. """
    if os.path.exists(file_path):
        os.remove(file_path)

"""
remove_newlines_from_end takes in a file path to a text file and removes trailing newlines from the end of the text file.
Would love feedback on a more efficient way to do this!
"""
def remove_newlines_from_end(file_path):
    """
    Open text file for reading, read data into a list, strip the last item in the list (last line of text file) of any newlines, and close file. 
    This is not efficient as it will load the entire content of the file into memory.
    """
    file_r = open(file_path, 'r')
    file_lines = file_r.readlines()
    file_lines[-1] = file_lines[-1].strip('\n')
    file_r.close()

    """
    Open text file for writing, write modified data back into the file, and close file.
    I think this could be done sooner in module_2() when its output file is already open for write, but it seems like the file needs to be closed first 
    for needed data to be saved to it.
    """
    file_w = open(file_path, 'w')
    file_w.writelines(file_lines)
    file_w.close()



""" Lab Deliverables """
"""
Module 1:
module_1() reads random.txt line by line using iteration, then writes each line to a new file called new_random.txt
"""
def module_1():
    """
    read_path is the path to the file we will be reading data from.
    output_path is the path to the file we will be writing results to.
    """
    read_path = './assets/random.txt'
    output_path = './output/new_random.txt'

    """ Check if output file exists. If it does, delete it so we can start from scratch. """
    delete_file_if_exists(output_path)

    """ Variable 'output' is the text file we are writing to. Use mode 'w' to enable write. """
    output = open(output_path, 'w')

    """
    Using the 'with' keyword ensures that the random.txt file is properly closed after iteration.
    Iterate over each line in random.txt and write line to output.
    """
    with open(read_path) as random:
        for line in random:
            output.write(line)

    """ Close output file. """
    output.close()

module_1()


"""
Module 2:
module_2() reads names.txt line by line using iteration, reverses each line, and writes reversed line to a new file called new_names.txt
"""
def module_2():
    """
    read_path is the path to the file we will be reading data from.
    output_path is the path to the file we will be writing results to.
    """
    read_path = './assets/names.txt'
    output_path = './output/new_names.txt'

    """ Check if output file exists. If it does, delete it so we can start from scratch. """
    delete_file_if_exists(output_path)

    """ Variable 'output' is the text file we are writing to. Using mode 'w' will create file if it doesn't exist. """
    output = open(output_path, 'w')

    """
    Using the 'with' keyword ensures that the random.txt file is properly closed after iteration.
    Iterate over each line in names.txt. 
    For each line, reverse it, add a newline, then write reversed line to output.
    """
    with open(read_path) as names:
        for name in names:
            output.write(f'{reverse_string(name)}\n')

    """ Close output file. """
    output.close()

    """ Remove trailing whitespace from end of text file. Would love feedback on a more efficient way to do this! """
    remove_newlines_from_end(output_path)

module_2()