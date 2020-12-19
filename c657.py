# while True:
#     try:
#         a = input()
#         count = 0
#         max_count = 0
#         max_char = ''
#         front = a[0]
#         for i in a:
#             if front != i:
#                 count = 1
#             else:
#                 count += 1
#                 if count > max_count:
#                     max_count = count
#                     max_char = i
#             front = i
#         print(max_char, max_count)
#     except:
#         break


while True:
    try:
        x = input() + '1'
        count = 1
        maximum = 0
        maximumalphabet = ''
        for i in range(len(x) - 1):
            if x[i] == x[i+1]:
                count += 1
            else:
                if maximum < count:
                    maximum = count
                    maximumalphabet = x[i]
                    count = 1
                    print(maximumalphabet, maximum)
    except:
        break

