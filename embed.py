from urllib.parse import urlsplit, parse_qs
import discord

class EMBED:
    def __init__(self, title, description, nom_fonction=None, logo=None, color=0x1f6e9e):
        self.embed_title = title
        self.embed_description = description
        self.embed_nom_fonction = nom_fonction
        self.embed_logo = logo
        self.embed_color = color
        self.embed = discord.Embed(title= self.embed_title, url= "https://myges.fr", description= self.embed_description, color= self.embed_color)

    def create(self):
        self.embed.set_author(name=f"ESGI | {self.embed_nom_fonction}", icon_url= self.embed_logo)
        self.embed.set_thumbnail(url="https://www.sciences-u-lyon.fr/images/2020/03/myges.png")
        self.embed.set_footer(text="Made by DAVE")

    def add_field(self, name, value, inline=True):
        self.embed.add_field(name=name, value=value, inline=inline)
        
    def to_dict(self):
        return self.embed.to_dict()