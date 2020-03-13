#from textgenrnn import textgenrnn
import requests
url = 'http://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail'
url_id = 'https://thecocktaildb.com/api/json/v1/1/lookup.php?i='
resp = requests.get(url=url)
drink_id = list()
outf = open('cocktail.txt','w')

for res in resp.json()['drinks']:
    drink_id.append(res['idDrink'])

for idd in drink_id:
    resp = requests.get(url=url_id+str(idd))
    keys = list()
    for res in resp.json()['drinks']:
        keys = res.keys()
        for key in keys:
            if ((key=='strDrink') or (key == 'strInstructions') or ('strIngredient' in key)):
               if str(res[key]) != 'None':
                  outf.write('{'+str(key)+':'+str(res[key])+'}')
        outf.write('\n')  
        outf.write('\n')
#textgen = textgenrnn()
#textgen.train_from_file('ch-cookie.txt', num_epochs=2)
#textgen.generate_to_file('cookie-new.txt', n=20)
