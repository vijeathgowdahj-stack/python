class item:
    def_init_(self, data):
       self.data = data 
       self.next = None
    
    class stack:
        def_init_(self):
           self.top = None
        def push(self,data):
            item = Item(data)
            item.next = self.top
            self.top = item
         def pop(self):
            if(self.top is None):
                return
            temp = self.top
            value = temp.data
            self.top = self.top.next
            del temp
            return value
        def printStack(self):
            temp = self.top
            while (temp):
                print(temp.data)
                temp = temp.nexts 
                s = Stack()
                s.push(1)
                s.push(2)
                s.push(3)
                s.push(4)
                s.push(5)
                a=s.pop()   
                while(a):
                    print(a)
                    a=s.pop()     