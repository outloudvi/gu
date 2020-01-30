import yaml
from os import environ
from os import path


def read_from_env(name):
    return environ[name] if name in environ else None


def get_config_default_path():
    # Goes w/ XDG spec
    if read_from_env("XDG_CONFIG_HOME"):
        return path.join(read_from_env("XDG_CONFIG_HOME"), "gu.yml")
    elif read_from_env("HOME"):
        return path.join(read_from_env("HOME"), ".config", "gu.yml")
    else:
        import getpass
        username = getpass.getuser()
        if username == "root":
            return "/root/.config/gu.yml"
        else:
            return "/home/{}/.config/gu.yml".format(username)


def read_config(filename=get_config_default_path()):
    try:
        with open(filename, "r") as conffile:
            return yaml.load(conffile, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("[WARN] Config file is not found.")
        return {}
    except:
        print("[WARN] Config file is not readable.")
        return {}
