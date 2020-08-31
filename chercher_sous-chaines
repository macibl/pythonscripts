#!/usr/bin/env python
# chercher des sous-chaines a l'aide d'une expression réguliere
# serie est juste une chaine de caracteres avec nom-serie:personnage separes par ;

import re

series = 'Miss Fish:Phrany Fish;GOT:Daeney Tar;X-Files:Dana Scully;Miss Fish:Jack Robinson;Miss Fish:Dorothy Williams;GOT:John Snow;GOT:Tyrion Lannister;X-Files:Fox Mulder'

# pattern recherche en raw string 'r' un ":" suivi de lettres ou espace autant qu'on veut entre () donc ce sera ce qui est extrait de la chaine et jusqu'à trouver soit un ";" soit la fin de ligne "$" 
pattern = r':([A-Za-z ]+)[;|$]' 

# re.findall(motif, string to look) will return all occurences found
match = re.findall(r'GOT' + pattern, series)

print('without compil',match)

# si la chaine est ok, on la compile
pattern = re.compile(r'GOT:([A-Za-z ]+)[;|$]')
match = pattern.findall(series)
print('after compil', match)

