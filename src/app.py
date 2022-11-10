# =================================================================================================
# This program is written by Sachinthra N V.
# This code reads a yaml file and adds imagepullpolicy according the cases given.
__author__ = "Sachinthra N V"
__copyright__ = "Copyright (C) Sachinthra N V"
__version__ = "1.0"
# =================================================================================================
# This lib can be used to get command line arguments
import sys
# MyYaml is the class i created in the functions folder
from functions.functions import MyYaml

# add globals for every string
# var naming

# Main function
# This function reads the input file using the link given in as arguments in the run command
# python3 src/app.py Source_Data_File_Path [Destination_Data_File_Path]
def main():
    if len(sys.argv) > 1:
        try:
            file1 = open(sys.argv[1],"r+")
        except: 
            print(sys.argv[1]," - File not found")
        else:
            # Read all the lines in the Yaml file
            lines = file1.readlines()

            # Creating a MyYaml Class Object.
            v = MyYaml(len(lines), lines)

            # Call the function findTags which is in the MyYaml class.
            lines = v.findTags('image:')

            # This checks the user gave the destination location if not it will use the default location. 
            outFile = sys.argv[2] if len(sys.argv)==3 else 'src/data/final.yaml'
            
            # Writing the output to the destination file.
            print("OUTFILE: ", outFile)
            with open(outFile, 'w') as f:
                f.writelines(lines)
            # findTags('image:', lines)

            file1.close()
    else:
        print("Args Missing")
  
if __name__=="__main__":
    main()