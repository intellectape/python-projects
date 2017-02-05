# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, C, D):
    # write your code in Python 2.7
    
    try:
        list_numbers = [A, B, C, D]
        list_numbers.sort()
        # String for returning the value.
        string = ""
        # Adding value of maximum hours in the format in the string
        string += str(max(filter(lambda x: x <= 2, list_numbers)))
        list_numbers.pop(list_numbers.index(max(filter(lambda x: x <= 2, list_numbers))))
        if string[0] == '2':
            string += str(max(filter(lambda x: x <= 3, list_numbers)))
            list_numbers.pop(list_numbers.index(max(filter(lambda x: x <= 3, list_numbers))))
        else:
            string += str(max(filter(lambda x: x <= 9, list_numbers)))
            list_numbers.pop(list_numbers.index(max(filter(lambda x: x <= 9, list_numbers))))
        string += ":"
        # Adding value of maximum minutes in the format in the string
        string += str(max(filter(lambda x: x <= 5, list_numbers)))
        list_numbers.pop(list_numbers.index(max(filter(lambda x: x <= 5, list_numbers))))
        string += str(max(filter(lambda x: x <= 9, list_numbers)))
        return string     
    except ValueError:
        return "NOT POSSIBLE"
    
