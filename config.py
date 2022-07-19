import json

with open("env.json") as env:

    priv = json.load(env)
    
    link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    TOKEN = str(priv["MATH_VAR"])

    GUILD_ID = int(priv["GUILD_VAR"])

    OWNER_ID = int(priv["OWNER_VAR"])

with open("./extension/choice.json") as choices:

    choice = json.load(choices)

    _prefix = dict(choice["_prefix"])

    _si_unit = dict(choice["_si_unit"])

    _curve = dict(choice["_curve"])

    _four_side = dict(choice["_quad"])

    _tri = dict(choice["_tri"])

    _cylinder = dict(choice["_cylinder"])

    _cone = dict(choice["_cone"])

    _linearOperation = dict(choice["_straLine"])
    
    _setOperation = dict(choice["_setOperation"])
    
    _quadOperation = dict(choice["_quadOperation"])
    
    _factor = dict(choice["_factor"])
    
    _multiple = dict(choice["_multiple"])