from pyrogram import Client, filters

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"✉`{prefix_userbot}spam`"
ccomand = f" Начинает флудить сообщением, которое вы выбрали. Пример: `{prefix_userbot}spam 3 Telery - круто!`"


def command_spam(app):
    @app.on_message(filters.me & filters.command(["spam"], prefixes=prefix_userbot))
    def spam_message(_, message):
        _, count, *words = message.text.split()
        count = int(count)
        text = ' '.join(words)
        message.delete()
        for _ in range(count):
            app.send_message(message.chat.id, text)

print("Модуль spam загружен!")
