def split_fileA(line):
        # split the input line in word and count on the comma
        key_value = line.split(",")
        #get the word and turn the count to an integer  
        return (key_value[0], int(key_value[1]))
