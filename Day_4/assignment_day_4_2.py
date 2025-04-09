# Question-6:
# #MaxFile class 
# from pkg.file import File 
# fs = File(".")
# fs.getMaxSizeFile(2) # gives two max file names 
# fs.getLatestFiles(datetime.date(2018,2,1))
# #Returns list of files after 1st Feb 2018 

import os
import datetime

class MaxFile:
    
    def __init__(self,path):
        self.path = path
        
    def get_max_size_file(self,n,file_dict=None):
        
        if file_dict is None:
            file_dict = {}
            
        for root,dirs,files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root,file)
                if os.path.isfile(file_path):
                    file_dict[file_path] = os.path.getsize(file_path)
                    
        sorted_files = sorted(file_dict.items(), key = lambda k : k[1] ,reverse = True)
        
        return [file[0] for file in sorted_files[:n]]
        
    def get_latest_files(self,date):
        
        latest_files = []
            
        for root,dirs,files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root,file)
                if os.path.isfile(file_path):
                    latest_time = os.path.getmtime(file_path)
                    file_date = datetime.date.fromtimestamp(latest_time)
                    
                    if file_date > date:
                        latest_files.append(file_path)
                        
        return latest_files
        
if __name__ == "__main__":
    
    path = r"C:\Users\Subash\handson"
    
    fs = MaxFile(path)
    
    print(f"Top 2 Largest Files within a given directory : \n {fs.get_max_size_file(2)}")
    
    #Latest date = 8th April 2025
    
    print(f"Latest Files after the given date :\n {fs.get_latest_files(datetime.date(2025,4,8))}")
