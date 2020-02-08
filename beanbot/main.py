import discord, os, random
import praw as reddit

from dotenv import load_dotenv
load_dotenv()           #load environmentals




r = reddit.Reddit(client_id=os.getenv("REDDIT_CLIENT"), client_secret=os.getenv('REDDIT_SECRET'), password=os.getenv('REDDIT_PASSWORD'), user_agent='bean bot by /u/DavZOfficial', username='DavZOfficial')
print("Connected to Reddit")
beans = r.subreddit('BeansInThings')
client = discord.Client()

@client.event
async def on_ready():
    print('Connected to discord as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(" with some beans"))   #initialised bot


def find_beans(search_term = ""):
    if search_term == "":
        return beans.random()
    else:
        print("searching for ", search_term)
        posts = beans.search(search_term, sort="relevant", limit=20)   #random of 10 posts in a search
        randnum = random.randint(1,20)
        for i, reddit_post in enumerate(posts):   #quickly chooses random post inside
            if randnum == i:
                print(reddit_post.url)
                if "v.redd.it" not in reddit_post.url:
                    if reddit_post.url != None:
                        return reddit_post
                    else:
                        return find_beans(search_term)
                else:
                    return find_beans(search_term)   #reiterate and do process again cos i cbs now
        else:
            #search for the very first image and if that doesnt work then just say didnt find random beans
            posts = beans.search(search_term, sort="relevant", limit=1)
            for post in posts:
                print(post.url)   
                if post.url == None:
                    return None
                else:                                               #for loop that doesnt actually loop
                    return post



random_titles = ["what? are you not satisfied with the number of commands?", "Yeah thats it. Did you expect more?", "what friggin else would you want in this bot?", "ok we get it you thought there was more. There isnt."]
random_descriptors = ["idek bro", "oh.... uhh....", "wait what the hell that was it? ok then...", "*disappointment ensues*", "bean is not proud", "no", "just use the bot or something its there to serve one singular purpose in it's life."]

random_nothing = ["No beans today", "No beans were found", "*Lack of bean*", "*lack of beanage*", "disappointed, there are no beans", "ERROR: NO BEANS", "Beans not detected", "beans are invisible or something", "beans dont0 work", "for some ungodly reason the stupid post that i chose randomly chose not to show us some beans. What a scam.", "beanage 'nt", "WHERE ARE THE BEANS???", "i swear to god "]


def random_hex():
    return random.randint(0, 16777216)

@client.event
async def on_message(message):
    if message.author == client.user:
        return                          #bot doesnt talk to itself

    if len(message.content.strip()) > 19:
        return

    if message.content.strip().lower().startswith('bean'):
        print(message.content.strip())

        if message.content.strip().lower().strip() == "bean help":
            embed=discord.Embed(title="Bean Bot", description="Commands:", color=random_hex())
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/welcome-to-bloxburg/images/5/58/CanofBeans.png/revision/latest?cb=20171202024558")
            embed.add_field(name="Bean |types of beans|", value="Shows a picture of beans based on the type of beans you specify. ", inline=False)
            embed.add_field(name="Beans", value="Shows a random picture of beans", inline=True)
            embed.add_field(name="Bean Help", value="Display assistance when trying to make beans pop up.", inline=True)
            embed.add_field(name=random.choice(random_titles), value=random.choice(random_descriptors))
            embed.set_footer(text="Made by Davit Gogiberidze (@Dave#8425) for We Suck at Producing")
            await message.channel.send(embed=embed)
            return

        elif message.content.strip().lower() == "beans":    #if you say only bean then do this
            post = find_beans()
            if post == None:
                embed=discord.Embed(title="Bean Bot", description="uh", color=random_hex())
                embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/welcome-to-bloxburg/images/5/58/CanofBeans.png/revision/latest?cb=20171202024558")
                embed.add_field(name="bruh", value=random.choice(random_nothing), inline=False)
                embed.set_footer(text="Made by Davit Gogiberidze (@Dave#8425) for We Suck at Producing")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(post.url)
            return

        elif message.content.strip().lower().startswith("bean"):          #if you say bean then you automatically assume you search for something. bean by itself doesnt work
            post = find_beans(message.content.strip().lower().split("bean", 1)[1].strip())
            if post == None:
                embed=discord.Embed(title="Bean Bot", description="uh", color=random_hex())
                embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/welcome-to-bloxburg/images/5/58/CanofBeans.png/revision/latest?cb=20171202024558")
                embed.add_field(name="bruh", value=random.choice(random_nothing), inline=False)
                embed.set_footer(text="Made by Davit Gogiberidze (@Dave#8425) for We Suck at Producing")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(post.url)
            return
            


client.run(os.getenv("DISCORD_TOKEN"))
