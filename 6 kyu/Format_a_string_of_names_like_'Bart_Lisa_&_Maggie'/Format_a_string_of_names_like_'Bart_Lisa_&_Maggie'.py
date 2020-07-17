def namelist(names):
    formated = ''
    if(len(names) == 1):
        return names[0]['name']
    elif(len(names) == 2):
        formated += names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for i in range(0, len(names)-1):
            formated += names[i]['name'] + ", "
        formated = formated[:-2] + " & " + names[len(names)-1]['name']
    return formated