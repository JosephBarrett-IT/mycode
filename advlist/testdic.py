#I/usr/env/python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
char_name = input('Which character do you want to know more about? Startlord, Mystique, Hulk' )

char_stat = input('What statistic do you want to know about? real name, powers, archenemy')

print(f" {char_name}'s {char_start} is: {marvelchars[{char_name}}]" )
