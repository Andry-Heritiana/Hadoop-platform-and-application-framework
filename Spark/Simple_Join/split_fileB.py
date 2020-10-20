def split_fileB(line):
        # split the input line into word, date and count_string
        dateword_count = line.split(",")
        date_word = key_value[0].split(" ")
        return (date_word[1] , date_word[0] + " " + key_value[1])
