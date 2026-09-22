import streamlit as st

# App title and introduction
st.set_page_config(page_title="Afro Civic Prototype", page_icon="🌍")
st.title("Welcome to Afro Civic")
st.subheader("Your Pan-African Civic Education and Engagement Platform")

st.write("---")

# A friendly placeholder message
st.markdown("""
### Current Prototype Status: **Initialization**

This is a preliminary test to confirm that our GitHub-to-deployment pipeline is active.

**Immediate Development Roadmap:**
1. [x] Create GitHub repository.
2. [x] Deploy initial "Hello World" app.
3. [ ] Integrate a large language model (LLM) for plain language bill translation.
4. [ ] Build multi-language (e.g., Swahili, English, native languages) toggle.
5. [ ] Design an interactive citizen-to-government feedback interface.
""")

st.write("---")
st.info("Stay tuned. We are building something impactful for civic engagement in Africa.")
