class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

#Test Patient Class
p1 = Patient("Riley", 2)
print(p1.name)       
print(p1.urgency)    

class MinHeap:
    def __init__(self):
        self.data = []
   
    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if (self.data[index].urgency >= self.data[parent_index].urgency):
                break
            self.data[index], self.data[parent_index] = (self.data[parent_index], self.data[index])
            index = parent_index
    
    def heapify_down(self, index):
        size = len(self.data)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if (left < size and self.data[left].urgency < self.data[smallest].urgency):
                smallest = left

            if (right < size and self.data[right].urgency < self.data[smallest].urgency):
                smallest = right

            if smallest == index:
                break
            self.data[index], self.data[smallest] = (self.data[smallest], self.data[index])
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        for patient in self.data:
            print(f"{patient.name} ({patient.urgency})")

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def remove_min(self):
        if len(self.data) == 0:
            return None
        minimum = self.data[0]

        if len(self.data) == 1:
            self.data.pop()
            return minimum
        
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return minimum

# Test your MinHeap class here including edge cases
heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.print_heap()

next_up = heap.peek()
print(next_up.name, next_up.urgency)

served = heap.remove_min()
print(served.name) 
heap.print_heap()

#Test an Empty Heap
empty_heap = MinHeap()
print(empty_heap.peek())
print(empty_heap.remove_min())

#Test a Heap Containing One Patient
single_heap = MinHeap()
single_heap.insert(Patient("Riley", 2))
served = single_heap.remove_min()
print(served.name, served.urgency)
print(single_heap.peek())
print(single_heap.data)

#Test Heap Containing Patients with the Same Urgency
equal_heap = MinHeap()
equal_heap.insert(Patient("Alex", 3))
equal_heap.insert(Patient("Jordan", 3))
equal_heap.print_heap()
print(equal_heap.remove_min().urgency)
print(equal_heap.remove_min().urgency)