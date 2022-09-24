import unittest
import random
import pytest
from pytest import list_of


import avl



class TestAvl(unittest.TestCase):
    def test_createList(self):
        self.assertIsNotNone(avl.createList())
        self.assertEqual([], avl.createList())

    def test_addToList(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        self.assertEqual([1], toDoList)
        avl.addToList(toDoList, 2)
        self.assertEqual([1,2], toDoList)

    def test_delElem(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.addToList(toDoList, 2)
        self.assertEqual([1,2], toDoList)
        avl.delElem(toDoList, 1)
        self.assertEqual([2], toDoList)
        avl.delElem(toDoList, 2)     
        self.assertEqual([], toDoList)
        

    def test_delElem_notInList(self):
        toDoList = avl.createList()
        self.assertEqual("L'élément n'est pas présent dans la liste", avl.delElem(toDoList, 2))


    def test_clearList(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.addToList(toDoList, 2)
        avl.addToList(toDoList, 3)
        avl.clearList(toDoList)
        self.assertIsNotNone(toDoList)
        self.assertEqual([], toDoList)
        avl.clearList(toDoList)
        self.assertIsNotNone(toDoList)
        self.assertEqual([], toDoList)

    def test_isInList(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        self.assertTrue(avl.isInList(toDoList, 1))

    def test_isNotInList(self):
        toDoList = avl.createList()
        self.assertFalse(avl.isInList(toDoList, 1))

    def test_reverseList(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.addToList(toDoList, 2)
        avl.addToList(toDoList, 3)
        avl.reverseList(toDoList)
        self.assertEqual([3,2,1], toDoList)

    def test_reverseEmptyList(self):
        toDoList = avl.createList()
        avl.reverseList(toDoList)
        self.assertEqual([], toDoList)

    def test_reverseListOfOneElem(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.reverseList(toDoList)
        self.assertEqual([1], toDoList)

    def test_lenList(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.addToList(toDoList, 2)
        avl.addToList(toDoList, 3)
        self.assertEqual(3, avl.lenList(toDoList))

    
    def test_lenEmptyList(self):
        toDoList = avl.createList()
        self.assertEqual(0, avl.lenList(toDoList))


    def test_numberOfOcc(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.addToList(toDoList, 1)
        self.assertEqual(2, avl.numberOfOcc(toDoList, 1))

    
    def test_numberOfOccEqualsZero(self):
        toDoList = avl.createList()
        avl.addToList(toDoList, 1)
        avl.addToList(toDoList, 1)
        self.assertEqual(0, avl.numberOfOcc(toDoList, 2))


    def test_numberOfOccEmptyList(self):
        toDoList = avl.createList()
        self.assertEqual(0, avl.numberOfOcc(toDoList, 2))


    def test_parseToDoEmptyList(self):
        l = avl.parseToDoList("")
        self.assertEqual([], l)
        l = avl.parseToDoList("\n\n")
        self.assertEqual(["",""], l)


    def test_parseToDoList(self):
        l = avl.parseToDoList("Hello\nWorld!\n")
        self.assertEqual(["Hello", "World!"], l)


@pytest.mark.randomize(l=list_of(str))
def test_writeToCSVFile(l):
    avl.writeToCSVFile("fichierTestRandom.csv", l)
    l2 = avl.parseToDoList(avl.readCSVFile("fichierTestRandom.csv"))
    assert l == l2

@pytest.mark.randomize(l=list_of(str))
def test_randomDoubleReverse(l):
    l2 = l.copy()
    avl.reverseList(l)
    avl.reverseList(l)
    assert l2 == l

@pytest.mark.randomize(l=list_of(str))
def test_randomReverseTwoList(l):
    l2 = l.copy()
    avl.reverseList(l)
    avl.reverseList(l2)
    assert l2 == l

@pytest.mark.randomize(l=list_of(str, min_items=1))
def test_randomDel(l):
    old_len = avl.lenList(l)
    avl.delElem(l, random.choice(l))
    assert old_len-1 == avl.lenList(l)
