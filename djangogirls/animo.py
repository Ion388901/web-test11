import boto3
from pprint import pprint
from botocore.config import Config
from boto3.dynamodb.conditions import Key




def query_animo(numero):
    dynamodb = boto3.resource('dynamodb')
    table_mensajes = dynamodb.Table('Mensajes')
    response=table_mensajes.query(KeyConditionExpression=Key('ID').eq('1'))
    return response['Items']

def insertar_mensaje(id, estado, mensaje):
    dynamodb = boto3.resource ('dynamodb')
    table_mensajes = dynamodb.Table('Mensajes')
    response=table_mensajes.put_item(
        Item={
            "ID" : id,
            "Estado" : estado,
            "Mensaje" : mensaje,

        }
    )
    return response

mensaje=query_animo(1)
print (mensaje)


nuevo=insertar_mensaje("5","Mas o menos","Linda Noche")
print (nuevo)

#https://dynamodb.us-east-1.amazonaws.com

#arn:aws:dynamodb:us-east-1:277634144225:table/Mensajes