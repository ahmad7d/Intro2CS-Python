image = [[[1, 2]]]
print(image[0][0])
print(image[0])
lst1 = []
for i in range(len(image[0][0])):
    lst2 = []
    for j in range(len(image[0])):
        lst3 = []
        for k in range(len(image)):
            lst3.append(image[k][j][i])
        lst2.append(lst3)
    lst1.append(lst2)

print(lst1)


# d1 = []
# for i in range(len(image)):
#     d2 = []
#     for j in range(len(image[i])):
#         d3 = []
#         for k in range(len(image[i][j])):
#             d3.append([])













for i in range(5):
    print(i)






