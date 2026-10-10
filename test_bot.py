from zankene.telegram_bot import run_bot

# Replace with your actual BotFather token
TELEGRAM_BOT_TOKEN = "8896817169:AAGHu0Q07N24gH9naLlmRpyngck4zQn_wco"

if __name__ == "__main__":
    if TELEGRAM_BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("⚠️ Please insert your Telegram Bot Token from @BotFather in test_bot.py!")
    else:
        run_bot(TELEGRAM_BOT_TOKEN)