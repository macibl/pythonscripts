#!/usr/bin/env python
# find sub-strings using regex re.findall
# series is just a string with TV_serie_name:character separated with ";"

import re

series = 'Miss Fish:Phrany Fish;GOT:Daeney Tar;X-Files:Dana Scully;Miss Fish:Jack Robinson;Miss Fish:Dorothy Williams;GOT:John Snow;GOT:Tyrion Lannister;X-Files:Fox Mulder'

# pattern do search in raw string 'r' one ":" followed by letters or spaces as much as needed, in (), then will be extracted, until ";" is found or end of line "$" 
pattern = r':([A-Za-z ]+)[;|$]' 

# re.findall(motif, string to look) will return all occurences found
match = re.findall(r'GOT' + pattern, series)

print('without compil',match)

# if string is OK, can be compiled, work faster
# same as above, but compiled
pattern = re.compile(r'GOT:([A-Za-z ]+)[;|$]')
match = pattern.findall(series)
print('after compil', match)

