import discord
import asyncio
import random

msgs_list = [
    'rabbit1.png',
    'rabbit2.png',
    'rabbit3.png',
    'rabbit4.png',
    'rabbit5.png',
    'rabbit6.png',
    'rabbit7.png',
    'rabbit8.png',
    'rabbit9.png',
    'rabbit10.png',
    #'https://tenor.com/view/coelhocaindofofoengracadocuticutiuwu-gif-18255501',
    #'https://tenor.com/view/soobtime-bunny-stare-staring-cute-gif-18914755',
    #'https://tenor.com/view/gina101-gina101creative-bunny-rabbit-cute-gif-20125194',
    ]

tts_list = [
    "i love rabbits",
    "i love hares",
    ]

# Set up the bot client with intents
intents = discord.Intents.default()
intents.message_content = True  # This intent is needed to read message content

client = discord.Client(intents=intents)

# Replace with your bot's token
TOKEN = 'YOUR TOKEN'

# The ID of your friend's user
FRIEND_IDS = [
    511961079086055435, #hugo,
    291283720588099584, #matthew,
    638529428753874974, #noah,
    680069106896207873, #ben,
    436239524952145930, #william,
    ]
    
#FRIEND_ID = 511961079086055435
CHANNEL_ID = 905143091504226354

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    #friend = await client.fetch_user(friend)
    #channel = client.get_channel(CHANNEL_ID)

    while True:
        for friend in FRIEND_IDS:
            friend = await client.fetch_user(friend)
            try:
                #msg = random.choice(msgs_list)
                image=random.choice(msgs_list)
                await friend.send("rabbit", file=discord.File(image))
                print("Sent to",friend.name,":", image)
            except discord.errors.Forbidden:
                print("Cannot send messages to", friend.name, "due to privacy settings or other restrictions.")
                break  # Exit the loop if message sending is forbidden
        await asyncio.sleep(600)

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Print received messages
    print(f"Received message from {message.author}: {message.content}")

    # Optional: Respond to the user
    #if message.author.id == FRIEND_ID:
        #await message.channel.send("Got your message!")

# Run the bot
client.run(TOKEN)
