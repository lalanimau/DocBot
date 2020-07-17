#coding: UTF-8
import re
from docbot.bot import respond_to
from docbot.bot import listen_to


@respond_to('hello$', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello user!')


@respond_to('^reply_webapi$')
def hello_webapi(message):
    message.reply_webapi('hey there!', attachments=[{
        
    }])


@respond_to('^reply_webapi_not_as_user$')
def hello_webapi_not_as_user(message):
    message.reply_webapi('hello!', as_user=False)


@respond_to('hello_formatting')
def hello_reply_formatting(message):
    # Format message with italic style
    message.reply('_hello_ user!')


@listen_to('hello$')
def hello_send(message):
    message.send('hello team!')


@listen_to('hello_decorators')
@respond_to('hello_decorators')
def hello_decorators(message):
    message.send('hello!')

@listen_to('hey!')
def hey(message):
    message.react('eggplant')


@listen_to('start a thread')
def start_thread(message):
    message.reply('Started a thread', in_thread=True)

@respond_to('say hi to me')
def direct_hello(message):
    message.direct_reply("Hi")

