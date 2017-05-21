"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension(filename):
    """Return the file extension for a full file path."""
    test=re.compile("\.([a-z]*)$")
    result=test.finditer(filename)
    #result1=result.replace(".","")
    #return result1
    for m in result:
        result1=m.group(1)
    #result2=result1.replace(".","")
    #return result2
    return result1 

def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    pattern=re.compile("\w*[aeiou]{4}\w*")
    #dictionary="hello this is a test and eiae and to try doing oiaeuu"
    result=pattern.findall(dictionary)
    return result


def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    #pattern=re.compile("[A-F a-f]*$")
    pattern=re.compile(r"([^(g-zG-Z " "\s)][A-Fa-f]+)\s?")
    result=pattern.findall(dictionary)
    return result 

def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    pattern=re.compile(r".*[^aeiouAEIOU\d\s]{6}.*")
    result=pattern.findall(dictionary)
    return result


def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.
    

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """
    #dictionary="hello"
    #partial_word="h_l_o"
    
    partial_word=partial_word.replace("_","[a-zA-Z]")
    pattern=re.compile(r"\b"+partial_word+r"\b",re.IGNORECASE)
    listt=set(pattern.findall(dictionary))
    return sorted(listt)



def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""

    
    string = r'\b[a-z]*'+letter +r'[a-z]*' +letter + r'[a-z]*'+letter+r'[a-z]*'+letter+r'[a-z]*'+letter +r'[a-z]*\b'
    pattern = re.compile(string)
    return pattern.findall(dictionary)


def abbreviate(phrase):
    """Return an acronym for the given phrase."""
    """phrase=phrase.split(" ")

    hello=""
    for word in phrase:
        hello=hello+word[0]
    return hello"""
    finalresult=""
    pattern = re.compile(r'\b([a-zA-z])[a-z]*([A-Z])*[a-z]*\b')
    result= pattern.findall(phrase)
    
    for item in result:
        for each in item:
            if len(each)>0:
                finalresult= finalresult+each.upper()
    return finalresult



def palindrome5(dictionary=dictionary):
    """Return a list of all five letter palindromes."""
    
    l=[]
    pattern=re.compile(r"\b([a-zA-Z])([a-zA-Z])[a-zA-Z]\2\1\b")
    result= pattern.finditer(dictionary)
    for m in result:
        result2=m.group()
        l.append(result2)
    return l       



def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    """
    l=[]
    pattern=re.compile(r"[a-zA-Z]*([a-zA-Z]{2})([a-zA-Z]{1}\1[a-zA-z]*)\b")
    result=pattern.finditer(dictionary)
    for m in result:
        result2=m.group(0)
        l.append(result2) 
    return l    



def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur"""
    #pattern=re.compile(r"\b([a-z]+)\1\b")
    #result=pattern.finditer(dictionary)
    l=[]
    pattern=re.compile(r"([a-z]+)(\1)\b")
    result=pattern.finditer(dictionary)
    for m in result:
        result2=m.group(0)
        l.append(result2) 
    return l 


    




