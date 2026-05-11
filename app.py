import streamlit as st
import ollama

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="TinyLlama Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- TITLE ---------------- #
st.title("🤖 ChatGPT-based Python Application")
st.markdown("Built using Python + Streamlit + Ollama")

# ---------------- SESSION STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- USER INPUT ---------------- #
user_input = st.text_input("Ask your question")

# ---------------- GENERATE BUTTON ---------------- #
if st.button("Generate Response"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a valid question")

    else:

        try:

            # Save user message
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            # Generate AI response
            response = ollama.chat(
                model="tinyllama",
                messages=st.session_state.messages
            )

            ai_reply = response["message"]["content"]

            # Save AI response
            st.session_state.messages.append({
                "role": "assistant",
                "content": ai_reply
            })

            # Display AI response
            st.success(ai_reply)

        except Exception as e:

            st.error(f"❌ Error: {e}")

            st.info("""
✅ Make sure:
1. Ollama is installed
2. Run: ollama pull tinyllama
3. Ollama server is running
            """)

# ---------------- CHAT HISTORY ---------------- #
st.subheader("📜 Conversation History")

for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")

    else:
        st.markdown(f"🤖 **AI:** {msg['content']}")








