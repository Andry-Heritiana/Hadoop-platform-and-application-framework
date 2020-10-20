#!/usr/bin/env python

#The input will be <show, viewer_count> and <show, channel>
#and this will return viewer counts for tv shows that air an ABC

prev_show = " "  #initialize previous show to blank string
is_ABC = 0 # check if show is ABS 

total_viewer = 0 # we will sum the total number of viewer

line_cnt = 0 #count input lines
current_show = " "
for line in sys.stdin:
	line = line.strip() #strip out carriage return
	key_value = line.split('\t')
	line_cnt += 1
	current_show = key_value[0] #key is the first item in the list
        value_in = key_value[1] #value is the second item

	if current_show != prev_show: # check if the current with the previous show
		if  line_cnt > 1 and is_ABC== 1:
			print('{0} {1}'.format(prev_show,total_viewer))
		#reset variables
		is_ABC = 0
		total_viewer= 0
		prev_show = current_show # set current to be the previous for the next set of the input lines
         if value_in =='ABC': #process the current show
		is_ABC = 1
         else:
		total_viewer += int(value_in)

#print final result
print('{0} {1}'.format(current_show, total_viewer))



