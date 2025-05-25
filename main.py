from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

USER_NAME = "Tamerlan"
START_WEIGHT = 74.0
GOAL_WEIGHT = 62.0
CURRENT_WEIGHT = START_WEIGHT
CHECKINS = {"football": []}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hi, {USER_NAME}!\n"
        f"Your goal: {GOAL_WEIGHT} kg. Start weight: {START_WEIGHT} kg.\n"
        f"I will help you stay on track!"
    )

async def weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURRENT_WEIGHT
    try:
        weight = float(context.args[0])
        CURRENT_WEIGHT = weight
        lost = START_WEIGHT - CURRENT_WEIGHT
        remaining = CURRENT_WEIGHT - GOAL_WEIGHT
        await update.message.reply_text(
            f"✅ Weight saved: {weight} kg\n"
            f"Lost: {lost:.1f} kg\n"
            f"Remaining to goal: {remaining:.1f} kg"
        )
    except:
        await update.message.reply_text("Use like this: /weight 72.8")

async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lost = START_WEIGHT - CURRENT_WEIGHT
    remaining = CURRENT_WEIGHT - GOAL_WEIGHT
    await update.message.reply_text(
        f"Current weight: {CURRENT_WEIGHT} kg\n"
        f"Lost: {lost:.1f} kg\n"
        f"Remaining: {remaining:.1f} kg"
    )

async def plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    day = datetime.datetime.today().weekday()
    if day == 0 or day == 3:
        await update.message.reply_text("Today: Football at 20:30!")
    else:
        await update.message.reply_text("Today: Rest or optional swim.")

async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0].lower() == "football":
        CHECKINS["football"].append(str(datetime.date.today()))
        await update.message.reply_text("Football checked in. Nice job!")
    else:
        await update.message.reply_text("Example: /checkin football")

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Drink more water and keep moving daily!")

def main():
    app = ApplicationBuilder().token("7042426667:AAFaQdiXF_8XnNyYckXLzykQP8oHjgeGwGI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weight", weight))
    app.add_handler(CommandHandler("progress", progress))
    app.add_handler(CommandHandler("plan", plan))
    app.add_handler(CommandHandler("checkin", checkin))
    app.add_handler(CommandHandler("tip", tip))
    app.run_polling()

if __name__ == "__main__":
    main()
