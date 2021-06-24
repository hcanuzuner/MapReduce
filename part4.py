
from mrjob.job import MRJob

class q4(MRJob):
    
    
    def mapper(self,key,document):
        
        arr = document.split(",")
        yield "_",arr 
                

    
            
    def reducer(self, string, links):
        url_list = list(links)
        a = 0
        if a<=len(url_list):
            for i in url_list:
                a = a + 1
                for j in url_list:
                    if(i[0] == j[1]):
                        url = (i+j)[1:]
                        url.append(url[0])
                        url = ",".join(url[1:])
                        yield url, ""

q4.run()