# gu Documentation

A sample configuration file: [config.sample.yml](https://github.com/outloudvi/gu/blob/master/config.sample.yml)

## Finding the configuration file

### Format

The format for the configuration file is [YAML](https://yaml.org/).

### Default filename & location

The default configuration filename is `gu.yml`.

According to [XDG spec](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html), we will find this file in these directories, in:
* `$XDG_CONFIG_HOME/gu.yml`
* `$HOME/.config/gu.yml`
* `/home/{username}/.config/gu.yml` (for non-root) or `/root/.config/gu.yml` (for root)

You can use `--conf path/to/conf.yml` to use a custom configuration file.

## Global settings

``` yaml
globals:
  prefer: telegram  #The preferred sender
```

## Sender settings

### Stdout

(No config here.)

### Telegram

``` yaml
senders:
  telegram:
    username_or_userid: 23333  # Username or chat id
    bot_token: 23333:token     # Bot token
    parse_mode: markdown       # (optional) Parse mode of the message
```