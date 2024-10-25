import os
import json
import logging
import logging.config
from pathlib import Path

__parent = Path(__file__).parent


def __get_filenames(config: dict) -> list:
    handlers: dict = config.get("handlers", {})
    return [v["filename"] for v in handlers.values() if "filename" in v]


def __set_permissions(filename: str, dir_permissions: int, file_permissions: int):
    filename: Path = Path(filename)
    umask = os.umask(0)
    parent = filename.parent
    parent.mkdir(parents=True, exist_ok=True, mode=dir_permissions)
    filename.touch(mode=file_permissions, exist_ok=True)
    os.umask(umask)


def getLogger(name: str,
              config_path: Path = __parent/"defaultConf.json",
              config: dict[str] = None,
              dir_permissions: int = 0o777,
              file_permissions: int = 0o777) -> logging.Logger:
    config = config or json.load(config_path.open())
    for filename in __get_filenames(config):
        __set_permissions(filename, dir_permissions, file_permissions)
    logging.config.dictConfig(config)
    return logging.getLogger(name)
