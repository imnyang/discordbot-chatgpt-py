import os
import openai
import discord
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Bot(intents=intents)


def handle_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "OpenAI Discord Bot"},
            {"role": "user", "content": f"{message}"},
       ]
    )

    print(response)
    response = response.choices[0].message.content;
    return response


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.command()
async def chatgpt(ctx, answer:str):
    response = handle_response(answer)
    await ctx.respond(response)

try:
    client.run(DISCORD_BOT_TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
