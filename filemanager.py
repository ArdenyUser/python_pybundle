print("--Python File Manager--")
class PythonFileManager:
    print("Defining Functions")
    def inputuser():
        inputu = input("@User:")
    print("Defined Functions")
x = 1
while True:
    print("1: Edit a File, 2: View a File, 3: Erase Contents/Delete File (Select a Number 1 or 2, or 3)")
    inputu = input("@User:")
    if inputu == "1":
        print("Type a Name of a File (All File Names Must Be In This Programs Main Directory)")
        inputu = input("@User:")
        hold1 = inputu
        print(hold1 + " is selected")
        print("Now Type a Sentence to Add to " + hold1)
        inputu = input("@User:")
        hold2 = inputu
        print("Editing File")
        with open(hold1, "r+") as f:
         old = f.read() # read everything in the file
         f.seek(0) # rewind
         f.write(hold2 + old) # write the new line before
        print("Finished Editing")
    if inputu == "2":
        print("Select a File to View (Only in This Programs Directory)")
        inputu = input("@User:")
        holdv1 = inputu
        print("Viewing File " + holdv1)
        with open(holdv1, "r+") as f:
         data = f.read() # read everything in the file
         f.seek(0) # rewind
        print(data)
    if inputu == "3":
        print("1 to Erase Contents of A File, 2 to Delete A File")
        inputu = input("@User:")
        if inputu == "2":
            print("Select A File to Delete")
            inputu = input("@User:")
            ghold1 = inputu
            print("Are You Sure? Y or N")
            inputu = input("@User:")
            if inputu == "Y":
                print("Deleting File")
                import os
                if os.path.exists(ghold1):
                 os.remove(ghold1)
                else:
                 print("The File Does Not Exist")
            if inputu == "N":
                print("Aborting...")
                import sys
                sys.exit()
        if inputu == "1":
            print("Select A File to Erase It's Contents")
            inputu = input("@User:")
            holdsv1 = inputu
            print("Are You Sure? Y or N")
            inputu = input("@User:")
            if inputu == "Y":
                print("Erasing Contents")
                file = open(holdsv1,"w")
                file.close()
            if inputu == "N":
                print("Aborting...")
                import sys
                sys.exit()
                
                
    
    
            
        
      

        
        
       
    x += 1
    