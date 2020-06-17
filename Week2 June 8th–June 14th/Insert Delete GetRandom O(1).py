# This is an exclusive problem only available in the Deluxe version of this course.
# To learn more, visit https://kaeducation.com/lc-py.html

import random

class RandomizedSet:

    def __init__(self):
        self.array = []
        self.pos = {}

    def insert(self, val):
        if val not in self.array:
            self.array.append(val)
            self.pos[val] = len(self.array) - 1
            return True
        return False


    def remove(self, val):
        if val in self.array:
            indx = self.pos[val]
            self.swap(self.array, indx, -1)
            self.pos[self.array[indx]] = indx
            self.array.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        return random.choice(self.array)


    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
