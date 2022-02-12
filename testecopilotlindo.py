def expanded_form(num):
    num_str = str(num)
    num_list = []
    for i in range(len(num_str)):
        if num_str[i] != '0':
            num_list.append(num_str[i] + '0' * (len(num_str) - i - 1))
    return ' + '.join(num_list)

print(expanded_form(12))

