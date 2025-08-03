import streamlit as st
import requests

st.set_page_config(page_title="📄 TalkToPDF Chat", page_icon="🤖")
st.title("📄 TalkToPDF – Chat with your documents")

# Handle upload
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and "pdf_uploaded" not in st.session_state:
    with st.spinner("Uploading and processing PDF..."):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}

        try:
            res = requests.post("http://localhost:8000/upload/", files=files)
            res.raise_for_status()
            st.session_state.pdf_uploaded = True
            st.success("✅ PDF uploaded and ingested!")
        except Exception as e:
            st.error(f"❌ Upload failed: {e}")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat UI
query = st.chat_input("Ask a question from your PDF...")

if query:
    # Display user message
    st.chat_message("user").markdown(query)
    st.session_state.chat_history.append({"role": "user", "content": query})

    # Query backend
    try:
        res = requests.post("http://localhost:8000/ask/", json={"query": query})
        res.raise_for_status()
        answer = res.json().get("response", "No answer returned.")
    except Exception as e:
        answer = f"❌ Error: {e}"

    # Display assistant response
    st.chat_message("assistant").markdown(answer)
    st.session_state.chat_history.append({"role": "assistant", "content": answer})

# Show chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])
