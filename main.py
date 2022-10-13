import random

import discord

import time

from discord.ext import tasks

TOKEN = 'Classified'

client = discord.Client()

@client.event
async def on_ready():


    print("{0.user} is online, brah!".format(client))

    seconds = time.time()
    local = time.localtime(seconds)

    awesometime = str(local.tm_hour) + ":" + str(local.tm_min)









@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    uppercaseusername = username.upper()
    user_message = str(message.content)

    if user_message.lower() == "go":
        @tasks.loop(seconds=5)  # task runs every 60 seconds
        async def on_ready():
            channel = client.get_channel("classified")  # channel ID goes here
            await message.channel.send("zyzz")















    if message.author == client.user:
        return

    if user_message.lower() == "zyzz4life":
        await message.channel.send(f'WHATS GOOD {uppercaseusername} !!! IF YOU NEED SOME HELP GETTING STARTED, JUST TYPE IN !help FOR SOME TIPS. CHEERS MATE')
        return

    if user_message.lower() == "!help":
        await message.channel.send(f"""Don't sweat it {username}, here's a list of commands brah: \n
!help - Just do this command to get a list of commands brah \n
!motivation - We all need motivation at times, brah. Just type this one in for a quick generic positive quote from me\n
!mirin - Just enter this one into the chat for some sweet Zyzz pics.. they're phenomenal mate \n
""")


    if user_message.lower() == "!mirin":
        pics_list = ['https://i.imgur.com/hltL23z.jpeg', "https://i.imgur.com/qJkJmFq.jpeg",
                                   'https://i.imgur.com/9vjJ5KC.jpeg', 'https://i.imgur.com/Icuo2y2.jpeg',
                                   'https://i.imgur.com/voLY5tu.jpeg', 'https://i.imgur.com/cWAEyNw.jpeg',
                                   'https://i.imgur.com/5BZmFAk.png', 'https://i.imgur.com/UIv6rn2.jpeg',
                                   'https://i.imgur.com/PesyiXk.jpeg', 'https://i.imgur.com/myfjrfH.jpeg',
                                   'https://i.imgur.com/1RdKKn8.jpeg', 'https://i.imgur.com/ecDbDGe.jpeg',
                                   'https://i.imgur.com/ORjKnO4.jpeg', 'https://i.imgur.com/dGx3KY5.jpeg',
                                   'https://i.imgur.com/yq4DuXL.jpeg', 'https://i.imgur.com/cM8bF1I.jpeg',
                                   'https://i.imgur.com/bM9T1cB.jpeg', 'https://i.imgur.com/o2r8F3Y.jpeg',
                                   'https://i.imgur.com/vpWMQaA.jpeg', 'https://i.imgur.com/o1jgrgA.jpeg',
                                   'https://i.imgur.com/a6tBm5e.jpeg', 'https://i.imgur.com/xEuuT1I.jpeg',
                                   'https://i.imgur.com/I1Jsjuk.jpeg', 'https://i.imgur.com/hojkTh1.jpeg',
                                   'https://i.imgur.com/U2UyciV.jpeg', 'https://i.imgur.com/arFsjgt.jpeg',
                                   'https://i.imgur.com/1olnW3T.jpeg', 'https://i.imgur.com/4v63EjH.jpeg',
                                   'https://i.imgur.com/SxOvxeB.jpeg', 'https://i.imgur.com/VFHlCW5.jpeg']

        random_pic = pics_list[random.randint(0,29)]
        embed = discord.Embed(title='YOU MIRIN BRAH???', color=discord.Color.green())
        embed.set_image(url=random_pic)
        await message.channel.send(embed=embed)

    if str(message.author) == "classified":
        await message.reply("classifiedgif", mention_author=True)

    if str(message.author) == "classified" or "classified":
        link = str(user_message.lower())
        giveaway = "https"
        if giveaway in link:
            await message.channel.send(user_message)





    if user_message.lower() == "!time":

        seconds = time.time()
        local = time.localtime(seconds)


        if local.tm_hour <= 12 and local.tm_min > 10:
            await message.channel.send("Of course brah! The time is " + str(local.tm_hour) + ":" + str(local.tm_min) + "AM")
        elif local.tm_hour > 12 and local.tm_min > 10:
            await message.channel.send("Of course brah! The time is " + str(local.tm_hour - 12) + ":" + str(local.tm_min) + "PM")
        elif local.tm_hour <= 12 and local.tm_min < 10:
            await message.channel.send("Of course brah! The time is " + str(local.tm_hour) + ":0" + str(local.tm_min) + "AM")
        elif local.tm_hour > 12 and local.tm_min < 10:
            await message.channel.send("Of course brah! The time is " + str(local.tm_hour - 12) + ":0" + str(local.tm_min) + "PM")








    if user_message.lower() == "!motivation":
        motivational_quotes = ["¨The first time I see a jogger smiling, I’ll consider it.¨- Joan Rivers",
                               "“All progress takes place outside the comfort zone.”- Michal Joan Bobak",
                               "¨Look in the mirror. That’s your competition.¨ – John Assaraf",
                               "¨Tough times don’t last. Tough people do.¨ – Robert H. Schuller",
                               "¨A feeble body weakens the mind.¨ – Jean-Jacques Rousseau",
                               "¨Put all excuses aside and remember this: You are capable.¨ – Zig Ziglar",
                               "¨Bodybuilding is much like any other sport. To be successful, you must dedicate yourself 100% to your training, diet and mental approach.¨ – Arnold Schwarzenegger",
                               "¨If we could give every individual the right amount of nourishment and exercise, not too little and not too much, we would have found the safest way to health.¨ — Hippocrates",
                               "¨Swimming is normal for me. I’m relaxed. I’m comfortable, and I know my surroundings. It’s my home.¨- Michael Phelps",
                               "“If you think lifting is dangerous, try being weak. Being weak is dangerous.” – Bret Contreras",
                               "¨There is a moment when you get older when your metabolism slows down and you don’t feel like working out any more, so you don’t want to keep yourself fit any more, but that’s your decision. Why should you be judged for it?¨ – Janet Jackson",
                               "¨The groundwork for all happiness is good health.¨ – Leigh Hunt",
                               "“The only place where success comes before work is in the dictionary.”- Vidal Sassoon",
                               "¨The human body is the best picture of the human soul.¨ – Ludwig Wittgenstein",
                               "¨Our bodies are our gardens – our wills are our gardeners.¨ – William Shakespeare",
                               " “The clock is ticking. Are you becoming the person you want to be?” – Greg Plitt",
                               "¨Reading is to the mind what exercise is to the body.¨- Joseph Addison",
                               "¨Exercise is king. Nutrition is queen. Put them together and you’ve got a kingdom.¨ – Jack LaLanne",
                               " ¨Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity.¨ – John F. Kennedy",
                               "“Whether you think you can, or you think you can’t, you’re right.” – Henry Ford",
                               " ¨There’s a lot of people in this world who spend so much time watching their health that they haven’t the time to enjoy it.¨- Josh Billings",
                               "¨Success is what comes after your stop making excuses.¨ – Luis Galarza",
                               "“The successful warrior is the average man, with laser-like focus.”- Bruce Lee",
                               "¨What’s important is to get into shape and then not to have to worry about it. I don’t want to get on stage and not being able to do something. Not being physically fit doesn’t work for me.¨ – Chris Cornell",
                               "¨Discipline is the bridge between goals and accomplishment.¨ – Jim Rohn",
                               "¨Here’s what I tell anybody and this is what I believe. The greatest gift we have is the gift of life. We understand that. That comes from our Creator. We’re given a body. Now you may not like it, but you can maximize that body the best it can be maximized.¨ – Mike Ditka",
                               "“You must expect great things of yourself before you can do them.”- Michael Jordan",
                               "¨The pain you feel today will be the strength you feel tomorrow.¨ – Arnold Schwarzenegger",
                               "¨I’m not a waif-y girl and never will be. I think it’s healthy when fitness experts encourage fitness rather than getting a certain body shape.¨- Sophia Bush",
                               "¨I wanted to get really fit. I wanted to lose some weight. So I’ve been doing Pilates and yoga, trying to lean out my body so I won’t be bulky.¨- Serena Williams",
                               "“Action is the foundational key to all success.”- Pablo Picasso",
                               "¨Setting goals is the first step into turning the invisible into the visible.¨ – Tony Robbins",
                               "¨Your body is the church where Nature asks to be reverenced.¨ – Marquis de Sade",
                               "“Things may come to those who wait, but only the things left by those who hustle.”- Abraham Lincoln",
                               "¨Get comfortable with being uncomfortable!¨ – Jillian Michaels",
                               "¨The only way for a rich man to be healthy is by exercise and abstinence, to live as if he were poor.¨- William Temple",
                               "“All our dreams can come true if we have the courage to pursue them.”- Walt Disney",
                               "¨Great works are performed, not by strength, but by perseverance.¨ – Samuel Johnson",
                               "“A champion is someone who gets up when they can’t.”- Jack Dempsey",
                               "“If something stands between you and your success, move it. Never be denied.”- Dwayne Johnson"]

        await message.channel.send(motivational_quotes[random.randint(0, 39)])
        return






client.run(TOKEN)