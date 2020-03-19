import sys

def compareString(string1, string2) :
  
  
    # Store mapping of every character from string 1 to that of string 2. Initialize all entries of the array as -1
    str1_map = [-1] * MAX_CHARS
  
    # Loop through all characters one by one
    for i in range(len(string1)) :
  
        # If the character in string 1 is found before, then check if previous appearance is mapped to same character of string 2 
        if str1_map[ord(string1[i])] != string2[i] :
            return False
        
        # if current character of string 1 is found for first time
        elif str1_map[ord(string1[i])] == -1 :
  
            # Store mapping of current characters
            str1_map[ord(string1[i])] = string2[i]
            
    return True
  
# Driver program
if __name__ == "__main__" :
    MAX_CHARS = 256
    print(compareString(sys.argv[1], sys.argv[2]))