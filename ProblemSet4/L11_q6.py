class Queue(object):
    def __init__(self):
        self.q=[]
        
    def insert(self,e):
        return self.q.append(e)
        
    def remove(self):
        try:
            return self.q.pop(0)       
        except:
            raise ValueError("ValueError")