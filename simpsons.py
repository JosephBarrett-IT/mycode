challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]




a = challenge[2][1] 

b = challenge[2][0]

c = challenge[3]

#print(f'My {a}! The {b} do {c}!') Challenge complete!

e = trial[2]["goggles"]  #op=eyes

f = trial[2]["eyes"]   #op=goggles

g = trial[3] #op=nothing

#print(f' My {e}! The {f} do {g}!')

#print(nightmare[0]["user"]["first"])

h = nightmare[0]["user"]["name"]["first"]

i = nightmare[0]["kumquat"]

j = nightmare[0]["d"]

print(f'My {h}! The {i} do {j}!')
