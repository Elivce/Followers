from discord.ext import commands
import subprocess
import threading
import discord
import asyncio
import aiohttp
import random
import socket
import ctypes
import time
import json
import ssl
import re
import os
import ctypes
from itertools import cycle

token = 'OTMwOTY2NzM4OTY5OTUyMzI3.Yd9kVw.PuYaTh6pjYRtWmVtGVWqZSVS1iM'
prefix = '.'

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
bot.remove_command('help')

Bacon = 887130741056610326
Premium = 927768111145426975 #rmg#0699 2/3/21
Premium_2 = [] #Brycee 12/11/21 908504740118265867
Classic =  []
Classic_2 = []

threads = 500 + 4
queue = []

administrator_ids = [824759664810000424,770020312535924796]
administrator_roles = [887130740150661173,887130740133879810]

roles = {
    '887130740133879809': '750',
    '932233622566633473': '250',
    '887130740133879808': '125',
    '887130740117094419': '100',
    '887130740117094418': '50', #Bacon V3
    '877807591156219914': '500',
    '908507340477706340': '200', 
    '908507057114730616': '100',
    '877756676483215410': '50',
    '877756309523546152': '0', #Brycee
    '926930939743993936': '250', 
    '926736167188193320': '25', #rny

}

database = {}
invites_database = {}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Twitchers"))

class tfollow_bot:

    def __init__(self, channel_id, amount):
        self.channel_id = str(channel_id)
        self.amount = int(amount)
        self.tokens = []
        self.load_tokens()
        random.shuffle(self.tokens)

    def load_tokens(self):
        self.tokens = open('tokens.txt', 'r').read().splitlines()

    def bot(self, i):
        try:
            _, _, token = self.tokens[i].split(':')
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36/zEQnQ9g8-55'
            origin = 'https://www.twitch.tv'
            content_type = 'text/plain;charset=UTF-8'
            client_id = 'kimne78kx3ncx6brgo4mv6wki5h1ko'
            authorization = f'OAuth {token}'
            accept_language = 'en-US'
            data = '[{"operationName":"FollowButton_FollowUser","variables":{"input":{"disableNotifications":false,"targetID":"%s"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3efee1acda90efdff9fef6e6b4a29213be3ee490781c5b54469717b6131ffdfe"}}}]' % self.channel_id
            content_length = len(data)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('gql.twitch.tv', 443))
                s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)
                s.sendall(f'POST /gql HTTP/1.1\r\nHost: gql.twitch.tv\r\nAuthorization: {authorization}\r\nUser-Agent: {user_agent}\r\nOrigin: {origin}\r\nContent-Type: {content_type}\r\nClient-Id: {client_id}\r\nAccept-Language: {accept_language}\r\nContent-Length: {content_length}\r\n\r\n{data}\r\n'.encode('utf-8'))
                s.recv(4096)
        except:
            pass

    def start(self):
        for i in range(self.amount):
            while True:
                if threading.active_count() < threads:
                    threading.Thread(target=self.bot, args=(i,)).start()
                    break
        while True:
            if threading.active_count() == 4:
                break
        return

class tfriend_bot:

    def __init__(self, channel_id, amount):
        self.channel_id = str(channel_id)
        self.amount = int(amount)
        self.tokens = []
        self.load_tokens()
        random.shuffle(self.tokens)

    def load_tokens(self):
        self.tokens = open('tokens.txt', 'r').read().splitlines()

    def bot(self, i):
        try:
            _, _, token = self.tokens[i].split(':')
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36/zEQnQ9g8-55'
            origin = 'https://www.twitch.tv'
            content_type = 'text/plain;charset=UTF-8'
            client_id = 'ymd9sjdyrpi8kz8zfxkdf5du04m649'
            authorization = f'OAuth {token}'
            accept_language = 'en-US'
            data = '[{"operationName":"FriendButton_CreateFriendRequest","variables":{"input":{"targetID":"%s"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"380d8b19fcffef2fd8654e524444055dbca557d71968044115849d569d24129a"}}}]' % self.channel_id
            content_length = len(data)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('gql.twitch.tv', 443))
                s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_SSLv23)
                s.sendall(f'POST /gql HTTP/1.1\r\nHost: gql.twitch.tv\r\nAuthorization: {authorization}\r\nUser-Agent: {user_agent}\r\nOrigin: {origin}\r\nContent-Type: {content_type}\r\nClient-Id: {client_id}\r\nAccept-Language: {accept_language}\r\nContent-Length: {content_length}\r\n\r\n{data}\r\n'.encode('utf-8'))
                _ = s.recv(4096).decode('utf-8')
                resp = s.recv(4096).decode('utf-8')
                if 'service error' in resp:
                    self.bot(i)
        except:
            pass

    def start(self):
        for i in range(self.amount):
            while True:
                if threading.active_count() < threads:
                    threading.Thread(target=self.bot, args=(i,)).start()
                    break
        while True:
            if threading.active_count() == 4:
                break
        return

def zoom():
    while True:
        try:
            task = queue.pop(0).split('|')
            if task[0] == 'tfollow':
                tfollow_bot(task[1], task[2]).start()
            elif task[0] == 'tfriend':
                tfriend_bot(task[1], task[2]).start()
        except:
            pass

threading.Thread(target=zoom).start()

async def status():
    while True:
        try:
            members = sum([len([member for member in guild.members if not member.bot]) for guild in bot.guilds])
            activity = discord.Activity(type=discord.ActivityType.watching, name=f'{members} members!')
            await bot.change_presence(activity=activity)
            await asyncio.sleep(300)
        except:
            pass

@bot.event
async def on_command_error(ctx, error: Exception):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        ctx.command.reset_cooldown(ctx)
        embed = discord.Embed(color=16776960, description='You are missing arguments required to run this command!')
        if ctx.channel.id == Bacon or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2: await ctx.send(embed=embed) 
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(color=16776960, description=f'{error}')
        if ctx.channel.id == Bacon or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2: await ctx.send(embed=embed) 

@bot.command()
async def bronze(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}help')
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            embed = discord.Embed(color=16776960)
            embed.add_field(name='Free Bronze', value=f'Put `dsc.gg/twitch=followers` in status for bronze once you remove the role will also be removed', inline=True)
            await ctx.send(embed=embed)
      else:
            await ctx.message.delete()

@bot.command()
async def help(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}help')
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            embed = discord.Embed(color=16776960)
            embed.add_field(name='Help', value=f'`{bot.command_prefix}help`', inline=True)
            embed.add_field(name='Twitch Info', value=f'`{bot.command_prefix}tinfo (channel)`', inline=True)
            embed.add_field(name='Twitch Followers', value=f'`{bot.command_prefix}tfollow (channel)`', inline=True)
            embed.add_field(name='Twitch Friend Req', value=f'`{bot.command_prefix}tfriend (channel)`', inline=True)
            embed.add_field(name='Follow Tasks', value=f'`{bot.command_prefix}tasks`', inline=True)
            embed.add_field(name='Owners & Server', value=f'`{bot.command_prefix}credits`', inline=True)
            embed.add_field(name='Free Bronze', value=f'`{bot.command_prefix}bronze`', inline=True)
            embed.set_thumbnail(url='https://cdn.vox-cdn.com/uploads/chorus_asset/file/19234624/03c_Glitch.gif')
            await ctx.send(embed=embed)
      else:
            await ctx.message.delete()

@bot.command()
async def credits(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}help')
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            embed = discord.Embed(color=16776960)
            embed.add_field(name='Credits & Invitation', value=f'Server: https://discord.gg/ADsJ6Frnth', inline=True)
            await ctx.send(embed=embed)
      else:
            await ctx.message.delete()

@bot.command()
async def tasks(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> .tasks')
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            embed = discord.Embed(color=16776960, description=f'`{len(queue)}` tasks in the queue!')
            await ctx.send(embed=embed)
      else:
            await ctx.message.delete()

tfollow_cooldown = []

@bot.command()
async def tinfo(ctx, channel):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}tinfo {channel}')
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            try:
                async with aiohttp.ClientSession() as session:
                    try:
                        channel_lower = channel.lower()
                        headers = {
                            'Client-Id': 'abe7gtyxbr7wfcdftwyi9i5kej3jnq',
                            'Accept': 'application/vnd.twitchtv.v5+json'
                        }
                        async with session.get(f'https://api.twitch.tv/kraken/users?login={channel_lower}', headers=headers) as r:
                            r = await r.json()
                            channel_id = r['users'][0]['_id']
                        async with session.get(f'https://api.twitch.tv/kraken/channels/{channel_id}', headers=headers) as r:
                            r = await r.json()
                            name = r['display_name']
                            followers = r['followers']
                            views = r['views']
                            logo = r['logo']
                    except:
                        embed = discord.Embed(color=16776960, description=f'Invalid twitch channel!')
                        await ctx.send(embed=embed)
                        return
                embed = discord.Embed(color=16776960)
                embed.set_thumbnail(url=f'{logo}')
                embed.add_field(name='Name', value=f'`{name}`', inline=True)
                embed.add_field(name='Channel ID', value=f'`{channel_id}`', inline=True)
                embed.add_field(name='Followers', value=f'`{followers}`', inline=True)
                embed.add_field(name='Channel Views', value=f'`{views}`', inline=True)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(color=16776960, description='An error has occured while attempting to run this command!')
                await ctx.send(embed=embed)
      else:
            await ctx.message.delete()

@bot.command()
@commands.cooldown(1, 30, type=commands.BucketType.user)
async def tfollow(ctx, channel, amount: int=None):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}tfollow {channel}' + (f' {amount}' if amount else ''))
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            try:
                max_amount = 0
                member_roles = [role.id for role in ctx.author.roles]
                for role in member_roles:
                    if f'{role}' in roles.keys():
                        max_amount += int(roles[f'{role}'])
                member = ctx.guild.get_member(ctx.author.id)
                for status in member.activities:
                    if isinstance(status, discord.CustomActivity):
                        if status.name == '[]':
                            max_amount += 0
                            break
                admin_roles = [role for role in ctx.author.roles if role.id in administrator_roles]
                if admin_roles or ctx.author.id in administrator_ids:
                    tfollow.reset_cooldown(ctx)
                    max_amount = len(open('tokens.txt', 'r').read().splitlines())
                if not amount:
                    amount = max_amount
                elif amount > max_amount:
                    amount = max_amount
                async with aiohttp.ClientSession() as session:
                    try:
                        channel_lower = channel.lower()
                        headers = {
                            'Client-Id': 'abe7gtyxbr7wfcdftwyi9i5kej3jnq',
                            'Accept': 'application/vnd.twitchtv.v5+json'
                        }
                        async with session.get(f'https://api.twitch.tv/kraken/users?login={channel_lower}', headers=headers) as r:
                            r = await r.json()
                            channel_id = r['users'][0]['_id']
                    except:
                        tfollow.reset_cooldown(ctx)
                        embed = discord.Embed(color=16776960, description=f'Invalid twitch channel!')
                        await ctx.send(embed=embed)
                        return
                position = len(queue) + 1
                embed = discord.Embed(color=16776960, description=f'Sending `{amount}` twitch followers to `{channel}`! (`{position}/{position}`)')
                await ctx.send(embed=embed)
                queue.append(f'tfollow|{channel_id}|{amount}')
            except:
                tfollow.reset_cooldown(ctx)
                embed = discord.Embed(color=16776960, description='An error has occured while attempting to run this command!')
                await ctx.send(embed=embed)
      else:
            tfollow.reset_cooldown(ctx)
            await ctx.message.delete()

@bot.command()
@commands.cooldown(1, 180, type=commands.BucketType.user)
async def tfriend(ctx, channel, amount: int=None):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}tfriend {channel}' + (f' {amount}' if amount else ''))
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == Bacon or ctx.author.id in administrator_ids or ctx.channel.id == Premium or ctx.channel.id == Premium_2 or ctx.channel.id == Classic or ctx.channel.id == Classic_2:
            try:
                max_amount = 0
                member_roles = [role.id for role in ctx.author.roles]
                for role in member_roles:
                    if f'{role}' in roles.keys():
                        max_amount += int(roles[f'{role}'])
                member = ctx.guild.get_member(ctx.author.id)
                for status in member.activities:
                    if isinstance(status, discord.CustomActivity):
                        if status.name == '..':
                            max_amount += 0
                            break
                admin_roles = [role for role in ctx.author.roles if role.id in administrator_roles]
                if admin_roles or ctx.author.id in administrator_ids:
                    tfriend.reset_cooldown(ctx)
                    max_amount = len(open('tokens.txt', 'r').read().splitlines())
                if not amount:
                    amount = max_amount
                elif amount > max_amount:
                    amount = max_amount
                async with aiohttp.ClientSession() as session:
                    try:
                        channel_lower = channel.lower()
                        headers = {
                            'Client-Id': 'abe7gtyxbr7wfcdftwyi9i5kej3jnq',
                            'Accept': 'application/vnd.twitchtv.v5+json'
                        }
                        async with session.get(f'https://api.twitch.tv/kraken/users?login={channel_lower}', headers=headers) as r:
                            r = await r.json()
                            channel_id = r['users'][0]['_id']
                    except:
                        tfriend.reset_cooldown(ctx)
                        embed = discord.Embed(color=16776960, description=f'Invalid twitch channel!')
                        await ctx.send(embed=embed)
                        return
                position = len(queue) + 1
                embed = discord.Embed(color=16776960, description=f'Sending `{amount}` twitch friend requests to `{channel}`! (`{position}/{position}`)')
                await ctx.send(embed=embed)
                queue.append(f'tfriend|{channel_id}|{amount}')
            except:
                tfriend.reset_cooldown(ctx)
                embed = discord.Embed(color=16776960, description='An error has occured while attempting to run this command!')
                await ctx.send(embed=embed)
      else:
            tfriend.reset_cooldown(ctx)
            await ctx.message.delete()
bot.run(token)
