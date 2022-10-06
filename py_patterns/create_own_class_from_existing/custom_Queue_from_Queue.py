from queue import Queue as q                                                                                                            

class Queue(q):                                                                                                                         
    """create my own dunder methods for a class that does not come with any, or not customer to current codebase"""                        
    def __repr__(self):                                                                                                                 
        return f"Queue({self._qsize()})"                                                                                                 

qu = Queue()                                                                                                                            
print(qu)  
