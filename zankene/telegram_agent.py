import sys
import os

# Add root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest
from zankene.llm import ZankeneLLMEngine

BOT_TOKEN = "8896817169:AAGHu0Q07N24gH9naLlmRpyngck4zQn_wco"

engine = ZankeneLLMEngine()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 ZANKENE Multi-Agent System Online!\n\nSend me any command, code prompt, or web search task.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    status_msg = await update.message.reply_text("⚙️ ZANKENE Engine Processing Task...")
    
    try:
        sys_prompt = "You are ZANKENE Autonomous AI System Controller. Provide clear analysis, actionable steps, or raw python code based on request."
        response = engine.generate_agent_response(system_prompt=sys_prompt, user_prompt=user_text)
        
        await status_msg.edit_text(f"🤖 ZANKENE Response:\n\n{response}")
    except Exception as e:
        await status_msg.edit_text(f"❌ Execution Error: {e}")

if __name__ == '__main__':
    print("🚀 Starting ZANKENE Telegram Controller Bot...")
    
    # Custom request config with increased timeout to prevent network drop
    request_config = HTTPXRequest(connect_timeout=20.0, read_timeout=20.0)
    
    app = ApplicationBuilder().token(BOT_TOKEN).request(request_config).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()