
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random
import os

BOXES = {
    "box3000": {
        "chance": 0.1,
        "big_win": [
            {"photo": "images/watch1.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch2.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
        ],
        "standard": [
            {"photo": "images/watch3.jpg", "caption": "✅ You got a standard Rolex under $10k."},
            {"photo": "images/watch4.jpg", "caption": "✅ You got a standard Rolex under $10k."},
            {"photo": "images/watch5.jpg", "caption": "✅ You got a standard Rolex under $10k."},
            {"photo": "images/watch6.jpg", "caption": "✅ You got a standard Rolex under $10k."},
        ]
    },
    "box6000": {
        "chance": 0.3,
        "big_win": [
            {"photo": "images/watch7.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch8.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
        ],
        "standard": [
            {"photo": "images/watch9.jpg", "caption": "✅ You got a standard Rolex under $10k."},
            {"photo": "images/watch10.jpg", "caption": "✅ You got a standard Rolex under $10k."},
            {"photo": "images/watch11.jpg", "caption": "✅ You got a standard Rolex under $10k."},
            {"photo": "images/watch12.jpg", "caption": "✅ You got a standard Rolex under $10k."},
        ]
    },
    "box7500": {
        "chance": 0.4,
        "big_win": [
            {"photo": "images/watch13.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch14.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch15.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch16.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch17.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch18.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch19.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
            {"photo": "images/watch20.jpg", "caption": "🎉 Congratulations 👏\\nDM for more information."},
        ],
        "standard": [
        ]
    },
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 $3,000 Box", callback_data="box3000")],
        [InlineKeyboardButton("💼 $6,000 Box", callback_data="box6000")],
        [InlineKeyboardButton("🧳 $7,500 Box", callback_data="box7500")],
    ]
    await update.message.reply_text("Choose your mystery box:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_box(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    box_id = query.data
    box = BOXES[box_id]
    is_big_win = random.random() < box["chance"]
    result = random.choice(box["big_win"] if is_big_win else box["standard"])

    with open(result["photo"], "rb") as img_file:
        await query.message.reply_photo(photo=img_file, caption=result["caption"])

def main():
    TOKEN = os.environ.get("7561016807:AAFSd9qksZTevryHjvqB_ntVWk1745YDSXU")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_box))
    app.run_polling()

if __name__ == "__main__":
    main()
