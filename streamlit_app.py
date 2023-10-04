import streamlit as st

# Initialize a session state for the chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("PizzaBot")

# User Input
user_input = st.text_input("You: ")

# When the user presses enter
if user_input:

    # Add the user input to chat history
    st.session_state.chat_history.append({"user": user_input})

    # Bot Logic (You can replace this with more advanced logic or NLP)
    if "menu" in user_input.lower():
        bot_reply = "We have Margherita, Vegan, and Pepperoni pizzas."
    elif "order" in user_input.lower():
        bot_reply = "Great! What type of pizza would you like to order?"
    elif "hello" in user_input.lower():
        bot_reply = "Hello! How can I assist you today?"
    else:
        bot_reply = "I'm sorry, I don't understand."

    # Add the bot's reply to chat history
    st.session_state.chat_history.append({"bot": bot_reply})

# Display Chat History
for chat in st.session_state.chat_history:
    if "user" in chat:
        st.write(f"You: {chat['user']}")
    else:
        st.write(f"PizzaBot: {chat['bot']}")
