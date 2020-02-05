import discord, os, random
import praw as reddit

from dotenv import load_dotenv
load_dotenv()           #load environmentals




r = reddit.Reddit(client_id='t3SwJQkjzB7hoQ', client_secret=os.getenv('REDDIT_SECRET'), password=os.getenv('REDDIT_PASSWORD'), user_agent='bean bot by /u/DavZOfficial', username='DavZOfficial')
print("Connected to Reddit")
beans = r.subreddit('BeansInThings')
client = discord.Client()

@client.event
async def on_ready():
    print('Connected to discord as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(" with some beans"))   #initialised bot

@client.event
async def on_message(message):
    if message.author == client.user:
        return                          #bot doesnt talk to itself

    if message.content.strip().lower().startswith('bean'):
        print(message.content.strip())

        if message.content.strip().lower() == "beans":    #if you say only bean then do this
            post = beans.random()
            embeded = discord.Embed(title="", value="huh?")
            embeded.set_image(url=post.url)
            await message.channel.send(embed=embeded)

        elif message.content.startswith("bean"):          #if you say bean then you automatically assume you search for something. bean by itself doesnt work

            print("searching for ", message.content.split("bean", 1)[1].strip())

            posts = beans.search(message.content.split("bean", 1)[1].strip(), sort="relevance", limit=20)   #random of 10 posts in a search
            randnum = random.randint(1,20)
            for i, post in enumerate(posts):   #quickly chooses random post inside
                if randnum == i:
                    embeded = discord.Embed(title="", value= "huh")
                    embeded.set_image(url=post.url)

                    await message.channel.send(embed=embeded)
                    return
                else:
                    continue

            posts = beans.search(message.content.split("bean", 1)[1].strip(), sort="relevance", limit=1)   #selects only the first post just in case there arent enough posts
            print("gonna find the first post in search")
            for post in posts:                                                  #for loop that doesnt actually loop
                embeded = discord.Embed(title="", value= "huhh")
                embeded.set_image(url=post.url)
                await message.channel.send(embed=embeded)
                break   #only makes sure we run this once


client.run(os.getenv("DISCORD_TOKEN"))