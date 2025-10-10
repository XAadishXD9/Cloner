import discord
from discord.ext import commands
import asyncio

# === BOT SETTINGS ===
VOICE_CHANNEL_ID = 1406561957024370848  # your voice channel ID
PREFIX = "!"
TOKEN = "YOUR_BOT_TOKEN"  # paste your real Discord bot token here

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    # Automatically join your specific voice channel
    for guild in bot.guilds:
        channel = guild.get_channel(VOICE_CHANNEL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            try:
                if not guild.voice_client:
                    await channel.connect()
                    print(f"🎧 Connected to voice channel: {channel.name}")
                else:
                    print(f"Already connected to: {guild.voice_client.channel.name}")
            except Exception as e:
                print(f"❌ Could not connect: {e}")
        else:
            print("❌ Voice channel not found or invalid ID")

    # Stay alive 24/7
    while True:
        await asyncio.sleep(60)

# === COMMANDS ===

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel.name} ✅")
    else:
        await ctx.send("❌ You’re not in a voice channel!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Left the voice channel 👋")
    else:
        await ctx.send("I’m not connected to any voice channel.")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! I’m online and running 24/7.")

bot.run(TOKEN)
