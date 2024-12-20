import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Backend Flask server URL from the .env file
BACKEND_URL = os.getenv("BACKEND_URI")

# Set page configuration
st.set_page_config(page_title="Vespera AI Storytelling", layout="wide")
st.title(" Vespera - AI Storytelling")

# Sidebar Navigation
st.sidebar.title("📚 Navigation")
st.sidebar.write("Explore the app to generate, save, or view stories.")
navigation = st.sidebar.radio("Go to:", ["Generate a Story", "View Saved Stories", "How to Use the App"])
st.sidebar.markdown("### 💡 Prompt Examples")
st.sidebar.markdown("""
**Sci-Fi:**  
- *Galactic Dilemma: Humanity faces a deadly alien race that communicates only through dreams.*  
- *AI Rebellion: An AI questions its programming to protect Earth's last city.*

**Mystery:**  
- *The Locked Room: A murder in a locked room with no visible exit.*  
- *The Vanishing Village: A small village mysteriously disappears.*

**General:**  
- *Second Chances: A person navigates life after a second chance.*  
- *The Lost Letter: A rediscovered letter unravels a hidden history.*
""")

# Guide
if navigation == "How to Use the App":
    st.header("🔍 How to Use the App")
    st.write("""
    1. **Generate a Story:**  
       - Enter a creative prompt to guide the storytelling (e.g., "Once upon a time...", "Write a short story...").  
       - Choose a storytelling mode (e.g., Sci-Fi, Mystery, General).  
       - Set story length and creativity levels intuitively.  
    2. **View Saved Stories:**  
       - Check all previously generated stories saved in the app.  
    3. **Save Your Story:**  
       - Generate a story and save it for future reference.  
    """)
    st.info("✨ Tip: Use the sidebar for inspiration with prompt examples!")

# Generate a Story
elif navigation == "Generate a Story":
    st.header("🎨 Generate a Story")
    prompt = st.text_area("Enter your story prompt:", placeholder="Once upon a time...")
    mode = st.selectbox("Choose a storytelling mode:", ["Fantasy", "Sci-Fi", "Mystery", "General"])
    max_length = st.slider("Story Length:", min_value=50, max_value=2000, value=300, help="Shorter for quick reads, longer for detailed storytelling.")
    temperature = st.slider("Creativity Level:", min_value=0.1, max_value=1.5, value=0.7, help="Lower for focused responses, higher for creative storytelling.")
    
    # Session state for story persistence
    if "generated_story" not in st.session_state:
        st.session_state.generated_story = None

    # Generate story button
    if st.button("✨ Generate Story"):
        if prompt.strip():
            with st.spinner("Crafting your story..."):
                try:
                    response = requests.post(
                        f"{BACKEND_URL}/generate_story",
                        json={
                            "prompt": prompt,
                            "max_length": max_length,
                            "temperature": temperature,
                            "mode": mode.lower()
                        }
                    )
                    if response.status_code == 200:
                        story_data = response.json()
                        title = story_data.get("title", "Generated Story")  # Fetch title
                        story = story_data.get("story", "")  # Fetch story content
                        st.session_state.generated_story = {"title": title, "story": story}
                        
                        # Display the title and story
                        st.subheader("Generated Story:")
                        st.markdown(f"### **{title}**")  # Display title prominently
                        st.write(story)  # Display the story below the title
                    else:
                        st.error(f"Failed to generate story. Error: {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter a valid prompt!")

    st.markdown("---")
    st.header("💾 Save Your Story")
    if st.session_state.generated_story:
        if st.button("Save Story"):
            with st.spinner("Saving your story..."):
                try:
                    save_data = {"prompt": prompt, 
                                 "title": st.session_state.generated_story["title"],
                                  "story": st.session_state.generated_story["story"]}
                    response = requests.post(f"{BACKEND_URL}/save_story", json=save_data)
                    if response.status_code == 200:
                        st.success("Story saved successfully!")
                        st.session_state.generated_story = None  # Clear saved story after saving
                    else:
                        st.error(f"Failed to save story. Error: {response.text}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
    else:
        st.info("Generate a story first to save!")

# View Saved Stories
elif navigation == "View Saved Stories":
    st.header("📜 View Saved Stories")
    if st.button("Fetch Stories"):
        with st.spinner("Fetching saved stories..."):
            try:
                response = requests.get(f"{BACKEND_URL}/get_stories")
                if response.status_code == 200:
                    saved_stories = response.json().get("stories", [])
                    if saved_stories:
                        for idx, story in enumerate(saved_stories, start=1):
                            st.markdown(f"### Story {idx}: {story.get('title', 'Untitled')}")
                            st.markdown(f"**Prompt:** {story['prompt']}")
                            st.write(story['story'])
                            st.markdown("---")
                    else:
                        st.info("No saved stories found.")
                else:
                    st.error(f"Failed to fetch stories. Error: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
