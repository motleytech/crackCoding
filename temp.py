data = """How quickly can you find out what is so unusual about this paragraph? It looks so ordinary that you would think that nothing is wrong with it at all, and, in fact, nothing is. But it is unusual. Why? If you look at it, study it and think about it, you may find out, but I am not going to assist you in any way. You must do it without coaching. No doubt, if you work at it for long, it will dawn on you. Who knows? Go to work and try your skill. Par is about half an hour. So jump to it and try your skill at figuring it out. Good luck --don't blow your cool."""

import string
print string.letters

numchars =  len([x for x in data if x in string.letters])
freq = .12
prob = pow(1 - freq, numchars)
print prob
print numchars
