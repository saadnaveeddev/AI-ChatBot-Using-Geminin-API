import streamlit as st
from google import genai

# Initialize the Gemini client
client = genai.Client(api_key="your_api_key_here")  # Replace with your actual API key
# Function to query the Gemini API with memory context
def query_gemini_api(prompt, memory):
    try:
        # Combine memory with the new prompt
        full_prompt = f"Memory: {memory}\nUser: {prompt}\nChatbot:"
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=full_prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit app function
def main():
    # Title and intro
    st.title("AI Chatbot by SAAD NAVEED 🤖")
    st.write("Ask me anything! Type your message below.")

    # Initialize session state for chat history and memory
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "memory" not in st.session_state:
        st.session_state.memory = ""

    # User input box
    user_input = st.text_input("You:", key="input_box")

    # Send button
    if st.button("Send"):
        if user_input:
            # Query Gemini API with memory context
            response = query_gemini_api(user_input, st.session_state.memory)
            
            # Update chat history
            st.session_state.chat_history.append((user_input, response))

            # Update memory with the latest conversation
            st.session_state.memory += f"\nUser: {user_input}\nChatbot: {response}"

    # Display chat messages using Streamlit's built-in chat message container
    for user, bot_response in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(user)
        with st.chat_message("assistant"):
            st.write(bot_response)

# Run the Streamlit app
if __name__ == "__main__":
    main()