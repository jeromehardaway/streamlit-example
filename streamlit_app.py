import streamlit as st

# Initialize session states for chat history and user name
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_name' not in st.session_state:
    st.session_state.user_name = None

# Header
st.markdown("# Welcome to PizzaBot!")
st.markdown("Your friendly neighborhood pizza ordering service.")

# Title
st.title("Chat with PizzaBot")

# Ask for User Name if not already set
if st.session_state.user_name is None:
    name_input = st.text_input("Please enter your name:")
    if st.button("Submit Name"):
        st.session_state.user_name = name_input
        st.write(f"Welcome {st.session_state.user_name}, how can I help you today?")
        st.write("Type 'menu' to see the menu, 'order' to place an order, or 'hello' to greet the bot.")
else:
    # User Input for the chat
    user_input = st.text_input(f"{st.session_state.user_name}: ")

    # When the user presses the send button
    if st.button("Send") and user_input:

        # Add the user input to chat history
        st.session_state.chat_history.append({st.session_state.user_name: user_input})

        # Bot Logic with Enhanced Prompts
        if "menu" in user_input.lower():
            bot_reply = "Sure, we offer a variety of pizzas like Margherita, Vegan, and Pepperoni. Would you like to know more about each?"
        elif "yes" in user_input.lower():
            bot_reply = """Great! Here are the details:
            - Margherita: Classic Italian pizza with tomatoes, mozzarella, fresh basil, salt, and extra-virgin olive oil.
            - Vegan: A cruelty-free option with vegan cheese and a variety of vegetable toppings.
            - Pepperoni: A popular choice loaded with pepperoni slices.

            Which one would you like? And what size do you prefer: Small, Medium, or Large?"""
        elif "order" in user_input.lower():
            bot_reply = "Fantastic! What type of pizza would you like to order? You can choose from Margherita, Vegan, and Pepperoni."
        elif "hello" in user_input.lower():
            bot_reply = f"Hello, {st.session_state.user_name}! How may I assist you today?"
        else:
            bot_reply = "I'm sorry, I didn't catch that. Could you please rephrase? Type 'menu' to see the menu, 'order' to place an order, or 'hello' to greet the bot."

        # Add the bot's reply to chat history
        st.session_state.chat_history.append({"PizzaBot": bot_reply})

    # Display Chat History
    for chat in st.session_state.chat_history:
        if st.session_state.user_name in chat:
            st.write(f"{st.session_state.user_name}: {chat[st.session_state.user_name]}")
        else:
            st.write(f"PizzaBot: {chat['PizzaBot']}")

# Footer
st.markdown("---")
st.markdown("Thanks for using PizzaBot! If you have any questions, please [contact us](mailto:support@pizzabot.com).")
