# Config

This module is a binding to [pydantic-settings](https://github.com/pydantic/pydantic-settings) and adds watchers for config sources with [watchfiles](https://github.com/samuelcolvin/watchfiles). Supports both, synchronously (threads) and asynchronously (tasks), modes. Every source have own watcher.

Watchers created automatically for all sources (detected by **SettingsConfigDict** arguments with `_file` ends).

## How to use
```Python
from time import sleep

from dublib.engine.config import Config
from pydantic import MySQLDsn
from pydantic_settings import BaseSettings

class ConfigModel(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive = True,
        env_file = ".env",
    )

    DATABASE_URL: MySQLDsn
    IS_DEBUG: bool = False

config = Config(ConfigModel) 
config.watch_all()

print(config.data.IS_DEBUG) # Value at script start moment.
sleep(10) # Work simulation. Edit value in .env in this time.
print(config.data.IS_DEBUG) # Value after editing.
```

All you need to use this module asynchronously is to run `watch_all_async()` instead `watch_all()`.

## Members
```{eval-rst}
.. automodule:: dublib.engine.config
	:members:
```