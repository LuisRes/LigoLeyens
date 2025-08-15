import discord
import os
import randomizer
from discord.ext import commands
import io

#TODO
#END GRACEFULLY IN CASE OF SUDDEN CLOSE
#FIX IMAGE LOADING IN CASE OF LATENCY ERROR
#CHECK FOR POSSIBLE LOCALE FIXES
#ADD ABREVIATIONS FOR ROLES

TOKEN = os.getenv("LIGOLEYENS_TOKEN")

if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in environment variables.")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

roles = ['top', 'jungle', 'mid', 'adc', 'support']

@bot.event
async def on_ready():
    print('Logged in as {0}'.format(bot.user))
    
@bot.command()
async def build(ctx, role: str = None):
    role = role.lower()

    if role is None:
        await ctx.send("Rol no incluido, Ejemplo: `!build top`")
        return
    elif role not in roles:
        await ctx.send("Rol no valido, Roles validos: top, jungle, mid, adc, support")
        return

    try:
        image_bytes = await randomizer.get_build_async(role)
    except Exception as e:
        await ctx.send(f"Error generating build: {e}")
        return

    # Send screenshot as a Discord file
    await ctx.send(file=discord.File(io.BytesIO(image_bytes), filename="build.png"))

print(repr(TOKEN))
bot.run(TOKEN)