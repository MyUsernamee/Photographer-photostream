import dotenv
import discord
import os
import convert

dotenv.load_dotenv()
output_directory = os.getenv("OUTPUT")
token = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user or message.channel.name != "photos":
        return

    # Get the attached photo, if there is none, return
    if message.attachments:
        for attachment in message.attachments:
            for file_type in convert.supported_formats:
                if attachment.filename.lower().endswith(file_type):

                    if convert.convert_image(attachment.url, output_directory, file_type):
                        await message.add_reaction("👍")
                    else:
                        await message.add_reaction("👎")
                        # Send the user a message in direct messages saying that the conversion failed
                        await message.author.send(f"Conversion failed for {attachment.url}")
                        return

bot.run(token)