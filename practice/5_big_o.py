# What is it?

# Big-O Notation describes the worst-case complexity, in time and space required, of an algorithm or data structure, described in terms of the growth of the input. An example is simpler.

# This data structure:

a_list = [1, 2, 3, 4, 5]

# has n potential size. Big-O doesn't describe what it is right now, but what the potential complexity could be if the input - n - grew very large (asymptotic growth - toward infinity). So for an array like above, the size complexity is O(n) -> as n grows, the size of the array grows in direct relation to n.

# This method:

a_list.sort()

# has O(n * log(n)) time (on average and at worst). Different sorts have different tradeoffs - some take more space (like this one - Timsort - takes O(n)), while some take more time (like Bubble Sort, which is potentially O(n^2) but doesn't take extra space). This - http://www.sorting-algorithms.com/ - is a great breakdown of sorting algos.

# Important to remember:

# Big O is worst-case time and is generally the practical use case of complexity analysis. There's also Big Theta - upper and lower bound - and Big Omega - lower bound - but they're much less practical except for specific cases.

# Big O is mathematically computed by getting some kind of equation to describe the runtime or space complexity of a particular structure or algorithm. For example, an algorithm might be described as taking x^2 + 3x + 5 time. But you'd say that takes O(x^2) time, because as you grow the input asymptotically, only the x^2 matters.

# Great article about misconceptions: http://ssp.impulsetrain.com/big-o.html