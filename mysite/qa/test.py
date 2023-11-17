import sys
sys.path.append("D:\\15694\\my_bin\\project_argBrain\\llm_qa\\notebooks")
from m import *

def main():

    #print(sys.path)

    print("Please input a question:")
    tmp_in  = input()
    answer = fff(tmp_in)
    print("result is %s" %answer)

if __name__ =="__main__":
    main()