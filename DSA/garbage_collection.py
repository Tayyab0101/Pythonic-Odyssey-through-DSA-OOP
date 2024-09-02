import gc

class House:
    def __init__(self, address):
        self.address = address
        print(f"A house at {address} is constructed.")
    
    def __del__(self):
        print(f"The house at {self.address} is demolished.")

# Create some instances of the House class
house1 = House("123 Main Street")
house2 = House("456 Oak Avenue")

# Now, let's simulate a situation where the houses are no longer needed
# We'll delete the references to the houses
del house1
del house2

# At this point, the houses are no longer accessible, but they still exist in memory

# Let's trigger garbage collection explicitly to reclaim the memory
gc.collect()
