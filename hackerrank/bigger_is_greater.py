def swap_last_in_order_letters(w):
    w = list(w)
    first_ind = len(w) - 2
    second_ind = len(w) - 1
    done = False
    
    while first_ind >= 0 and not done:
        if w[first_ind] >= w[second_ind]:
            first_ind -= 1
            second_ind -= 1
        else:
            w[first_ind], w[second_ind] = w[second_ind], w[first_ind]
            done = True
    
    if not done:
        res = 'no answer'
    else:
        res = ''.join(w)
    
    return res
    
def next_largest(w):
    if len(w) <= 1:
        res = 'no answer'
    else:
        res = swap_last_in_order_letters(w)

    return res
    
words = ['jpli']

for word in words:
    print next_largest(word) #== 'lijp'