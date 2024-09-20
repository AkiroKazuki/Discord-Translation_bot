import os
import discord
from discord.ext import commands
from google.cloud import translate_v2 as translate
from google.api_core.exceptions import GoogleAPICallError, InvalidArgument

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Inisialisasi client penerjemah Google Cloud
translate_client = translate.Client()

# Menyimpan status channel yang menggunakan terjemahan otomatis dan bahasa targetnya
auto_translate_channels = {}

# Fungsi logging sederhana
def log_message(message):
    print(f"{message.author} in {message.channel}: {message.content}")

@bot.command()
async def translate_on(ctx, target_language="en"):
    if ctx.channel.id in auto_translate_channels:
        await ctx.send("Automatic translation is already enabled for this channel.")
    else:
        auto_translate_channels[ctx.channel.id] = target_language
        await ctx.send(f"Automatic translation enabled for this channel. Target language set to '{target_language}'.")

@bot.command()
async def translate_off(ctx):
    if ctx.channel.id in auto_translate_channels:
        del auto_translate_channels[ctx.channel.id]
        await ctx.send("Automatic translation disabled for this channel.")
    else:
        await ctx.send("Automatic translation is not enabled for this channel.")

@bot.command()
async def set_language(ctx, target_language):
    if ctx.channel.id in auto_translate_channels:
        auto_translate_channels[ctx.channel.id] = target_language
        await ctx.send(f"Target language updated to '{target_language}'.")
    else:
        await ctx.send("Please enable automatic translation for this channel first using `!translate_on`.")

@bot.command()
async def translate(ctx, target_language, *, text):
    try:
        translation = translate_client.translate(text, target_language=target_language)
        translated_text = translation['translatedText']
        embed = discord.Embed(title="Manual Translation", color=0x00ff00)
        embed.add_field(name="Original", value=text, inline=False)
        embed.add_field(name="Translated", value=translated_text, inline=False)
        await ctx.send(embed=embed)
    except GoogleAPICallError as e:
        await ctx.send(f"An error occurred while calling the translation API: {e.message}")
    except InvalidArgument as e:
        await ctx.send(f"Invalid argument provided to the translation API: {e.message}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    log_message(message)

    channel_id = message.channel.id

    if channel_id in auto_translate_channels:
        try:
            detected_lang = translate_client.detect_language(message.content)['language']
            target_language = auto_translate_channels[channel_id]

            if detected_lang != target_language:
                translation = translate_client.translate(message.content, target_language=target_language)
                translated_text = translation['translatedText']

                embed = discord.Embed(title="Automatic Translation", color=0x00ff00)
                embed.add_field(name="Original", value=message.content, inline=False)
                embed.add_field(name="Translated", value=translated_text, inline=False)
                await message.channel.send(embed=embed)
        except GoogleAPICallError as e:
            await message.channel.send(f"An error occurred while calling the translation API: {e.message}")
        except InvalidArgument as e:
            await message.channel.send(f"Invalid argument provided to the translation API: {e.message}")
        except Exception as e:
            await message.channel.send(f"An unexpected error occurred: {e}")

    await bot.process_commands(message)

bot.run("Discord Bot token")  # ganti sama token bot discord
