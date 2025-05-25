from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

# Персональные данные
USER_NAME = "Тамерлан"
START_WEIGHT = 74.0
GOAL_WEIGHT = 62.0
CURRENT_WEIGHT = START_WEIGHT
CHECKINS = {"футбол": []}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Привет, {USER_NAME}!\n"
        f"Твоя цель: {GOAL_WEIGHT} кг. Стартовый вес: {START_WEIGHT} кг.\n"
        f"Я помогу тебе похудеть и вести учёт!"
    )

async def вес(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURRENT_WEIGHT
    try:
        weight = float(context.args[0])
        CURRENT_WEIGHT = weight
        lost = START_WEIGHT - CURRENT_WEIGHT
        remaining = CURRENT_WEIGHT - GOAL_WEIGHT
        await update.message.reply_text(
            f"✅ Вес сохранён: {weight} кг\n"
            f"Сброшено: {lost:.1f} кг\n"
            f"До цели: {remaining:.1f} кг"
        )
    except:
        await update.message.reply_text("Используй: /вес 72.8")

async def прогресс(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lost = START_WEIGHT - CURRENT_WEIGHT
    remaining = CURRENT_WEIGHT - GOAL_WEIGHT
    await update.message.reply_text(
        f"Текущий вес: {CURRENT_WEIGHT} кг\n"
        f"Сброшено: {lost:.1f} кг\n"
        f"До цели: {remaining:.1f} кг"
    )

async def план(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = datetime.datetime.today().weekday()
    if day == 0 or day == 3:
        await update.message.reply_text("Сегодня футбол в 20:30!")
    else:
        await update.message.reply_text("Сегодня отдыхаешь или можешь поплавать.")

async def отметить(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0].lower() == "футбол":
        CHECKINS["футбол"].append(str(datetime.date.today()))
        await update.message.reply_text("Футбол отмечен. Молодец!")
    else:
        await update.message.reply_text("Пример: /отметить футбол")

async def совет(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пей больше воды и не забывай про движение даже в дни без тренировки.")

def main():
    app = ApplicationBuilder().token("7042426667:AAFaQdiXF_8XnNyYckXLzykQP8oHjgeGwGI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("вес", вес))
    app.add_handler(CommandHandler("прогресс", прогресс))
    app.add_handler(CommandHandler("план", план))
    app.add_handler(CommandHandler("отметить", отметить))
    app.add_handler(CommandHandler("совет", совет))
    app.run_polling()

if __name__ == "__main__":
    main()
