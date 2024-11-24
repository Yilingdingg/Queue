class Queue:
    def __init__(self,n):
        self.queue=[]
        self.max=n
        self.size=len(self.queue)
        self.front=0
        self.rear=0

    def enqueue(self,value):
        if self.size<self.max:
            self.queue.append(value)
            self.front=self.queue[0]
            self.rear=self.queue[-1]
            self.size=len(self.queue)
        else:
            print("The queue is full.")

    def dequeue(self):
        if self.size==0:
            print("The queue is empty")
        else:
            remove=self.queue.pop(0)
            return remove


    def clear(self):
        if self.size==0:
            print("There is no value in the queue.")
        else:
            self.queue=[]
            print("The queue is now clear.")

    def display(self):
        return self.queue
    
    def display_size(self):
        return len(self.queue)
    
    def display_front(self):
        return self.queue[0]
    
    def display_rear(self):
        return self.queue[-1]
    
    def peek(self):
        return self.display_front()
    

qu_1=Queue(10)
qu_1.enqueue(8)
#only return, so need to print
print(qu_1.display())
print(qu_1.display_size())
qu_1.enqueue(11)
print(qu_1.display())
print(qu_1.display_size())
qu_1.enqueue(92)
print(qu_1.display())
print(qu_1.display_size())
qu_1.enqueue(883)
print(qu_1.display())
print(qu_1.display_size())
print(qu_1.peek())
print(qu_1.display_rear())
print(qu_1.display_front())
qu_1.dequeue()
print(qu_1.display())
print(qu_1.display_size())
print(qu_1.peek())
qu_1.dequeue()
print(qu_1.display())
print(qu_1.display_size())

