#test modules and toy functions
def swapcenter(str):
    spnt=int(len(str)/2)
    new=f'{str[:spnt]}a{str[spnt+1:]}'
    return new
def doubleword(phrase,ref):
    word=phrase.split()
    new=""
    for i in range(3):
        new+=f'{word[i]} '
        if i==ref-1:
            new+=f'{word[ref-1]} ' 
    string=""
    for n in range(len(new)-1):
        string+=new[n]
    return string
#uncomment the prints to test the functions
#print(swapcenter("hello"))
#print(doubleword("one two three",1))
