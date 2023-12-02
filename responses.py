import random

def handle_response(message) -> str:
    process_msg = message.lower()

    if process_msg == "hello":
        return "Hey there"
    
    if process_msg == "roll":
        return str(random.randint(1, 6))
    
    if process_msg == "!help":
        return "`DISCORD BOT IS HERE TO HELP!`"
    
    return "Sorry, what?"