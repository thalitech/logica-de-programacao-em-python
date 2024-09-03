scores = [60,50,60,58,54,54,58,50,52,54]
score= scores[3]
print (score)

smoothies = ['coconut','strawberry','banana','pineapple','acai berry']
favorite = smoothies[2]
print (smoothies)
print (favorite)

eighties = ['','duran duran','B-52s','muse']
newwave = ['flock of seagulls', 'postal service']

remember = eighties[1]

eighties[1] = 'culture club'

band = newwave[0]

eighties[3] = band

eighties[2] = remember

print (eighties)

length = len(smoothies)
length2 = len(newwave)
print(length,length2)

length = len(smoothies)
last = smoothies[length-1]
print(last)

last = smoothies[-1]
second_last = smoothies[-2]
third_last = smoothies [-3]
print(last)
print(second_last)
print(third_last)

most_recent = -1
recent = smoothies[most_recent]
print(recent)
most_recent2 = len(smoothies)-1
recent2 = smoothies[most_recent2]
print(recent2)
