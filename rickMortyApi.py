import json
import requests
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    characters = []
    
    try:
######## GET Rick&Morty Characters
        
        for i in range(1,4):
            url = f"https://rickandmortyapi.com/api/character/?page={i}"    
            response = requests.get(url)
            result = response.json()
            
            for j in range(20):
                processedResults = {
                    "ID": result["results"][j]["id"],
                    "Name": result["results"][j]["name"],
                    "Species": result["results"][j]["species"],
                    "Status": result["results"][j]["status"],
                    "Origin": result["results"][j]["origin"]["name"],
                    "Image": result["results"][j]["image"],
                }
                characters.append(processedResults)
        
        
        
######## DynamoDB

        dynamoResponse = dynamodb.batch_write_item(
            RequestItems={
                'RickMortyAPITable': [
                    {
                        'PutRequest': {
                            'Item': {
                                'ID': {
                                    'N': '1',
                                },
                                'Name': {
                                    'S': 'Rick Sanchez',
                                },
                                'Species': {
                                    'S': 'Human',
                                },
                                'Status': {
                                    'S': 'Alive',
                                },
                                'Origin': {
                                    'S': 'Earth (C-137)',
                                },
                                'Image': {
                                    'S': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg',
                                },
                            },
                        },
                    },
                ],
            },
        )
        
        print(dynamoResponse)

        return characters    
      
            
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
