def str_split(input_str, delimiter1, delimiter2):
    parts = input_str.find(delimiter1)
    parts2 = input_str.find(delimiter2)
    result = input_str[parts +1 :parts2]
    return result
