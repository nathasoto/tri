# def swap(A, i, j):
#     A[i], A[j] = A[j], A[i]
#     return A
#
#
# def insertion_sort(list):
#     for i in range(1, len(list)):
#         temp = list[i]
#         j = i
#         while j > 0 and list[j - 1] > temp:
#             list[j], list[j - 1] = list[j - 1], list[j]
#             j = j - 1
#         list[j] = temp
#
#     return list
#
#
# def selection_sort(list):
#     for i in range(len(list)):
#         min = i
#         for j in range(i + 1, len(list)):
#             if list[j] < list[min]:
#                 min = j
#         swap = (list[i], list[min])
#         list[i], list[min] = list[min], list[i]
#
#     return list
#
#
# def bubble_sort(list):
#     passage = 0
#     permut = True
#     while permut:
#         permut = False
#         for i in range(len(list) - 1):
#             if list[i] > list[i + 1]:
#                 list[i], list[i + 1] = list[i + 1], list[i]
#                 permut = True
#         passage = passage + 1
#
#     return list
#
#
# def shell_sort(list):
#     espacements = []
#     longueur = len(list)
#     e = 0
#     while e < longueur:
#         e = (3 * e + 1)
#         espacements.insert(0,e)
#
#     for e in espacements:
#         for i in range(longueur):
#             valeur = list[i]
#             j = i
#             while j > e - 1 and list[j - e] > valeur:
#                 list[j] = list[j - e]
#                 j = j - e
#             list[j] = valeur
#
#     return list
#
#
# def heap_sort(inputarr, indexStart, indexEnd):
#     print("implement me")
