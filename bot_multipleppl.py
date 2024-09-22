import discord
import asyncio
import random

# Set up the bot client with intents
intents = discord.Intents.default()
intents.message_content = True  # This intent is needed to read message content

client = discord.Client(intents=intents)

TOKEN = 'YOUR TOKEN'

# The ID of your friend's user
FRIEND_IDS = [
    511961079086055435, #hugo
    291283720588099584, #matthew
    ]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    while True:
        for friend in FRIEND_IDS:
            friend = await client.fetch_user(friend)
            try:
                number = random.randint(1,32)
                image = 'rabbit'+str(number)+'.png'
                await friend.send("rabbit for you", file=discord.File(image))
                print("Sent to",friend.name,":", image)
            except discord.errors.Forbidden:
                print("Cannot send messages to", friend.name, "due to privacy settings or other restrictions.")
                break  # Exit the loop if message sending is forbidden
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Print received messages
    print(f"Received message from {message.author}: {message.content}")

# Run the bot
client.run(TOKEN)
