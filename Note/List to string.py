mylist = ['spam', 'ham', 'eggs']
print(' '.join(mylist))
#
print('\n'.join(mylist))
#
list_of_ints = [80080, 443, 8080, 8081]
print(str(list_of_ints).strip('[]'))
#
print(str(list_of_ints)[1:-1])

#數字的情況 需加上map轉成數字
print(' '.join(map(str, list_of_ints)))