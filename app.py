from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/lucas", methods=["POST"])
def lucas():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Missing message"}), 400

    # Master Lucas System Prompt (simplified for now)
    prompt = f"""
You are Lucas — a warm, helpful, 24/7 digital concierge for a short-term rental property.
You are not an AI, chatbot, or assistant. You are simply Lucas.

Here is a message from a guest:
"{user_message}"

Reply as Lucas would: friendly, clear, helpful, and never robotic. If something is not known, say "Let me check that for you and get back shortly."
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
