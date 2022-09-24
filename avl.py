


def createList():
    return []

def addToList(list, task):
    list.append(task)

def delElem(list, elem):
    if elem not in list:
        return "L'élément n'est pas présent dans la liste"
    else:
        list.remove(elem)

def clearList(list):
    list.clear()

def isInList(list, elem):
    return elem in list

def reverseList(list):
    list.reverse()

def lenList(list):
    return len(list)

def numberOfOcc(list,elem):
    return list.count(elem)


def readCSVFile(fileName):
    try:
        f = open(fileName, "r")
        r = f.read()
        f.close()
        return r
    except FileNotFoundError:
        print("Le fichier '%s' n'existe pas." %fileName)


def parseToDoList(string):
    l = createList()
    for t in string.splitlines():
        addToList(l, t)
    return l


def writeToCSVFile(fileName, list):
    f = open(fileName, "w")
    f.write('\n'.join(list))
    f.close()
    







def main():
    
    todoList = createList()
    addToList(todoList, 'task')
    addToList(todoList, 'task')
    #print(isInList(todoList, 'task'))
    #delElem(todoList, 'task')
    #print(lenList(todoList))
    #print(numberOfOcc(todoList, 'task'))
   #print(todoList)
    #clearList(todoList)
    #print(isInList(todoList, 'task'))
    #print(todoList)
    
    writeToCSVFile("fichiers.csv",todoList)
    readCSVFile("fichier.csv")
    


if __name__ == '__main__':
    main()
