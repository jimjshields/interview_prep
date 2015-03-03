test_input = ['AAAA', 'BBBBB', 'ABABABAB', 'BABABA', 'AAABBB']

def check_if_alternating(string):
    """Checks whether a string has alternating characters."""
    
    index = 0
    deletion_count = 0
    
    while index < len(string) - 1:
        start = string[index]
        next_c = string[index + 1]
        while next_c == start:
            deletion_count += 1
            index += 1
            if index < len(string) - 1:
                next_c = string[index + 1]
            else:
                break
        index += 1
    
    return deletion_count

for i in test_input:
    print check_if_alternating(i)