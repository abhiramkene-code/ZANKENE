import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest
from zankene.llm import ZankeneLLMEngine
from zankene.search_agent import ZankeneWebSearchAgent

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

llm = ZankeneLLMEngine(model_name="llama3")
search_agent = ZankeneWebSearchAgent(model_name="llama3")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 Welcome to ZANKENE V10 Mobile Mission Control!\n\nCommands:\n/search <query> - Live Web Search\n/status - System Health\nOr send any prompt directly to talk to Llama3.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 ZANKENE V10 Engine Status: ONLINE\n🧠 Active Mesh Model: Llama3\n⚡ FastAPI & Streamlit Connected")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Usage: /search <topic>")
        return
    await update.message.reply_text(f"🌐 Gathering live web intelligence for: '{query}'...")
    res = search_agent.run_live_search_task(query)
    await update.message.reply_text(f"📋 Insights:\n\n{res}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text("🤖 Thinking...")
    response = llm.generate_agent_response("You are ZANKENE Mobile Assistant.", user_text)
    await update.message.reply_text(response)

def run_bot(token: str):
    # Enhanced HTTP connection pooling and timeouts
    req = HTTPXRequest(
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0
    )
    
    app = ApplicationBuilder().token(token).request(req).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("search", search))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Telegram Bot Listening for Mobile Directives...")
    # Retries network bootstrap gracefully
    app.run_polling(poll_interval=2.0, bootstrap_retries=5)