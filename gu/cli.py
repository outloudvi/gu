from gu import config
from argparse import ArgumentParser
from importlib import import_module
from gu import sender

CONFIG = {
    "globals": {
        "prefer": "telegram"
    }
}


def conf(*arg, default=None):
    global CONFIG
    pointer = CONFIG
    for i in arg:
        if i in pointer:
            pointer = pointer[i]
        else:
            return default
    return pointer


def prepare(config_filename=""):
    global CONFIG
    if config_filename == "":
        CONFIG.update(config.read_config())
    else:
        CONFIG.update(config.read_config(config_filename))


def main():
    parser = ArgumentParser(
        description='CLI notification / message sending tool')
    parser.add_argument('text', type=str,
                        help='text message to send')
    parser.add_argument('--conf', type=str, nargs='?', default='',
                        help='config file to use')
    args = parser.parse_args()
    prepare(args.conf)
    sender_name = conf("globals", "prefer")
    sender_class_in_use = getattr(sender, sender_name.capitalize() + "Sender")
    send = sender_class_in_use(conf("senders", sender_name, default={}))
    if not send.validateParams():
        print("[EMERG] Bad config for {} sender".format(sender_name))
    send.sendText(args.text)


if __name__ == "__main__":
    main()
