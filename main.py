import time
import sort_algorithm
import random

if __name__ == '__main__':
    list_size = 8
    list = [random.randint(0, list_size * 2) for _ in range(list_size)]

    # Calculs, performances
    swapped_list = list.copy()
    sort_algorithm.swap(swapped_list, 0, 1)

    # Affichage des résultats
    print(f"Liste non triée : {list}")
    print(f"Swap des deux premiers éléments : {swapped_list} \n")

    start_time = time.time()
    insertion_list = sort_algorithm.insertion_sort(list.copy())
    end_time = time.time()
    print(f"Insertion : {insertion_list}")
    print(f"Time : {end_time-start_time}\n")


    start_time = time.time()
    selection_list = sort_algorithm.selection_sort(list.copy())
    end_time = time.time()
    print(f"Selection : {selection_list}")
    print(f"Time : {end_time-start_time} \n")

    start_time = time.time()
    bubble_list = sort_algorithm.bubble_sort(list.copy())
    end_time = time.time()
    print(f"Bubble : {bubble_list}")
    print(f"Time : {end_time-start_time} \n")

    start_time = time.time()
    shell_list = sort_algorithm.shell_sort(list.copy())
    end_time = time.time()
    print(f"Shell : {shell_list}")
    print(f"Time : {end_time-start_time} \n")

    # heap_list = sort_algorithm.heap_sort(list.copy())
    # print("Heap")
    # print(heap_list)
