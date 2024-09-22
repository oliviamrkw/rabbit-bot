import discord
import asyncio
import random

# Set up the bot client with intents
intents = discord.Intents.default()
intents.message_content = True  # This intent is needed to read message content

client = discord.Client(intents=intents)

TOKEN = 'YOUR TOKEN'
    
CHANNEL_ID = 905143091504226354

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    msg = None
    image = None
    
    # Check if the message content is 'rabbit' 
    if 'rabbit' in message.content.lower() or 'bunny' in message.content.lower() or '🐰' in message.content or '🐇' in message.content:
        number = random.randint(1,63)
        # Choose a random image from the list
        image = 'rabbit'+str(number)+'.png'
        msg = "rabbit :3"
        
        # Send the image to the channel where the message was received

    elif 'hare' in message.content.lower():
        number = random.randint(1,8)
        image = 'hare'+str(number)+'.jpg'
        msg = "hare :3"

    if msg and image:
        channel = message.channel
        try:
            await channel.send(msg, file=discord.File(image))
            print(f"Sent: {image}")
        except discord.errors.Forbidden:
            print("Cannot send messages to the channel due to permissions or other restrictions.")

# Run the bot
client.run(TOKEN)
