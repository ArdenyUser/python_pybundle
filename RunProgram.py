print("Program Booted")
print("Making Class Config1")
print("Made Class Config1")
class Config1:
    print("Running Class Config1")
    print("Configuring Class Config1 Varibles")
    mainclass = "Config1"
    logictest = "2"
    print("Configured Class Config1 Varibles")
    print("Importing Needed Information")
    import random
    import sys
    import extraresources
    print("Imported Needed Information")
    print("Testing System Data")
    if mainclass == "Config1":
     print("System Data Test One Complete")
    else:
     print("Logging Error to Log File")
     with open("self-error-log.txt", "r+") as f:
      old = f.read() # read everything in the file
      f.seek(0) # rewind
      f.write("System Data Test One Failed; MainClass != Config1\n" + old) # write the new line before
     print("Logged Error to Log File")
     print("System Data Test One Failed")
     print("Aborting...")
     sys.exit('Error: mainclass did NOT equal Config1')
    if logictest == "2":
     print("System Data Test Two Complete")
    else:
     print("Logging Error to Log File")
     with open("self-error-log.txt", "r+") as f:
      old = f.read() # read everything in the file
      f.seek(0) # rewind
      f.write("System Data Test Two Failed; Logic Test != 2\n" + old) # write the new line before
     print("Logged Error to Log File")
     print("System Data Test Two Failed")
     print("Aborting...")
     sys.exit('Error: logictest did NOT equal 2')
    print("All System Data Tests Completed")
    print("Running Core Program")
    print("Trying to Fully Boot Program")
    print("---------------------------------------")
    print("Press Enter Key to Boot Fully")
    txt1 = input("@User:")
    print("Setting txt1 to Enter")
    txt1 = "Enter"
    print("Setted txt1 to Enter")
    print("Making Class Config2Runner")
    print("Made Class Config2Runnner")
class Config2Runner:
    print("Running Class Config2Runner")
    print("Using some Varibles from Config1")
    print("Importing Config2")
    import configend
    
    
    
    
    
    

