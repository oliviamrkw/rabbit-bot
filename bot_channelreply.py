import discord
import asyncio
import random

##msgs_list = [
##    'rabbit1.png',
##    'rabbit2.png',
##    'rabbit3.png',
##    'rabbit4.png',
##    'rabbit5.png',
##    'rabbit6.png',
##    'rabbit7.png',
##    'rabbit8.png',
##    'rabbit9.png',
##    'rabbit10.png',
##    ]

# Set up the bot client with intents
intents = discord.Intents.default()
intents.message_content = True  # This intent is needed to read message content

client = discord.Client(intents=intents)

# Replace with your bot's token
TOKEN = 'YOUR TOKEN'
    
CHANNEL_ID = 1273657075561402380

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Check if the message content is 'rabbit' 
    if 'rabbit' in message.content.lower() or 'bunny' in message.content.lower() or '🐰' in message.content or '🐇' in message.content:
        number = random.randint(1,21)
        # Choose a random image from the list
        image = 'rabbit'+str(number)+'.png'
        
        # Send the image to the channel where the message was received
        channel = message.channel
        try:
            await channel.send("rabbit :3", file=discord.File(image))
            print(f"Sent: {image}")
        except discord.errors.Forbidden:
            print("Cannot send messages to the channel due to permissions or other restrictions.")

# Run the bot
client.run(TOKEN)
