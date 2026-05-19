class MyHashMap(object):

    def __init__(self):
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        idx = self._hash(key)
        for item in self.buckets[idx]:
            if item[0] == key:
                item[1] = value
                return
        self.buckets[idx].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        idx = self._hash(key)
        for item in self.buckets[idx]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        idx = self._hash(key)
        for i, item in enumerate(self.buckets[idx]):
            if item[0] == key:
                del self.buckets[idx][i]
                return