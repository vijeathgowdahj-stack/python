class Item:
    def __init__(self,data):
        self.next = None
        self.data = data
    class Queue:
        def _init_(self):
               self.front = None
               self.rear = None
    def insert(self,data):
            item= Item(data)
            if(self.rear is None):
                self.front=item
            else:
                 self.rear.next=item
                 self.rear=item
            def delete(self):
                 if(self.front is None):
                      return
                 temp= self.front
                 value = temp.data
                 self.front= self.front.next
                 del temp
                 return value
            
            q = Queue()
            q.insert(1)
            q.insert(2)
            q.insert(3)
            q.insert(4)
            q.insert(5)
            a=q.delete()
            while (a):
                 print(a)
                 a=q.delete()

            
            

            

            
