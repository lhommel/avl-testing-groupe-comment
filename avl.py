from todo import Todo


def createList():
    return []

def addToList(list, task):
    if isinstance(task, Todo):
        if len(filterByDate(filterByName(list, task.nom), task.date)) == 0:
            list.append(task)
            return True
        return False
    return False

def delElem(list, elem):
    if elem not in list:
        raise Exception("L'élément n'est pas présent dans la liste")
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

def filterByName(list, name):
    res = []
    for t in list:
        if t.nom == name:
            res.append(t)
    return res

def numberOfOcc(list, name):
    return len(filterByName(list, name))


def filterByDate(list, date):
    res = []
    for t in list:
        if t.date == date:
            res.append(t)
    return res

def filterByEtat(list, etat):
    res = []
    for t in list:
        if t.etat == etat:
            res.append(t)
    return res

def orderByPriority(list):
    list.sort(reverse=True, key=lambda t: t.priorite)

def readCSVFile(fileName):
    if fileName.endswith('.csv'):
        f = open(fileName, "r")
        r = f.read()
        f.close()
        return r
    raise Exception("L'extension n'est pas en .csv")


def parseToDoList(string):
    l = createList()
    for t in string.splitlines():
        var = t.split(", ")
        if len(var) != 4:
            raise Exception("Le format n'est pas correct, il n'y a pas 3 colonnes")
        todo = Todo(var[0], var[1], var[2])
        if var[3] == "FAIT":
            todo.fait()
        addToList(l, todo)
    return l


def writeToCSVFile(fileName, list):
    f = open(fileName, "w")
    f.write('\n'.join(map(str, list)))
    f.close()
    







def main():
    
    todoList = createList()
    addToList(todoList, Todo('task', '10/10/22'))
    addToList(todoList, Todo('task2', '10/10/22', 2))
    #print(isInList(todoList, 'task'))
    #delElem(todoList, 'task')
    #print(lenList(todoList))
    #print(numberOfOcc(todoList, 'task'))
    #print(todoList)
    #clearList(todoList)
    #print(isInList(todoList, 'task'))
    #print(todoList)
    
    writeToCSVFile("fichiers.csv",todoList)
    todoList2 = parseToDoList(readCSVFile("fichiers.csv"))
    print(str(todoList2[1]))
    
    print(todoList[0])

    orderByPriority(todoList)
    
    print(todoList[0])
    


if __name__ == '__main__':
    main()
