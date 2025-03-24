"""Dynaconf settings.

Super simple way to safely use variables.
from conf.config import conf

# get value from environment, parameters.toml, or secrets.toml or .env
print(conf['variable'])

# use this to reload once updated files
conf.reload()

"""

from dynaconf import Dynaconf

conf = Dynaconf(envvar_prefix=False,
                load_dotenv=True,
                settings_files=['conf/parameters.toml',
                                '.secrets.toml'])
#  can also use validators=[] to ensure some parameter meets a condition

# `envvar_prefix` = export envvars with `export FOO=bar`.
# `settings_files` = Load these files in the order.
