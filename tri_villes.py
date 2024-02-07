from tkinter import *
from tkinter import filedialog
import csv
import sort_algorithm
from geopy.distance import geodesic


class Ville:
    def __init__(self, nom_commune, codes_postaux, latitude, longitude, dist, distanceFromGrenoble):
        self.nom_commune = nom_commune
        self.codes_postaux = codes_postaux
        self.latitude = latitude
        self.longitude = longitude
        self.dist = dist
        self.distanceFromGrenoble = distanceFromGrenoble


def loadFile():
    listVille.clear()
    filename = filedialog.askopenfilename(initialdir="./",
                                          title="Selection du Fichier",
                                          filetypes=(("Text files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    changeLabelFile("Fichier : " + filename)
    with open(filename, 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            data = row[0].split(";")
            try:
                ville = Ville(data[8], data[9], float(data[11]), float(data[12]), float(data[13]), 0)
                ville.distanceFromGrenoble = getDistanceFromGrenoble(ville)
                listVille.append(ville)
            except:
                continue


def getDistanceFromGrenoble(ville):
    grenoble_latitude = 45.166672
    grenoble_longitude = 5.71667

    origin = (grenoble_latitude, grenoble_longitude)
    destination = (ville.latitude, ville.longitude)

    return round(geodesic(origin, destination).kilometers, 2)


def isLess(listVille, i, j):
    if listVille[i].distanceFromGrenoble < listVille[j].distanceFromGrenoble:
        return True


def swap(listVille, i, j):
    listVille[i], listVille[j] = listVille[j], listVille[i]
    return True


def changeLabelFile(text):
    labelFileExplorer = Label(fenetre,
                              text=text,
                              width=120, height=4,
                              fg="black", background="#579BB1")
    labelFileExplorer.place(x=150, y=offset + 40)


def changeLabelButtonSubmit(text):
    buttonValidation['text'] = text
    buttonValidation.place(x=150, y=offset + 120)


def onSelectTypeTri(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        global typeTriSelection
        typeTriSelection = data
        changeLabelButtonSubmit("Lancement du {}".format(data))


def sort():
    # effacement de la liste affichée
    listVilleSortedBox.delete(0, END)
    listVilleSorted = listVille.copy()

    if typeTriSelection == "Tri par insertion":
        listVilleSorted = insertsort(listVilleSorted)
    elif typeTriSelection == "Tri par sélection":
        listVilleSorted = selectionsort(listVilleSorted)
    elif typeTriSelection == "Tri à bulles":
        listVilleSorted = bubblesort(listVilleSorted)
    elif typeTriSelection == "Tri de Shell":
        listVilleSorted = shellsort(listVilleSorted)
    elif typeTriSelection == "Tri par fusion":
        listVilleSorted = mergesort(listVilleSorted)
    elif typeTriSelection == "Tri par tas":
        listVilleSorted = heapsort(listVilleSorted)
    elif typeTriSelection == "Tri rapide":
        listVilleSorted = quicksort(listVilleSorted)

    for ville in range(len(listVilleSorted)):
        listVilleSortedBox.insert(END, listVilleSorted[ville].nom_commune + " - " + str(
            listVilleSorted[ville].distanceFromGrenoble))
        listVilleSortedBox.itemconfig(ville, fg="black")

    listVilleSortedBox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listVilleSortedBox.yview)


def insertsort(list):
    for i in range(1, len(list)):
        temp = list[i].distanceFromGrenoble
        j = i
        while j > 0 and list[j - 1].distanceFromGrenoble > temp:
            list[j], list[j - 1] = list[j - 1], list[j]
            j = j - 1
        list[j].distanceFromGrenoble = temp

    return list


def selectionsort(list):
    for i in range(len(list)):
        min = i
        for j in range(i + 1, len(list)):
            if list[j].distanceFromGrenoble < list[min].distanceFromGrenoble:
                min = j
        list[i], list[min] = list[min], list[i]

    return list


def bubblesort(list):
    passage = 0
    permut = True
    while permut:
        permut = False
        for i in range(len(list) - 1):
            if list[i].distanceFromGrenoble > list[i + 1].distanceFromGrenoble:
                list[i], list[i + 1] = list[i + 1], list[i]
                permut = True
        passage = passage + 1

    return list


def shellsort(list):
    espacements = []
    longueur = len(list)
    e = 0
    while e < longueur:
        e = (3 * e + 1)
        espacements.insert(0, e)

    for e in espacements:
        for i in range(longueur):
            valeur = list[i]
            j = i
            while j > e - 1 and list[j - e].distanceFromGrenoble > valeur.distanceFromGrenoble:
                list[j] = list[j - e]
                j = j - e
            list[j] = valeur

    return list


def mergesort(listVille):
    if len(listVille) > 1:
        mid = len(listVille) // 2
        sub_array1 = listVille[:mid]
        sub_array2 = listVille[mid:]

        mergesort(sub_array1)
        mergesort(sub_array2)

        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i].distanceFromGrenoble < sub_array2[j].distanceFromGrenoble:
                listVille[k] = sub_array1[i]
                i += 1
            else:
                listVille[k] = sub_array2[j]
                j += 1
            k += 1
        while i < len(sub_array1):
            listVille[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            listVille[k] = sub_array2[j]
            j += 1
            k += 1

        return listVille


def heapsort(listVille):
    print("implement me !")
    return listVille


def quicksort(listVille):
    print("implement me !")
    return listVille


# Creation de la fenêtre
fenetre = Tk()
width = 1000
height = 180
offset = 10
listVille = []
listTri = ["Tri par insertion",
           "Tri par sélection",
           "Tri à bulles",
           "Tri de Shell",
           "Tri par fusion",
           "Tri par tas",
           "Tri rapide"]

typeTriSelection = "Tri par insertion"

labelFileExplorer = Label()
canvas = Canvas(fenetre, width=width + 2 * offset,
                height=height + 2 * offset, bg='white')
buttonValidation = Button(command=sort)

list = Listbox(fenetre, width=20, height=len(listTri), selectmode="single")
list.place(x=offset, y=offset)
list.bind("<<ListboxSelect>>", onSelectTypeTri)

for typeTri in range(len(listTri)):
    list.insert(END, listTri[typeTri])
    list.itemconfig(typeTri, fg="black")

buttonFile = Button(
    fenetre, text="Importation du fichier", command=loadFile)
buttonFile.place(x=150, y=offset)

changeLabelButtonSubmit("Lancement du {}".format(typeTriSelection))

changeLabelFile("Aucun Fichier ...")

canvas.pack()

listVilleSortedBox = Listbox(
    fenetre, width=100, height=25, selectmode="single")
listVilleSortedBox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(fenetre, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)
fenetre.mainloop()
