from queue import Queue as q                                                                                                            

class Queue(q):                                                                                                                         
    """create my own dunder methods for a class that does not come with any, or not customer to current codebase"""                        
    def __repr__(self):                                                                                                                 
        return f"Queue({self._qsize()})"                                                                                                 
    def __add__(self, item):
        self.put(item)
    
    def __sub__(self, item):
        self.get()

qu = Queue()      

qu + 1

qu + 2 

qu - 1

print(qu)  
