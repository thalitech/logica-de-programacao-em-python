import random

verbs = ['jogar ','cantar ','correr ','falar ']

adjectives = ['alegra','entristece','anima','enriquece']

nouns = [' o dia',' a noite',' a manhã',' a tarde']

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb +  adjective + noun
print (phrase)
