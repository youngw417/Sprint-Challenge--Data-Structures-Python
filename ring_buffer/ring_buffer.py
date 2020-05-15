class RingBuffer:
    def __init__(self, capacity):
        self.my_buffer = [None] * capacity
        self.capacity =  capacity
        self.count = 0

    def append(self, item):
       #before append, move all elements to left
       #append it at last postion
        # count = 0
        if self.my_buffer[0] is None:
            self.my_buffer.pop(0)
            self.my_buffer.append(item)
        else:
            turn = self.count % len(self.my_buffer)
            self.my_buffer[turn] = item
            self.count += 1

    def get(self):
        return [item for item in self.my_buffer if item is not None]


    