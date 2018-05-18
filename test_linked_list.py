import unittest
from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    linked_list = LinkedList()

    def setUp(self):
        items = [8, 2, 3, 6, 1, 7]
        for item in items:
            self.linked_list.insert(item)

    def tearDown(self):
        self.linked_list.clear()

    def test_not_empty(self):
        self.assertFalse(self.linked_list.empty(), "The linked list is empty")

    def test_length(self):
        self.assertEqual(6, self.linked_list.length(),
                         str(self.linked_list.to_list()) + " should have a length of 6")

    def test_insertion(self):
        self.linked_list.insert(0)
        self.assertEqual([8, 2, 3, 6, 1, 7, 0], self.linked_list.to_list())

    def test_deletion(self):
        self.linked_list.delete(6)
        self.assertEqual([8, 2, 3, 1, 7], self.linked_list.to_list())

    def test_cannot_delete_non_existing(self):
        self.assertFalse(self.linked_list.delete(12))

    def test_find_element(self):
        self.assertTrue(self.linked_list.find(3))

    def test_find_non_existing_element(self):
        self.assertFalse(self.linked_list.find(23))

    def test_to_list(self):
        self.assertEqual([8, 2, 3, 6, 1, 7], self.linked_list.to_list())

    def test_clear(self):
        self.linked_list.clear()
        self.assertTrue(self.linked_list.empty())
        self.assertEqual(0, self.linked_list.length())


if __name__ == '__main__':
    unittest.main()
