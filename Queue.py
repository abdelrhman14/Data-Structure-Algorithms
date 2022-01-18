class Queue:
    def __init__(self,size):
        self.q = []
        self.val = size

    def isfull(self):
        return len(self.q) == self.val

    def isempty(self):
        return len(self.q) == 0

    def enqueue(self,item):
        if self.isfull():
            print("Queue is Full!!!!")
            return
        else:
            self.q.append(item)
            print(item)

    def dequeue(self):
        if self.isempty():
            print("Queue is Empty!!!")
        else:
            e = self.q.pop(0)
            print('dequeue',e)

    def que_front(self):
        if self.isempty():
            print("Queue is Empty!!!")
        else:
            first = self.q[0]
            print('que_front',first)


    def que_rear(self):
        if self.isempty():
            print("Queue is Empty!!!")
        else:
            last = self.q[len(self.q)-1]
            print('que_rear',last)

queue = Queue(30)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue()
queue.que_front()
queue.que_rear()