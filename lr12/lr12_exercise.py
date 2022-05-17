def soundex(name):
    terminalCode = ""
    mappings = "01230120022455012623010202"
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', "E", 'I', 'O', 'U']
    terminalCode += name[0]
    for i in range(1, len(name)):
        if name[i] in vowels:
            continue
        else:
            terminalCode += mappings[ord(name[i].lower()) - 97]
    if len(terminalCode) < 4:
        terminalCode += "0" * (4 - len(terminalCode))
    elif len(terminalCode) > 4:
        terminalCode = terminalCode[:4]
    return terminalCode


print(soundex("Leonardo"))
