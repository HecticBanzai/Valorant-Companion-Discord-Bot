import os
from dotenv import load_dotenv

import discord
from discord import option
from discord.utils import get

import valorant

load_dotenv()

discord_client = discord.Bot(debug_guilds=[os.getenv("TEST_GUILD")])

valorant_client = valorant.Client(os.getenv("DEVELOPMENT_KEY"), locale=None)

@discord_client.event
async def on_ready():
	print("Valorant Bot is up and running!")
	print("-------------------------------")
 
@discord_client.slash_command(name="get-skins", description="Get skins")
@option(name="skin_name", description="Get all weapons of skin")
async def get_skins(ctx: discord.ApplicationContext, skin_name: str):
	skins = valorant_client.get_skins()
	name = skin_name
	results = skins.find_all(name=lambda x: name.lower() in x.lower())

	response = "\nResults: "

	for skin in results:
		response += f"\t{skin.name.ljust(21)} ({skin.localizedNames['en-US']})"

	await ctx.respond(response)
	
discord_client.run(os.getenv("TOKEN"))