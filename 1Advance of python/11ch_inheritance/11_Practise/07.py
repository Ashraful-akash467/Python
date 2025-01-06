class Vector:
    def __init__(self, l):
        self.l = 1

    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))