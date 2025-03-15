import discord
from vinc import calculate_vinc

TOKEN = 'TOKEN'
TIMEOUT = 1200  # in seconds

intents = discord.Intents.default()
client = discord.Client(intents=intents)

#Sample input
# !vinc
# John|Jake,1|James,3
# Jake|John,3|James,2
# James|John,3|Jake,2

@client.event
async def on_ready():
    #do nothing.
    pass

@client.event
async def on_message(message):
    if not message.author.bot and message.content.startswith("!help"):
        await message.channel.send(get_help_text())
        return
    if message.author.bot or not(message.content.startswith("!vinc")):
        return
    lines = message.content.split("\n")
    results = ""
    for line in lines[1:]:
        character = parse_line(line)
        vinc = calculate_vinc(character)
        results += format_as_line(vinc) + "\n"
    await message.channel.send(results)

def parse_line(line):
    character = []
    split = line.split("|")
    character.append(split[0])
    pairs = []
    for other_character in split[1:]:
        pairs.append(other_character.split(","))
    character.append(pairs)
    return character

def format_as_line(character):
    line = character[0]
    for other_character in character[1:]:
        line += "|" + other_character[0] + "," + other_character[1]
    return line

def get_help_text():
    return "Usage: \n!vinc\nJohn|Jake,1|James,3\nJake|John,3|James,2\nJames|John,3|Jake,2\nThis will calculate Vinc for a pack of three - where John's got 1 Vinc with Jake and 3 with James, Jake has 3 with John and 2 with James, and James has 3 with John and 2 with Jake."

client.run(TOKEN)