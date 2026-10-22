import streamlit as st
import ollama

st.title("🌍 ChatGeo: Geographic AI Assistant")
st.markdown("Specialized assistant that *only* answers geographical questions.")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input via Streamlit's chat input component
if prompt := st.chat_input("Ask a geographical question..."):
    # Add user message to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from local Llama 3 instance using Ollama
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Define the System Prompt enforcing the geographic constraint
            system_prompt = (
                "You are ChatGeo, a specialized geographical assistant. "
                "You are strictly forbidden from answering questions outside of geography, cartography, "
                "earth sciences, countries, capitals, and physical or political geography. "
                "If the user asks about math, coding, personal advice, or any non-geographical topic, "
                "you must politely refuse by saying: 'I am ChatGeo and can only answer geographical questions.'"
            )

            # Build messages array including the system prompt as context
            messages_payload = [{"role": "system", "content": system_prompt}] + [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]

            # Call local Ollama client (streaming response)
            stream = ollama.chat(
                model='llama3',
                messages=messages_payload,
                stream=True,
            )

            for chunk in stream:
                full_response += chunk['message']['content']
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Error connecting to local Ollama instance: {e}"
            message_placeholder.error(full_response)

    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": full_response})