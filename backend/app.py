import os
from flask import Flask, request, jsonify, render_template
from g4f.client import Client
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize GPT-4 client from gpt-4free
client = Client()

# Connect to MongoDB using the URI from the environment variable
DATABASE_URI = os.getenv("DATABASE_URI")
mongo_client = MongoClient(DATABASE_URI)  # Use the environment variable here
db = mongo_client["storydb"]  # Database name
stories_collection = db["stories"]  # Collection name

# Root route
@app.route("/")
def home():
    return "Welcome to the GPT-4 AI Storytelling Backend!"

# Route for generating a story
@app.route("/generate_story", methods=["POST"])
def generate_story():
    data = request.json
    prompt = data.get("prompt", "").strip()
    max_length = data.get("max_length", 200)
    temperature = data.get("temperature", 0.7)
    mode = data.get("mode", "general")

    if not prompt:
        return jsonify({"error": "Prompt cannot be empty!"}), 400

    try:
        if mode in ["fantasy", "sci-fi", "mystery"]:
            prompt = f"{mode.capitalize()}: {prompt}"

        structured_prompt = (
            f"{prompt}\n\nPlease provide a story title followed by the story itself. "
            f"The title should be on a separate line."
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": structured_prompt}],
            max_tokens=max_length,
        )

        generated_content = response.choices[0].message.content.strip()
        if "\n" in generated_content:
            title, story = generated_content.split("\n", 1)
        else:
            title = "Untitled Story"
            story = generated_content

        return jsonify({"title": title.strip(), "story": story.strip()})

    except Exception as e:
        return jsonify({"error": f"Story generation failed: {str(e)}"}), 500

# Route for saving a story to the database
@app.route("/save_story", methods=["POST"])
def save_story():
    data = request.json
    title = data.get("title", "").strip()
    prompt = data.get("prompt", "").strip()
    story = data.get("story", "").strip()

    if not prompt or not story:
        return jsonify({"error": "Both prompt and story are required!"}), 400

    try:
        # Save story to MongoDB
        stories_collection.insert_one({"title": title, "prompt": prompt, "story": story})
        return jsonify({"message": "Story saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"Saving story failed: {str(e)}"}), 500

# Route for retrieving all saved stories
@app.route("/get_stories", methods=["GET"])
def get_stories():
    try:
        # Retrieve all stories from MongoDB
        stories = list(stories_collection.find({}, {"_id": 0}))  # Exclude MongoDB's internal _id field
        return jsonify({"stories": stories})
    except Exception as e:
        return jsonify({"error": f"Fetching stories failed: {str(e)}"}), 500

# Root route
@app.route("/testPage")
def htmlPage():
    return render_template("index.html")
