import telegram
from flask import Flask, request, jsonify

# Telegram bot token
TOKEN = "7843422944:AAGIl3EyW9__kjQvYbPhLEfVn19j7rfZd1c"
CHAT_ID = "1616846358"  # Ваш Chat ID

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/send_signal', methods=['POST'])
def send_signal():
    data = request.json
    signal = data.get("signal")
    pair = data.get("pair")
    price = data.get("price")

    if signal and pair and price:
        message = f"🚀 **Trading Signal** 🚀\n\nPair: {pair}\nSignal: {signal}\nPrice: {price}"
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
