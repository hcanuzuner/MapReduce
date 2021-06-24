
from mrjob.job import MRJob

class q3(MRJob):
    
    
    def mapper(self,key,document):
        
        animals = []
        
        no = len(document.split(" "))
        
        arr = document.split(" ")
        
        for i in range (0, no-3):
            yield " ".join([arr[i],arr[i+1],arr[i+2],arr[i+3]]),1

    
            
    def reducer(self, word, maxnum):
        yield (word, sum(maxnum))
        
    

q3.run()





