import discord
import asyncio
import random

# Set up the bot client with intents
intents = discord.Intents.default()
intents.message_content = True  # This intent is needed to read message content

client = discord.Client(intents=intents)

# Replace with your bot's token
TOKEN = 'YOUR TOKEN'
    
FRIEND_ID = 511961079086055435

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    friend = await client.fetch_user(FRIEND_ID)

    while True:
        try:
            # Choose a random message from the list
            number = random.randint(1,20)
            # Choose a random image from the list
            image = 'rabbit'+str(number)+'.png'
            await friend.send("rabbit", file=discord.File(image))
            print("Sent:", image)
        except discord.errors.Forbidden:
            print("Cannot send messages to", friend.name, "due to privacy settings or other restrictions.")
            break  # Exit the loop if message sending is forbidden
        await asyncio.sleep(1)

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Print received messages
    print(f"Received message from {message.author}: {message.content}")

# Run the bot
client.run(TOKEN)
