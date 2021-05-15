import telebot
import pandas as pd
import yaml

config = []

with open("config.yaml", 'r') as stream:
    try:
        d = yaml.safe_load(stream)
        for key, value in d.items():
            config.append(value)
    except yaml.YAMLError as exc:
        print(exc)

bot = telebot.TeleBot(config[0], parse_mode=None)
u = config[2]
yo = config[1]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, ":')")

# He utilizado este comando como forma de debug, así que no está pensado para su utilización.
# De todas maneras, lo he dejado porque nunca viene mal. Te aviso que su formato en el mensaje está un poco roto.
@bot.message_handler(commands=['checkgeneral']) 
def send_checkgeneral(message):
    if str(yo) == str(message.from_user.id):
        for x in u:
            msg = bot.reply_to(message, 'Procesando...')
            tabla = pd.read_html(x)
            df = pd.DataFrame(tabla[0])
            df.columns = ['Fecha', 'Linea', 'Estación', 'd', 'e', 'f', 'Saldo']
            df = df[['Fecha', 'Linea', 'Estación', 'Saldo']]
            bot.edit_message_text(df.to_string(), message.chat.id, msg.message_id)
    else:
        bot.reply_to(message, 'Quién eres tu0?!01?! - ' + str(message.from_user.id))

@bot.message_handler(commands=['check'])
def send_check(message):
    if str(yo) == str(message.from_user.id):
        for x in u:
            msg = bot.reply_to(message, 'Procesando...')
            tabla = pd.read_html(x)
            df = pd.DataFrame(tabla[0])
            df.columns = ['Fecha', 'Linea', 'Estación', 'd', 'e', 'f', 'Saldo']
            df1 = df.iloc[0]
            df1 = df1[['Fecha', 'Linea', 'Estación', 'Saldo']]
            tabla = '<pre>' + df1.to_string() + '</pre>'
            bot.edit_message_text(tabla, message.chat.id, msg.message_id, parse_mode='HTML')
    else:
        bot.reply_to(message, 'Quién eres tu0?!01?! - ' + str(message.from_user.id))

bot.polling()