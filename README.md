
# Vespera-AI

Welcome to **Vespera AI**, an AI-powered storytelling web app! With Vespera, users can generate creative stories based on their prompts, choose storytelling modes, and save or view generated content for later use. This README provides details on the app, how to access it, and how to set up and run the backend and frontend.


## Features

- **Story Generation**: Create stories using AI by providing a custom prompt and selecting parameters like storytelling mode, length, and creativity.
- **Story Modes**: Choose from genres like Fantasy, Sci-Fi, Mystery, or General to customize your experience.
- **Save and View Stories**: Save your favorite stories and view them anytime with MongoDB integration.


## App Architecture

1. **Frontend**: Developed with **Streamlit**, providing an interactive user interface for prompt submission, viewing stories, and saving content.
2. **Backend**: Built with **Flask**, handling story generation using `gpt-4free` and managing story storage via MongoDB.

## Prerequisites

Ensure the following are installed on your system:

- **Python 3.8 or later**
- **MongoDB** (Running locally on `localhost:27017`) or MongoDB Atlas URI for cloud storage
- **Pip** (Python package manager)


## Requirements

This project requires several Python packages, which are listed in the `requirements.txt` file.

### Python Packages in `requirements.txt`

- `flask==3.0.3`: A web framework to build the API.
- `g4f==0.3.9.7`: A library for integrating with various AI services.
- `jinja2==3.1.4`: A templating engine for Python (used by Flask).
- `pymongo==4.10.1`: A MongoDB client to interact with a MongoDB database.
- `transformers==4.46.3`: Hugging Face library for Natural Language Processing.
- `werkzeug==3.0.6`: A library used by Flask for utility functions.
- `python-dotenv==1.0.1`: A library to read key-value pairs from `.env` files.


## Installation

1. **Clone the Repository**:
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/username/vespera-ai.git
   cd vespera-ai
   ```

2. **Install the Required Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create and Configure `.env` Files**:

   - **Backend `.env`**: Create a `.env` file in the root of your backend directory (where `main.py` is located) with the following content:
     ```plaintext
     DATABASE_URI=mongodb+srv://<username>:<password>@cluster0.tepk4.mongodb.net/
     ```

     Replace `<username>` and `<password>` with your MongoDB Atlas credentials. If you are using a local MongoDB instance, replace `DATABASE_URI` with your local connection string, e.g.:
     ```plaintext
     DATABASE_URI=mongodb://localhost:27017
     ```

   - **Frontend `.env`**: Create a `.env` file in the frontend directory (where `app.py` is located) with the following content:
     ```plaintext
     BACKEND_URI=http://127.0.0.1:5000
     ```


## Running the Application

### 1. Start the Backend (Flask)

- Navigate to the backend directory and run:
  ```bash
  python main.py
  ```
- The backend server will start at `http://127.0.0.1:5000`.

### 2. Start the Frontend (Streamlit)

- Open a new terminal window, navigate to the frontend directory, and run:
  ```bash
  streamlit run app.py
  ```
- The frontend will be accessible at `http://localhost:8501`.


## Usage

1. **Access the App**:
   - Open your web browser and go to `http://localhost:8501`.

2. **Generate Stories**:
   - Enter a prompt in the "Generate a Story" section.
   - Select a storytelling mode, adjust creativity and length parameters, and click **Generate Story**.

3. **Save Stories**:
   - After generating a story, click **Save Story** to store it in the database.

4. **View Saved Stories**:
   - Click **View Saved Stories** to retrieve all previously saved stories from MongoDB.


## Troubleshooting

1. **MongoDB Connection Issues**:
   - Ensure MongoDB is running and accessible at `localhost:27017` if using a local MongoDB instance.
   - If using MongoDB Atlas, ensure your `DATABASE_URI` is correctly set in the `.env` file.
   - Check if the `storydb` database and `stories` collection are set up correctly.

2. **Backend Errors**:
   - Verify that the Flask backend is running without errors and reachable at `http://127.0.0.1:5000`.

3. **Frontend Issues**:
   - Ensure all dependencies for Streamlit are installed, and check for port conflicts on `8501`.

---

Feel free to reach out with any questions or issues. Happy storytelling! 🌟

## Contact

If you have any questions or issues, feel free to reach out!

- **GitHub**: [https://github.com/shreyakabra](https://github.com/shreyakabra)
- **Email**: [kabrashreya23@gmail.com](mailto:kabrashreya23@gmail.com)
- **LinkedIn**: [https://linkedin.com/in/shreyakabra23](https://linkedin.com/in/shreyakabra23)

--- 