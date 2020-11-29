from collections import OrderedDict
global flag

def prefix_func(pattern, p, prefix_list): #prefix function to calculate the 

    lpi = 0 #longest prefix length found before
    prefix_list[0]   

    index = 1 #count starts from 1 since the first element in prefix_list array is zero
  
    while index < p: 
        if pattern[index]== pattern[lpi]: 
            lpi = lpi + 1
            prefix_list[index] = lpi
            index = index + 1
        else: 
            if lpi != 0: 
                lpi = prefix_list[lpi-1] 

            else: 
                prefix_list[index] = 0
                index = index+1

def KMP(pattern,text,file): 

    p = len(pattern)  
    t = len(text) 
  
    prefix_list = [0]*p #prefix array
    char_match = 0

    #initiating prefix function array calling prefic function
    prefix_func(pattern, p, prefix_list) 
  
    match_index = 0 #index for matching
    
    while match_index < t: 
        if pattern[char_match] == text[match_index]: 
            match_index = match_index+1
            char_match = char_match+1
  
        if char_match == p:
            
            global flag #flag for file writing purpose
            flag=1      

            file.write("Found pattern at index "+str(match_index-char_match)+"\n")
            print("Found pattern at index "+str(match_index-char_match)+"\n")
            #displaying output mentioning the pattern is found in the text
            
            char_match = prefix_list[char_match-1] 
  
        elif match_index < t and pattern[char_match] != text[match_index]: 
             
            if char_match != 0: 
                char_match = prefix_list[char_match-1] 
            else: 
                match_index = match_index+ 1
  
def read_text():

    text_list = OrderedDict()
    #initiating text_list dictionary
    #dictionary ordering function for ordering purposes of the dictionary

    textfile = open("dnadata.txt","r")
    textline = textfile.readline().rstrip()
    #file opening and reading line by line

    while textline!=">EOF":
        title = "" #initiating key and value of the dictionary
        text = ""

        if textline.startswith(">"):
            title = textline
            textline = textfile.readline().rstrip()
            #extracting titles from file

        while not textline.startswith(">"):
             text = text + textline
             textline = textfile.readline().rstrip()
             #extracting texts from file

        text_list.update({title[1:]:text})
        #adding extraxted titles and data to the dictionary

    textfile.close()
    return text_list

def read_pat():

    pat_list = OrderedDict()
    #initiating text_list dictionary
    #dictionary ordering function for ordering purposes of the dictionary

    patfile = open("querybase.txt","r")
    patline = patfile.readline().rstrip()

    while patline!=">EOF":
        description = "" #initiating key and value of the dictionary
        pattern = ""

        if patline.startswith(">"):
            description = patline
            patline = patfile.readline().rstrip()
            #extracting descriptions from file

        while not patline.startswith(">"):
            pattern = pattern + patline
            patline = patfile.readline().rstrip()

        pat_list.update({description[1:]:pattern})
    #adding extraxted desciptions and patterns to the dictionary
        
    patfile.close()
    return pat_list

def main():

    texts = read_text()
    patterns = read_pat()
    #assigning dictionaries

    output = open("output.txt", "a");
    #output file creating

    for j in range(0,len(patterns)):

        print("\n")
        output.write("\n")

        output.write("\t\t"+list(patterns.keys())[j])
        print("\t\t"+list(patterns.keys())[j])
        
        output.write("\n")
        print("\n")

        #displaying descriptions about patterns
        
        for i in range(0,len(texts)):

            output.write(list(texts.keys())[i])
            print(list(texts.keys())[i])

            #displaying titles of texts
            
            output.write("\n")
            #print("\n")

            text = list(texts.values())[i]

            output.write("\n")
            #print("\n")
            
            pattern = list(patterns.values())[j]
            
            global flag;
            flag=0;

            KMP(pattern,text,output)
            #applying pattern matching
            
            if(flag==0):
                output.write("Pattern not found"+"\n")
                print("Pattern not found"+"\n")

            #displaying not found if the flag is not set to 1 as in KMP function
            
            #print("\n")
            output.write("\n")

        
    output.close()
    #output file closing
    
main()
#calling main driver function
