import json

def validate(slots):

    
    if not slots['Location']:
        print("Inside Empty Location")
        return {
        'isValid': False,
        'violatedSlot': 'Location'
        }        
        
    if not slots['CheckInDate']:
        
        return {
        'isValid': False,
        'violatedSlot': 'CheckInDate',
    }
        
    if not slots['nights']:
        return {
        'isValid': False,
        'violatedSlot': 'nights'
    }
        
    if not slots['RoomType']:
        return {
        'isValid': False,
        'violatedSlot': 'RoomType'
    }

    return {'isValid': True}

def lambda_handler(event, context):
    
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    print(event['invocationSource'])
    print(slots)
    print(intent)
    validation_result = validate(slots)
    print(validation_result)
    if event['invocationSource'] == 'DialogCodeHook':
        
        if not validation_result['isValid']:
            
             response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                }
               } 
   
        else:
            response = {
                "sessionState": {
                    "dialogAction": {
                        "type": "Delegate"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                    
                    }
        
            }
        } 
        return response
    if event['invocationSource'] == 'FulfillmentCodeHook':
        
        
        response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intent,
                'slots': slots,
                'state':'Fulfilled'
                
                }
    
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "Thanks, I have placed your reservation"
            }
        ]
    }
    return response