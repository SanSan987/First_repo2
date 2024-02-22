mymoto = {
    'brand': 'Ducati', 'price': 10000, 'vol': 1.2
    } 
keyname = 'brand'
mymoto[keyname] = 'BMW'

print(mymoto.copy())
youmoto = mymoto.copy()
youmoto['type'] = 'diz'
youmoto['speed'] = 220, 250
print(youmoto)

