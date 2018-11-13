#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
###################################################################################################################################################### 
# Autor: Carlos Baeza                                                                                                                                #
# Version: 1.0 Beta                                                                                                                                  #
# Fecha 20/08/2018                                                                                                                                   #
# Descripción: Este codigo es un bot simple para enviar mensajes de alertas desde PRTG a telegram, este BOT utiliza la cla Updater para manjear BOT.    #
# Primero, se definen algunas funciones del manejador. Luego, esas funciones se pasan a el despachador y registrado en sus respectivos lugares.      #                                                           
# Luego, el bot se inicia y se ejecuta hasta que presione Ctrl-C en la línea de comando.                                                             #                         
#                                                                                                                                                    #
#                                                                                                                                                    #
# https://api.telegram.org/bot123456:xxxxxxxxxxxx_xxxxxxxxx/sendMessage?chat_id=-2222222&text=my sample text"                      #
# La petición mencionada anteriormente contiene el token del bot, los numeros que estan luego del chat_id corresponden al ID del GRUPO donde se      # 
# desea mandar el mensaje de parte del bot y por ultimo el text es el mensaje que va a llegar a la aplicación!                                                        #
#                                                                                                                                                    #
#                                                                                                                                                    #
# Algunos Comentarios se entienden mejor en ingles por lo cual quedaron de esa manera, dejo un link de ejemplo de BOT                                #
#   https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py                                                                                                                                                 #
######################################################################################################################################################
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define algunos controladores de comandos. Estos suelen tomar los dos argumentos bot y actualizar
def start(bot, update):
    """Enviar un mensaje cuando se emita el comando /start"""
    update.message.reply_text('HOLA ESTE BOT ESTA CREADO SOLO PARA ENTREGAR ALERTAS!')

def ayuda(bot, update):
    """Enviar un mensaje cuando se emita el comando /ayuda"""
    update.message.reply_text('HOLA ESTE BOT ESTA CREADO SOLO PARA ENTREGAR ALERTAS, SI NECESITAS AYUDA CONTACTA A SOPORTE@TOC.CL')

def help(bot, update):
    """Enviar un mensaje cuando se emita el comando /help"""
    update.message.reply_text('HOLA ESTE BOT ESTA CREADO SOLO PARA ENTREGAR ALERTAS, SI NECESITAS AYUDA CONTACTA A SOPORTE@TOC.CL')

    
def echo(bot, update):
    """este comando hace que el BOT repita lo que cliente mando como mensaje"""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Errores de registro causados ​​por las actualizaciones."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """¡¡¡¡¡ INICIA TU BOT AQUI !!!!!"""
    # Crea EventHandler y pasale el token que te entragara BotFatherde, este token sera el asignado para tu bot  {Ejemplo Token: 270485614:AAHfiqksKZ8WmR2zSjiQ7_v4TMAKdiHm9T0}
    updater = Updater("TOKENID")
 
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start)) 
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ayuda", ayuda))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
	main()
