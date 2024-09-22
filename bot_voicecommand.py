import discord
import asyncio
import random
import os
from gtts import gTTS

# Set up the bot client with intents
intents = discord.Intents.default()
intents.message_content = True  # This intent is needed to read message content

client = discord.Client(intents=intents)

TOKEN = 'YOUR TOKEN' 
   
VOICE_CHANNEL_ID = 905141459727048837#521340743667810304myserv#905141459727048837gamingserv
CHANNEL_ID = 732217684044939315#1273657075561402380myserv#905143091504226354gaminserv

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message starts with "say "
    if message.content.startswith("say "):
        # Extract the text after "say "
        text_to_say = message.content[len("say "):]

        # Convert text to speech using gTTS
        tts = gTTS(text=text_to_say, lang='en')
        tts.save("tts.mp3")

        # Checks to see if channel exists
        channel = client.get_channel(VOICE_CHANNEL_ID)
        if channel is None or not isinstance(channel, discord.VoiceChannel):
            await message.channel.send("Voice channel not found.")
            return

        # Check if the bot is already connected to a voice channel
        vc = discord.utils.get(client.voice_clients, guild=channel.guild)
        if not (vc and vc.is_connected()):
            vc = await channel.connect()

        # Ensure that the file exists
        if os.path.isfile("tts.mp3"):
            # Play the TTS message
            vc.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: print('Finished playing TTS message'))
        else:
            print("TTS file not found!")

    elif message.content.lower() == "dc":
        vc = discord.utils.get(client.voice_clients, guild=message.guild)
        if vc and vc.is_connected():
            await vc.disconnect()

    elif message.content.lower() == "stop":
        vc = discord.utils.get(client.voice_clients, guild=message.guild)
        if vc.is_playing():
            vc.stop()
            print("Stopping")

# Run the bot
client.run(TOKEN)
