import os
import requests
import streamlit as st
import pandas as pd
FLASK_API_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="📂 AI Powered File Organizer", layout="wide")


st.title("📂 AI Powered File Organizer")
st.subheader("Upload Files for Classification")
uploaded_files = st.file_uploader("Drag & drop files or browse", accept_multiple_files=True)

if uploaded_files:
    st.success(f"📁 {len(uploaded_files)} files selected. Uploading...")

    files_to_upload = [("files", (file.name, file, file.type)) for file in uploaded_files]
    
    try:
        response = requests.post(f"{FLASK_API_URL}/upload", files=files_to_upload)
        response.raise_for_status()
        result = response.json()

        st.success("✅ Files uploaded and classified successfully!")

        st.subheader("📋 Classification Results")

        for file in result["files"]:
            st.markdown(
                f"""
                <div style="border:2px solid #4CAF50; padding:10px; margin:5px; border-radius:10px;">
                    <h4>📄 {file["name"]}</h4>
                    <p><b>📁 Category:</b> <span style="color:#FFA500;">{file["category"]}</span></p>
                    <p>📌 <b>Stored at:</b> <code>{file["path"]}</code></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Upload failed: {e}")

st.subheader("📂 Stored Files in Database")

if st.button("🔄 Refresh File List"):
    try:
        response = requests.get(f"{FLASK_API_URL}/files")
        response.raise_for_status()
        stored_files = response.json()

        if stored_files:
            df = pd.DataFrame(stored_files)
            for _, row in df.iterrows():
                st.markdown(
                    f"""
                    <div style="border:2px solid #2196F3; padding:10px; margin:5px; border-radius:10px;">
                        <h4>📄 {row["name"]}</h4>
                        <p><b>📁 Category:</b> <span style="color:#FFA500;">{row["category"]}</span></p>
                        <p>📌 <b>Stored at:</b> <code>{row["path"]}</code></p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.warning("⚠️ No files found.")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Fetching files failed: {e}")
        
st.sidebar.title("ℹ️ Project Information")
st.sidebar.write("**Project:** AI File Organizer(Classifier) 📂")
st.sidebar.write("**Description:** Automatically categorizes files using a trained AI model.")
st.sidebar.write("**Technologies Used:**")
st.sidebar.markdown("- 🐍 Python (Flask, Streamlit)")
st.sidebar.markdown("- 🤖 Machine Learning (Scikit-learn, Pickle)")
st.sidebar.markdown("- 🗄️ SQLite Database")
st.sidebar.markdown("- 🔄 API Communication (Flask & Streamlit)")


