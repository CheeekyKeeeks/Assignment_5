
>>> def cumsum(t):
...     total = 0
...     res = []
...     for x in t:
...             total += x
...             res.append(total)
...     return res
...
>>> t = [1,2,3,4,5,6]
>>> cumsum(t)
[1, 3, 6, 10, 15, 21]
>>>