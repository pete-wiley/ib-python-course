# Lab 1

def extract_from_list(elements):
    """
    Implement a function to extract certain objects from this list. Test list is [[3,2,6], [4,9,3], [9,6,3]]

    What you will do: extract the 3 from the first list of numbers, the 3 from the second list of numbers, and the 6 from the last list of numbers.
    Yes this is a list of lists
    """
    """
    Return a list containing references to desired elements in passed-in list.
    """

    return [elements[0][0], elements[1][2], elements[2][1]]

print(f"extract_from_list([[3,2,6], [4,9,3], [9,6,3]]): {extract_from_list([[3,2,6], [4,9,3], [9,6,3]])}\n")

def count_e_in_string(string):
    """
    Write a function to go through a string and count the number of Es in the string. You must use iteration in this and also
    need to handle upper and lowercase letters

    Params: string(str), string to count the number of E's
    Returns: int, the number of E's in the string
    """
    """
    Instantiate a variable called e_count. This will hold the count of how many times the letter E, case-agnostic, is found in the passed-in string. Inital value is 0.
    Iterate over string. For each character in the string, make character uppercase and check to see if value is equal to "E". 
    If values are equal, increment e_count by 1.
    Once all characters are checked, return e_count.
    """

    e_count = 0

    for char in string:
        if char.upper() == "E":
            e_count = e_count + 1

    return e_count

print(f"count_e_in_string('How many uppercase + lowercase Es are in this string?'): {str(count_e_in_string('How many uppercase + lowercase Es are in this string?'))}\n")

def length_of_string(string):
    """
    Write a function to count the number of characters in  a string. You must use iteration to do this

    Params: string (str), string to count the length
    Returns: int, the length of the string
    """
    """
    Instantiate a variable called str_length. This variable will track the length of the string as it is iterated over. Initial value is 0.
    Iterate over string. For each character in the string, increment str_length by 1.
    Once each character in the string has been checked, return str_length.
    """

    str_length = 0

    for char in string:
        str_length = str_length + 1

    return str_length

print(f"length_of_string('This string is 33 characters long'): {str(length_of_string('This string is 33 characters long'))}\n")

def reverse_string(string):
    """
    Write a function to reverse a string. You must use iteration to do this. Hint: think about how objects enter a string and leave a string

    Params: string (str), string to reverse
    Returns: string, the reversed string
    """
    """
    Instantiate a variable called result. This will hold the value of the reversed string. Initial value is an empty string.
    This function utilizes the built in string reversed() function. 
    Returning reversed(string) would deliver correct results, but because it is required to use iteration, this function will iterate over reversed(string).
    For each character in reversed(string), append the character to result.
    Once each character has been checked, return result.
    """

    result = ""

    for char in reversed(string):
        result = f"{result}{char}"

    return result

print(f"reverse_string('Print this backwards (using iteration)!'): {reverse_string('Print this backwards (using iteration)!')}\n")

def concact_elements_in_list(elements):
    """
    Write a function to concact the elements in a list together. You can assume all the elements are of type string. Please be sure to indlude white space between each element.
    I recommend solving this before the next function so you understand how lists work in looping. You must use iteration for this

    Params: elements (list), list of strings
    Returns: string, the newly built string
    """
    """
    Instantiate a variable called result. This will hold the value of concatenated elements in the list. Initial value is an empty string.
    Iterate over the elements list. For each element in elements, append element to result.
    Once all elements have been checked, return result.
    """

    result = ""

    for element in elements:
        result = f"{result}{element}"

    return result

print(f"concact_elements_in_list(['hey, ', 'whats ', 'up?']): {concact_elements_in_list(['hey, ', 'whats ', 'up?'])}\n")

def sum_characters_in_list(elements):
    """
    Write a functuon to sum all the elements in a list. You can assume all the elements are of type int.

    Params: elements (list), list of integers
    Returns: int, the sum of all the integers
    """
    """
    Instantiate a variable called result. This will hold the value of the summed characters in the passed in list. Initial value is 0.
    Iterate over the elements list. For each element in elements, add its value to result.
    Once all elements have been checked, return result.
    """

    result = 0

    for element in elements:
        result = result + element

    return result

print(f"sum_characters_in_list([1, 2, 3, 4, 5]): {str(sum_characters_in_list([1, 2, 3, 4, 5]))}\n")