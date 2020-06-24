try:  
       
    fileptr = open("file.txt","r")  
except FileNotFoundError:  
    print("This file doesnt exsist")  
else:  
    print("The file opened successfully")  
    fileptr.close()   

    
