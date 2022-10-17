import sys
from functions.functions import MyYaml



def main():
    if len(sys.argv) > 1:
        try:
            file1 = open(sys.argv[1],"r+")
        except: 
            print("File not found")
        else:
            lines = file1.readlines()

            v = MyYaml(len(lines), lines)
            lines = v.findTags('image:')
            with open('src/data/final.yaml', 'w') as f:
                f.writelines(lines)
            # findTags('image:', lines)

            file1.close()
    else:
        print("Args Missing")
  
if __name__=="__main__":
    main()