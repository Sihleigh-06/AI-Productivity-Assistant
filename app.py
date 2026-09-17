import os
from dotenv import load_dotenv
import streamlit as st

from assistant_core import (
    generate_email,
    summarize_meeting,
    plan_tasks,
    research_assistant,
    chatbot_response,
)

load_dotenv()

st.set_page_config(page_title="AI Productivity Assistant", page_icon="🤖", layout="wide")

st.title("AI Productivity Assistant")
st.caption("A practical workplace copilot for email generation, meeting summaries, task planning, and research support.")

with st.sidebar:
    st.header("AI Settings")
    provider = st.selectbox("AI provider", ["demo", "openai", "gemini"], index=0)
    st.session_state["provider"] = provider

    if provider == "openai":
        api_key = st.text_input("OpenAI API key", type="password", value=os.getenv("OPENAI_API_KEY", ""))
        os.environ["OPENAI_API_KEY"] = api_key
    elif provider == "gemini":
        api_key = st.text_input("Gemini API key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
        os.environ["GEMINI_API_KEY"] = api_key

    st.markdown("---")
    st.markdown(
        """
        Ethical use checklist:
        - Verify before sending
        - Protect confidential information
        - Review for bias and tone
        - Keep a human in the loop
        """
    )


email_tab, meeting_tab, task_tab, research_tab, chatbot_tab = st.tabs([
    "Email Generator",
    "Meeting Summaries",
    "Task Planning",
    "Research Assistant",
    "Chatbot",
])

with email_tab:
    st.subheader("Generate a professional email")
    recipient = st.text_input("Recipient")
    purpose = st.text_input("Purpose")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Persuasive", "Concise"])
    details = st.text_area("Key details to include")

    if st.button("Generate Email"):
        if recipient and purpose:
            result = generate_email(recipient, purpose, tone, details)
            st.markdown(result)
        else:
            st.warning("Please provide the recipient and purpose.")

with meeting_tab:
    st.subheader("Summarize a meeting")
    notes = st.text_area("Paste meeting notes or transcript")
    if st.button("Summarize Meeting"):
        if notes:
            result = summarize_meeting(notes)
            st.markdown(result)
        else:
            st.warning("Add notes or transcript text.")

with task_tab:
    st.subheader("Plan tasks")
    goal = st.text_input("Project or goal")
    constraints = st.text_area("Constraints or time limits")
    if st.button("Build Plan"):
        if goal:
            result = plan_tasks(goal, constraints)
            st.markdown(result)
        else:
            st.warning("Enter a project goal first.")

with research_tab:
    st.subheader("Research helper")
    topic = st.text_input("Topic to research")
    if st.button("Research Topic"):
        if topic:
            result = research_assistant(topic)
            st.markdown(result)
        else:
            st.warning("Add a topic to research.")

with chatbot_tab:
    st.subheader("Workplace chatbot")
    user_input = st.text_area("Ask a question or share a task")
    if st.button("Ask Assistant"):
        if user_input:
            result = chatbot_response(user_input)
            st.markdown(result)
        else:
            st.warning("Type a question or task description.")

st.markdown("---")
st.markdown("Built for practical AI-assisted workplace productivity and responsible human review.")
