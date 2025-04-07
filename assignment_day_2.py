import glob
import os.path

#Given a directory, find out the file Name having max size recursively 

path = r"C:\Users\Subash\handson"

folder = glob.glob(path+r"\*")

def largest_file(folder,large_size,largest_file_path=None):
    
    for file in folder:
        if os.path.isfile(file):
            size = os.path.getsize(file)
            if size>large_size:
                largest_file_path = file
                large_size = size
        elif os.path.isdir(file):
            sub_folder = glob.glob(os.path.join(file,"*"))
            largest_file(sub_folder,large_size,)
            
    return (largest_file_path,large_size)
    
    
    
file = largest_file(folder,0)
print(f"Largest File within a given directory is  :{file[0]}")
print(f"Size of that file is  :{file[1]} in kbs")


#Recursively go below a dir and based on filter, dump those files in to  single file

path=r"C:\Users\Subash\handson"

folder=glob.glob(path+r"\*")

data=r"C:\Users\Subash\handson\Day_2\Data.txt"

def  single_file(folder,data):
    for file in folder:
        if os.path.isfile(file):
            if file.endswith(".txt"):
                with open(file,"rt") as f:
                    lines = f.readlines()
                with open(data,"at") as f_text:
                    f_text.write("\n-------------------------\n")
                    f_text.write("Data From file" + " "+file+"\n")
                    f_text.writelines(lines)
                    f_text.write("\n-------------------------\n")
        else:
            sub_folder=glob.glob(os.path.join(file,"*"))
            
            single_file(sub_folder,data)
            
single_file(folder,data)
            
      


