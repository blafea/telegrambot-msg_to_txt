from telegram.ext import Updater, CommandHandler

def hello(bot, update):
    update.message.reply_text('hello, {}'.format(update.message.from_user.first_name))

def add(bot, update):
    try:
        sentence = update.message.text[5:]
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                file_name = sentence[:i]
                text = sentence[i+1:]
        file_name = './txt/' + file_name + '.txt'
        with open(file_name, 'w', encoding='UTF-8') as f:
            f.write(text)
        update.message.reply_text('create file done')
    except:
        update.message.reply_text('create file error')
    

updater = Updater('2138023839:AAGP18zoPWksT8TSCYhAkKW7ihbAiUTyImk', use_context=False)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('add', add))

updater.start_polling()
updater.idle()
