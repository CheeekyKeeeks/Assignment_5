
>>> def nested_sum(t):
...     total = 0
...     for nested in t:
...             total += sum(nested)
...     return total
...
>>>
>>> t = [[1,2],[3],[4,5,6]]
>>> nested_sum(t)
21
>>>
