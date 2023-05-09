import lightbulb
import hikari
plugin = lightbulb.Plugin('character_info', 'info for characters')


@plugin.command
@lightbulb.option('character', 'what character', choices=['medusa', 'chimera', 'siren', 'theseus', 'perseus'])
@lightbulb.command('character_info', 'info for characters')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cinfo(ctx):
  bot = ctx.app
  if ctx.options.character == 'medusa':
    embed = hikari.Embed(
        title="Medusa",
        description="Can turn anyone she looks like into stone. "
      )
    embed.set_image("././character_images/medusa.jpg")
    await ctx.respond(embed)
  elif ctx.options.character == 'chimera':
    embed = hikari.Embed(
        title="Chimera",
        description="A fire breathing monster. Depicted as a lion"
      )
    embed.set_image("././character_images/chimera.jpg")
    await ctx.respond(embed)
  elif ctx.options.character == 'siren':
    embed = hikari.Embed(
        title="Siren",
        description="Human like beings with alluring voices. "
      )
    embed.set_image("././character_images/siren.jpg")
    await ctx.respond(embed) 
  elif ctx.options.character == 'theseus':
    embed = hikari.Embed(
        title="Theseus",
        description="Theseus was the mythical king and founder-hero of Athens."
      )
    embed.set_image("././character_images/theseus.jpg")
    await ctx.respond(embed) 
  elif ctx.options.character == 'perseus':
    embed = hikari.Embed(
        title="Perseus",
        description="Perseus is the legendary founder of Mycenae and of the Perseid dynasty. He was, alongside Cadmus and Bellerophon, the greatest Greek hero and slayer of monsters before the days of Heracles."
      )
    embed.set_image("././character_images/perseus.jpg")
    await ctx.respond(embed) 
def load(bot):
  bot.add_plugin(plugin)