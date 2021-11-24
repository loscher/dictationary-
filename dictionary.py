'''
Created on Nov 18, 2021

@author: loganoscher
dictionary
''' 
from itertools import count
def main():
    file = open("/Users/loganoscher/Library/Mobile Documents/com~apple~TextEdit/Documents/testie.txt", "r")
    dictionary = dict()
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.replace('  ', '') 
        line = line.replace('-', '')
        line = line.replace(':', '')
        line = line.replace('.', '')
        line = line.replace('!', '')
        line = line.replace(',', '')
        line = line.replace('?', '')
        text = line.split(" ")  
        for word in text:
            if word in dictionary:
                dictionary[word] = dictionary[word] + 1
            else:
                dictionary[word] = 1
    dictionary = sorted(dictionary.items(), key=lambda item: item[1])
    for x in dictionary:
        print(x)
    
if __name__ == "__main__":
    main()
#sorted(d.items(), key=lambda item: item[1])
#for key in list(dictionary.keys()):
    #return key, ",", dictionary[key]
