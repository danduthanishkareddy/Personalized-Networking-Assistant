import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Personalized Networking Assistant", layout="centered")

st.title("Personalized Networking Assistant")
st.write("Generate smart conversation starters for networking events.")

if "generated_data" not in st.session_state:
    st.session_state.generated_data = None

event_description = st.text_area("Enter Event Description")
interests_text = st.text_input("Enter your interests separated by commas")

if st.button("Generate Conversation Starters"):
    interests = [i.strip() for i in interests_text.split(",") if i.strip()]

    payload = {
        "event_description": event_description,
        "interests": interests
    }

    response = requests.post(f"{API_URL}/generate-conversation", json=payload)

    if response.status_code == 200:
        st.session_state.generated_data = response.json()
    else:
        st.error("Something went wrong.")

if st.session_state.generated_data:
    data = st.session_state.generated_data

    st.subheader("Extracted Themes")
    st.write(data["extracted_themes"])

    st.subheader("Conversation Starters")

    for starter in data["conversation_starters"]:
        st.write(f"• {starter}")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍 Helpful", key=f"helpful_{starter}"):
                requests.post(
                    f"{API_URL}/feedback",
                    json={
                        "conversation_starter": starter,
                        "feedback": "Helpful"
                    }
                )
                st.success("Feedback saved!")

        with col2:
            if st.button("👎 Not Helpful", key=f"not_helpful_{starter}"):
                requests.post(
                    f"{API_URL}/feedback",
                    json={
                        "conversation_starter": starter,
                        "feedback": "Not Helpful"
                    }
                )
                st.success("Feedback saved!")

st.divider()

st.subheader("Quick Fact Check")

topic = st.text_input("Enter a topic to fact-check")

if st.button("Fact Check"):
    response = requests.post(
        f"{API_URL}/fact-check",
        json={"topic": topic}
    )

    if response.status_code == 200:
        data = response.json()
        st.subheader("Summary")
        st.write(data["summary"])
    else:
        st.error("Fact check failed.")

st.divider()

st.subheader("Conversation History")

if st.button("Load History"):
    response = requests.get(f"{API_URL}/history")

    if response.status_code == 200:
        history = response.json()["history"]

        if history:
            for item in reversed(history):
                st.markdown(f"**Event:** {item['event_description']}")
                st.write("Themes:", item["themes"])
                st.write("Interests:", ", ".join(item["interests"]))

                st.write("Conversation Starters:")
                for starter in item["conversation_starters"]:
                    st.write(f"- {starter}")

                st.divider()
        else:
            st.info("No conversation history found.")
    else:
        st.error("Unable to load history.")

st.divider()

st.subheader("Feedback History")

if st.button("Load Feedback History"):
    response = requests.get(f"{API_URL}/feedback-history")

    if response.status_code == 200:
        feedback_history = response.json()["feedback_history"]

        if feedback_history:
            for item in reversed(feedback_history):
                st.write("Conversation Starter:", item["conversation_starter"])
                st.write("Feedback:", item["feedback"])
                st.divider()
        else:
            st.info("No feedback history found.")
    else:
        st.error("Unable to load feedback history.")