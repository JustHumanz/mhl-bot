import telebot,os,time,re,subprocess

bot = telebot.TeleBot("725295845:AAHsEoRjWgtFi0GACKX-r3JOSpZeKp_1hXU")
chatid = "386788173"


@bot.message_handler(commands=['solver'])
def handle_message(message):

    sol = subprocess.check_output('cat solver.txt',shell=True)
    bot.reply_to(message, "Solver List: \n"+str(sol.decode('utf-8').rstrip("\n")))


bot.infinity_polling(True)
