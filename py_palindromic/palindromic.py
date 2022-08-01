"""PALINDROM by .badian"""
def get_longest_palindrome(inputs: str) -> str:
    """find palindrom"""
    result = ''
    r_inputs = inputs[::-1]
    for index, _num in enumerate(inputs, 1):
        if inputs[0:index] == inputs[:index][::-1] and index > len(result):
            result = inputs[0:index]
        else:
            continue
    for index, _num in enumerate(r_inputs, 1):
        if r_inputs[0:index] == r_inputs[:index][::-1] and index > len(result):
            result = r_inputs[0:index]
        else:
            continue
    return result
