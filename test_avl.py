import unittest
import random
import pytest
from pytest import list_of


import avl
from etat import Etat
from todo import Todo


class TestAvl(unittest.TestCase):
    def test_createList(self):
        self.assertIsNotNone(avl.createList())
        self.assertEqual([], avl.createList())

    def test_addToList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        self.assertEqual(True, avl.addToList(toDoList, todo1))
        self.assertEqual(1, len(toDoList))
        self.assertEqual([todo1], toDoList)
        todo2 = Todo("task2", "2")
        self.assertEqual(True, avl.addToList(toDoList, todo2))
        self.assertEqual(2, len(toDoList))
        self.assertEqual([todo1, todo2], toDoList)

    def test_addNotAToDoClass(self):
        toDoList = avl.createList()
        self.assertEqual(False, avl.addToList(toDoList, "notATodoClass"))

    def test_addToDoAlreadyInList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "01/01/01")
        todo1Dup = Todo("task1", "01/01/01")
        self.assertEqual(True, avl.addToList(toDoList, todo1))
        self.assertEqual(1, avl.lenList(toDoList))
        self.assertEqual(False, avl.addToList(toDoList, todo1Dup))
        self.assertEqual(1, avl.lenList(toDoList))

    def test_delElem(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task2", "2")
        avl.addToList(toDoList, todo2)
        self.assertEqual([todo1, todo2], toDoList)
        avl.delElem(toDoList, todo1)
        self.assertEqual([todo2], toDoList)
        avl.delElem(toDoList, todo2)
        self.assertEqual([], toDoList)
        

    def test_delElem_notInList(self):
        toDoList = avl.createList()
        self.assertRaises(Exception, lambda: avl.delElem(toDoList, 2))


    def test_clearList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task2", "2")
        avl.addToList(toDoList, todo2)
        todo3 = Todo("task3", "3")
        avl.addToList(toDoList, todo3)
        avl.clearList(toDoList)
        self.assertIsNotNone(toDoList)
        self.assertEqual([], toDoList)
        avl.clearList(toDoList)
        self.assertIsNotNone(toDoList)
        self.assertEqual([], toDoList)

    def test_isInList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        self.assertTrue(avl.isInList(toDoList, todo1))

    def test_isNotInList(self):
        toDoList = avl.createList()
        self.assertFalse(avl.isInList(toDoList, Todo("task1", "1")))

    def test_reverseList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task2", "2")
        avl.addToList(toDoList, todo2)
        todo3 = Todo("task3", "3")
        avl.addToList(toDoList, todo3)
        avl.reverseList(toDoList)
        self.assertEqual([todo3, todo2, todo1], toDoList)

    def test_reverseEmptyList(self):
        toDoList = avl.createList()
        avl.reverseList(toDoList)
        self.assertEqual([], toDoList)

    def test_reverseListOfOneElem(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        avl.reverseList(toDoList)
        self.assertEqual([todo1], toDoList)

    def test_lenList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task2", "2")
        avl.addToList(toDoList, todo2)
        todo3 = Todo("task3", "3")
        avl.addToList(toDoList, todo3)
        self.assertEqual(3, avl.lenList(toDoList))

    
    def test_lenEmptyList(self):
        toDoList = avl.createList()
        self.assertEqual(0, avl.lenList(toDoList))



    def test_numberOfOcc(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "01/01/01")
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task1", "02/01/01")
        avl.addToList(toDoList, todo2)
        self.assertEqual(2, avl.numberOfOcc(toDoList, "task1"))

    
    def test_numberOfOccEqualsZero(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        avl.addToList(toDoList, todo1)
        self.assertEqual(0, avl.numberOfOcc(toDoList, "task2"))


    def test_filterByName(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, Todo("task1", "1"))
        avl.addToList(toDoList, Todo("task2", "2"))
        self.assertEqual(1, len(avl.filterByName(toDoList, "task1")))

    def test_filterByNameManyInList(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, Todo("task1", "1"))
        avl.addToList(toDoList, Todo("task2", "2"))
        avl.addToList(toDoList, Todo("task2", "3"))
        avl.addToList(toDoList, Todo("task2", "4"))
        avl.addToList(toDoList, Todo("task3", "5"))
        self.assertEqual(3, len(avl.filterByName(toDoList, "task2")))

    def test_filterByNameNotInList(self):
        toDoList = avl.createList()
        self.assertEqual(0, len(avl.filterByName(toDoList, "task2")))

    def test_numberOfOccEmptyList(self):
        toDoList = avl.createList()
        self.assertEqual(0, avl.numberOfOcc(toDoList, "task2"))

    def test_filterByEtat(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, Todo("task1", "1"))
        todo2 = Todo("task2", "2")
        todo2.fait()
        avl.addToList(toDoList, todo2)
        self.assertEqual(1, len(avl.filterByEtat(toDoList, Etat.FAIT)))

    def test_filterByEtatChangeEtat(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task2", "2")
        todo2.fait()
        avl.addToList(toDoList, todo2)
        self.assertEqual(1, len(avl.filterByEtat(toDoList, Etat.FAIT)))
        todo1.fait()
        self.assertEqual(2, len(avl.filterByEtat(toDoList, Etat.FAIT)))

    def test_filterByEtatManyInList(self):
        toDoList = avl.createList()
        todo1 = Todo("task1", "1")
        todo1.fait()
        avl.addToList(toDoList, todo1)
        todo2 = Todo("task2", "2")
        avl.addToList(toDoList, todo2)
        todo3 = Todo("task3", "3")
        todo3.fait()
        avl.addToList(toDoList, todo3)
        todo4 = Todo("task4", "4")
        todo4.fait()
        avl.addToList(toDoList, todo4)
        todo5 = Todo("task5", "5")
        avl.addToList(toDoList, todo5)
        self.assertEqual(2, len(avl.filterByEtat(toDoList, Etat.A_FAIRE)))
        self.assertEqual(3, len(avl.filterByEtat(toDoList, Etat.FAIT)))

    def test_filterByEtatNotInList(self):
        toDoList = avl.createList()
        self.assertEqual(0, len(avl.filterByEtat(toDoList, Etat.A_FAIRE)))
        self.assertEqual(0, len(avl.filterByEtat(toDoList, Etat.FAIT)))

    def test_parseToDoEmptyList(self):
        l = avl.parseToDoList("")
        self.assertEqual([], l)


    def test_parseToDoList(self):
        l = avl.parseToDoList("Hello, 10/10/22, 1, A_FAIRE\nWorld!, 05/10/22, 2, FAIT\n")
        self.assertEqual(2, len(l))

    def test_readBadExtension(self):
        self.assertRaises(Exception, lambda: avl.readCSVFile("fichierTestRandom.CVS"))

    def test_readFileNotFound(self):
        self.assertRaises(FileNotFoundError, lambda: avl.readCSVFile("fichierTestFileNotFound.csv"))

    def test_readBadFormat(self):
        self.assertRaises(Exception, lambda: avl.parseToDoList(avl.readCSVFile("fichierTestBadFormat.csv")))

    def test_writeEmptyToDoList(self):
        toDoList = avl.createList()
        avl.writeToCSVFile("fichierTestEmptyToDoList.csv", toDoList)
        l2 = avl.parseToDoList(avl.readCSVFile("fichierTestEmptyToDoList.csv"))
        self.assertEqual(toDoList, l2)

    def test_orderByPriority(self):
        toDoList = avl.createList()
        todo1 = Todo('task', '10/10/22')
        avl.addToList(toDoList, todo1)
        todo2 = Todo('task2', '10/10/22', 2)
        avl.addToList(toDoList, todo2)
        self.assertEqual(todo1, toDoList[0])
        avl.orderByPriority(toDoList)
        self.assertEqual(todo2, toDoList[0])

    def test_orderByPriorityNoChanges(self):
        toDoList = avl.createList()
        todo1 = Todo('task', '10/10/22', 2)
        avl.addToList(toDoList, todo1)
        todo2 = Todo('task2', '10/10/22', 2)
        avl.addToList(toDoList, todo2)
        self.assertEqual(todo1, toDoList[0])
        avl.orderByPriority(toDoList)
        self.assertEqual(todo1, toDoList[0])
    
    def test_orderByPriorityEmptyToDoList(self):
        toDoList = avl.createList()
        avl.orderByPriority(toDoList)
        self.assertEqual(0, avl.lenList(toDoList))


@pytest.mark.randomize(l=list_of(str))
def test_writeToCSVFile(l):
    l1 = []
    for i in l:
        todo = Todo(i, f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1, 24)}")
        if random.randint(1, 2) == 1:
            todo.fait()
        avl.addToList(l1, todo)
    avl.writeToCSVFile("fichierTestRandom.csv", l1)
    l2 = avl.parseToDoList(avl.readCSVFile("fichierTestRandom.csv"))
    assert l1 == l2

@pytest.mark.randomize(l=list_of(str))
def test_randomDoubleReverse(l):
    l1 = []
    for i in l:
        todo = Todo(i, f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1, 24)}")
        if random.randint(1, 2) == 1:
            todo.fait()
        avl.addToList(l1, todo)
    l2 = l1.copy()
    avl.reverseList(l1)
    avl.reverseList(l1)
    assert l2 == l1

@pytest.mark.randomize(l=list_of(str))
def test_randomReverseTwoList(l):
    l1 = []
    for i in l:
        todo = Todo(i, f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1, 24)}")
        if random.randint(1, 2) == 1:
            todo.fait()
        avl.addToList(l1, todo)
    l2 = l1.copy()
    avl.reverseList(l1)
    avl.reverseList(l2)
    assert l2 == l1

@pytest.mark.randomize(l=list_of(str, min_items=1))
def test_randomDel(l):
    l1 = []
    for i in l:
        todo = Todo(i, f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1, 24)}")
        if random.randint(1, 2) == 1:
            todo.fait()
        avl.addToList(l1, todo)
    old_len = avl.lenList(l1)
    avl.delElem(l1, random.choice(l1))
    assert old_len-1 == avl.lenList(l1)
