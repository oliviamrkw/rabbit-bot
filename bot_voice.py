import discord
import asyncio
import random
from gtts import gTTS

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
   
#FRIEND_ID = 511961079086055435
#CHANNEL_ID = 905143091504226354
VOICE_CHANNEL_ID = 521340743667810304
TTS_MESSAGE = random.choice(tts_list)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(VOICE_CHANNEL_ID)
    if channel is None or not isinstance(channel, discord.VoiceChannel):
        print(f"Voice channel with ID {VOICE_CHANNEL_ID} not found or is not a voice channel.")
        return

    vc = await channel.connect()

    if vc.is_connected():
        # Choose a random TTS message
        TTS_MESSAGE = random.choice(tts_list)
        
        # Generate TTS audio
        tts = gTTS(TTS_MESSAGE)
        tts.save("tts.mp3")

        # Play the TTS message in the voice channel
        vc.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: print('Finished playing TTS message'))

        # Wait until the message is played
        while vc.is_playing():
            await asyncio.sleep(1)
        
        # Disconnect from the voice channel
        await vc.disconnect()
    else:
        print("Failed to connect to the voice channel.")

# Run the bot
client.run(TOKEN)
