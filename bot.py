import discord
import responses
import config

async def send_msg(message, user_msg, is_private):
    try:
        response = responses.handle_response(user_msg)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_chatbot():
    TOKEN = config.token

    discordIntents = discord.Intents.default()
    discordIntents.message_content = True
    client = discord.Client(intents=discordIntents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        userMsg = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{userMsg}" ({channel})')

        if userMsg[0] == '?':
            userMsg = userMsg[1:]
            await send_msg(message, userMsg, is_private=True)
        else:
            await send_msg(message, userMsg, is_private=False)
    
    client.run(TOKEN)