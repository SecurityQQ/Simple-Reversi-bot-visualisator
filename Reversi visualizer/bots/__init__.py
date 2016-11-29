"""Bots module"""

from os import walk

__all__ = list(map(lambda x: x[:-3], list(walk('bots/'))[0][2]))

def turn(color, bot, field):
    exec('import bots.bot%s' % bot)
    return eval('bots.bot%s.make_turn(field, color)' % bot)

def name(botid):
    exec('import bots.bot%i' % botid)
    bot = eval('bots.bot%i' % botid)
    name = bot.__doc__
    if name is None:
        name = bot.make_turn.__doc__
        if name is None:
            name = '[неизвестный бот]'
        
    return name.strip()
