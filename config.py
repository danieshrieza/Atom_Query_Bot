import json
import discord

with open("env.json") as env:

    private = json.load(env)

    LINK = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    TOKEN = str(private["MATH_VAR"])

    GUILD_ID = discord.Object(int(private["GUILD_VAR"]))

    OWNER_ID = int(private["OWNER_VAR"])

    IMAGE_LINK = str(private["IMAGE_LINK"])

with open("./option.json") as options:

    choice = json.load(options)

    _prefix = dict(choice["_prefix"]).items()

    _si_unit = dict(choice["_si_unit"]).items()

    _circle = dict(choice["_circle"]).items()

    _sphere = dict(choice["_sphere"]).items()

    _square = dict(choice["_square"]).items()

    _cube = dict(choice["_cube"]).items()

    _triangle = dict(choice["_triangle"]).items()

    _pyramid = dict(choice["_pyramid"]).items()

    _cylinder = dict(choice["_cylinder"]).items()

    _cone = dict(choice["_cone"]).items()

    _linear = dict(choice["_linear"]).items()

    _set_operation = dict(choice["_set_operation"]).items()

    _quadratic = dict(choice["_quadratic"]).items()

    _trigonometric_ratio = dict(choice["_trigonometric_ratio"]).items()
