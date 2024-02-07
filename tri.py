#
#
#
# def tri_nathalie(list):
#     index = 0
#     ordered_list = []
#     list_size = len(list)
#
#     while list_size > len(ordered_list):
#         min_number = list[0]
#         for i in range(len(list)):
#             if list[i] <= min_number:
#                 min_number = list[i]
#                 index = i
#         list.pop(index)
#         ordered_list.append(min_number)
#
#     return ordered_list
#
# def tri_insertion(list):
#     size = len(list)
#     for i in range(1,len(list)):
#         temp = list[i]
#         j = i
#         while j > 0 and list[j-1] > temp:
#             swap = ( list[j-1], list[j])
#             list[j],list[j - 1] = swap[0],swap[1]
#             j=j-1
#         list[j]= temp
#
#     return list
#
# def tri_selection(list):
#     for i in range(len(list)):
#         min = i
#         for j in range(i+1, len(list)):
#             if list[j] < list[min]:
#                 min = j
#         swap = (list[i], list[min])
#         list[i], list[min] = swap[1], swap[0]
#
#     return list
#
# def tri_bulles(list):
#     passage = 0
#     permut = True
#     while permut:
#         permut = False
#         for i in range(len(list)-1):
#             if list[i] > list[i+1]:
#                 swap = (list[i], list[i+1])
#                 list[i], list[i+1] = swap[1], swap[0]
#                 permut = True
#         passage = passage + 1
#
#     return list
#
# def tri_shell(list):
#     new_list = []
#     longueur = len(list)
#     espacements = new_list
#     e = 0
#     while e < longueur:
#         e = (3*e+1)
#         new_list.append(e)
#
#     for i in range(len(new_list)-1):
#         valeur = list[i]
#         j=i
#         while j> e-1 and list[j-e] > valeur:
#             list[j] = list[j-e]
#             j=j-e
#         list[j] = valeur
#
#     return new_list
#