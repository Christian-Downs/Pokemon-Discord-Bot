from http.client import responses
import discord
from numpy import true_divide

import requests

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()
games = []
gameStarted = False 
pokemonChoosen = False
userPokemon = ""
user = ''


@bot.event
async def on_reaction_add(reaction, user,message):
    print(reaction)
    print(message)


@bot.event
async def on_message(message):
    currentUser = message.author
    if(currentUser.name != 'POKEMON' ):
        global gameStarted
        global pokemonChoosen
        global userPokemon
        global user
        #print(message)
        #print(gameStarted)
        channel = message.channel
        if message.content == "$It's Battel Time":
            user = currentUser
            #print ('testers')
            
            await channel.send("Enter your pokemon!")
            
            #def check(reaction, user):
            #    print("looking")
            #    return user == message.author and str(reaction.emoji) == '👍'
            #
            #try:
            #    reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)

            #except TimeoutError:
            #    print("timeout")
            #    await channel.send('👎')
            #else:
            #    print("tumbsUp")
            #    await channel.send('👍')
            
            gameStarted = True
        elif currentUser == user:
            if pokemonChoosen:
                print('test')
            elif gameStarted:
                api_url = "https://pokeapi.co/api/v2/pokemon/" + message.content
                response = requests.get(api_url)
                if (response == "Not Found"):
                    await channel.send("Pokemon not found")
                else:
                    #print(response.json())
                    #print(response.json()['sprites']['front_default'])
                    pokemonChoosen = True
                    userPokemon = message.content
                    sentMessage = await channel.send(response.json()['sprites']['front_default'])
                    #print(sentMessage)
                    #sentMessage = channel.fetch_message(sentMessage.id)
                    print(sentMessage)
                    await sentMessage.add_reaction('🅰️')
                    await sentMessage.add_reaction('🅱️')
                    #await sentMessage.add_reaction('C')
                    #await sentMessage.add_reaction('D')



bot.run(DISCORD_TOKEN)



