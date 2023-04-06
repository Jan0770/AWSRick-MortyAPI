import requests

def getCharacters():
    characters = []
    

######## GET Rick&Morty Characters
        
    for i in range(1,4):
        url = f"https://rickandmortyapi.com/api/character/?page={i}"    
        response = requests.get(url)
        result = response.json()
            
        for j in range(20):
            processedResults = {
                "ID": str(result["results"][j]["id"]),
                "Name": result["results"][j]["name"],
                "Species": result["results"][j]["species"],
                "Status": result["results"][j]["status"],
                "Origin": result["results"][j]["origin"]["name"],
                "Image": result["results"][j]["image"],
            }
            characters.append(processedResults)
        
    print(characters[0])    
        
######## DynamoDB
    # for i in range(60):
    #     RequestItems = {
    #                 'RickMortyAPITable': [
    #                     {
    #                         'PutRequest': {
    #                             'Item': {
    #                                 'ID': {
    #                                     'N': characters[i]["ID"],
    #                                 },
    #                                 'Name': {
    #                                     'S': characters[i]["Name"],
    #                                 },
    #                                 'Species': {
    #                                     'S': characters[i]["Species"],
    #                                 },
    #                                 'Status': {
    #                                     'S': characters[i]["Status"],
    #                                 },
    #                                 'Origin': {
    #                                     'S': characters[i]["Origin"],
    #                                 },
    #                                 'Image': {
    #                                     'S': characters[i]["Image"],
    #                                 },
    #                             },
    #                         },
    #                     },
    #                 ],
    #             },
            


getCharacters()