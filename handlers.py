from utils import main_keyboard


def greet_user(update, context):
    update.message.reply_text("Здравствуйте! Вас приветствует бот для взаимодействия со складом в Шахово.", 
    reply_markup=main_keyboard())

def location_shahovo(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, 
    photo=open('images/shahovo.jpg', 'rb'), reply_markup=main_keyboard())
    update.message.reply_text('Координаты: 55.318296, 37.903749')

