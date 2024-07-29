a = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{2, 'Urban', ('Urban2', 35)}])
]
def summator(a):
    if not a:
        return 0

    first_element = a[0]

    if isinstance(first_element, set):
        first_element = list(first_element)

    summa = summator(a[1:])

    if isinstance(first_element, (int, float)):
        return first_element + summa
    if isinstance(first_element, str):
        return len(first_element) + summa
    if isinstance(first_element, list):
        summa = summa + summator(first_element)
        return summa
    if isinstance(first_element, tuple):
        summa = summa + summator(first_element)
        return summa
    if isinstance(first_element, dict):
        for key, value in (first_element.items()):
            if isinstance(key, str):
                summa += len(key)
            if isinstance(key, int):
                summa += key
            if isinstance(value, str):
                summa += len(value)
            if isinstance(value, int):
                summa += value
        return summa
res = summator(a)
print(res)