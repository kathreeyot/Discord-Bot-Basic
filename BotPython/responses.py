import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'SawatDee ครับผม!'
    
    if message == '!roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    if p_message == '!Yo':
        return '``'
    if p_message == '':
        return '``'
    if message == '!information': 
        return ""#ใส่ข้อความที่คุณจะพิมลงไป
    
    
    return 'i not understand "!help".'    