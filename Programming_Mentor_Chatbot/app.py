import streamlit as st

from chatbot import ask_chatbot


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="💻",
    layout="centered",
)


# ============================================================
# HEADER
# ============================================================

st.title("💻 CodeMentor AI")

st.caption(
    "Your AI Programming Mentor for Python, ML, Web Development "
    "and Computer Science."
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🧠 CodeMentor AI")

    st.write(
        """
        **Available Mentors**

        🐍 Python Programming

        🤖 Machine Learning & AI

        🌐 Web Development

        💻 General Computer Science
        """
    )

    st.divider()

    st.write("### ⚙️ LangChain Features")

    st.write(
        """
        ✅ PromptTemplate

        ✅ RunnableBranch

        ✅ RunnableParallel

        ✅ Pydantic Structured Output

        ✅ Streamlit Chat Interface
        """
    )

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message["role"] == "user":

            st.write(message["content"])

        else:

            response = message["content"]

            # Category
            st.markdown(
                f"### 📌 {response.category}"
            )

            # Language
            st.markdown(
                f"**Language / Technology:** "
                f"{response.language}"
            )

            # Difficulty
            st.markdown(
                f"**🎯 Difficulty:** "
                f"{response.difficulty}"
            )

            # Confidence
            st.markdown(
                f"**📊 Confidence:** "
                f"{response.confidence:.0%}"
            )

            # Answer
            st.markdown("### 💡 Answer")

            st.write(response.answer)

            # Explanation
            st.markdown("### 📖 Explanation")

            st.write(response.explanation)

            # Complexity
            st.markdown("### ⚡ Complexity")

            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"**Time:**\n\n"
                    f"{response.time_complexity}"
                )

            with col2:

                st.info(
                    f"**Space:**\n\n"
                    f"{response.space_complexity}"
                )

            # Concepts
            st.markdown("### 🧠 Concepts")

            for concept in response.concepts:

                st.markdown(
                    f"- {concept}"
                )

            # Follow-up
            st.markdown("### ❓ Try This Next")

            st.write(
                response.follow_up_question
            )


# ============================================================
# USER INPUT
# ============================================================

user_question = st.chat_input(
    "Ask me a programming question..."
)


if user_question:

    # --------------------------------------------------------
    # Display user message
    # --------------------------------------------------------

    with st.chat_message("user"):

        st.write(user_question)


    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question,
        }
    )


    # --------------------------------------------------------
    # Generate AI response
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "CodeMentor is thinking..."
        ):

            try:

                response = ask_chatbot(
                    user_question
                )

                # Category
                st.markdown(
                    f"### 📌 {response.category}"
                )

                # Language
                st.markdown(
                    f"**Language / Technology:** "
                    f"{response.language}"
                )

                # Difficulty
                st.markdown(
                    f"**🎯 Difficulty:** "
                    f"{response.difficulty}"
                )

                # Confidence
                st.markdown(
                    f"**📊 Confidence:** "
                    f"{response.confidence:.0%}"
                )

                # Answer
                st.markdown("### 💡 Answer")

                st.write(response.answer)

                # Explanation
                st.markdown("### 📖 Explanation")

                st.write(response.explanation)

                # Complexity
                st.markdown("### ⚡ Complexity")

                col1, col2 = st.columns(2)

                with col1:

                    st.info(
                        f"**Time:**\n\n"
                        f"{response.time_complexity}"
                    )

                with col2:

                    st.info(
                        f"**Space:**\n\n"
                        f"{response.space_complexity}"
                    )

                # Concepts
                st.markdown("### 🧠 Concepts")

                for concept in response.concepts:

                    st.markdown(
                        f"- {concept}"
                    )

                # Follow-up
                st.markdown(
                    "### ❓ Try This Next"
                )

                st.write(
                    response.follow_up_question
                )

                # Save response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                    }
                )

            except Exception as e:

                st.error(
                    "Something went wrong while generating "
                    "the response."
                )

                st.exception(e)