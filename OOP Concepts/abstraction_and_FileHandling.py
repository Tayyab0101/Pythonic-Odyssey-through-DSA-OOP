# Abstraction serves as a foundational principle within Python programming, enabling the simplification of intricate concepts by emphasizing essential details. It entails concealing extraneous complexities, thereby presenting users with solely pertinent information.

from abc import ABC, abstractmethod

class DataStorage(ABC):
    @abstractmethod
    def store(self, key, data):
        pass

    @abstractmethod
    def retrieve(self, key):
        pass

class FileStorage(DataStorage):
    def store(self, key, data):
        file = open(key, "w")
        file.write(data)

    def retrieve(self, key):
        file = open(key, "r")
        return file.read()

if __name__ == "__main__": # to run directly and save from use as module
    storage = FileStorage()
    storage.store("data.txt", "Hello, world!") # Store Data
    data = storage.retrieve("data.txt") # Retrieve data
    print(data)  # Output: "Hello, world!"