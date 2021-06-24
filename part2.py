from mrjob.job import MRJob

class q2(MRJob):
    
    
    def mapper(self,key,document):
        record = document.split(",")
        
        for animal in record:
            yield animal, record
        
            
        
    
            
    def reducer(self, animal, arr):
        arrx = []
        
        for i in arr:
            if animal in i:
                arrx.append(",".join(i))
        yield animal, arrx
                
        
    

q2.run()