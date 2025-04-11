import streamlit as st
from bug_summarizer import generate_bug_report

st.set_page_config(page_title="Bug Report Formatter", layout="wide")
st.markdown("<h1 style='text-align: center;'>🪲 AI-Powered Bug Report Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Quickly convert messy bug notes into structured JIRA-style reports using LLaMA 3.2 or DeepSeek.</p>", unsafe_allow_html=True)

st.divider()

# --- Sidebar Settings ---
with st.sidebar:
    st.header("⚙️ Model & Settings")
    model = st.selectbox("Choose LLM Model", ["llama3.2", "deepseek-r1"])
    severity = st.radio("Select Bug Severity", ["Critical", "High", "Medium", "Low"])

# --- Bug Input Section ---
st.subheader("📝 Enter Raw Bug Description")
bug_input = st.text_area(
    "",
    placeholder="Example: The login button doesn't respond on Chrome browser...",
    height=180
)

# --- Generate Report Button ---
if st.button("✨ Generate Bug Report", use_container_width=True):
    if not bug_input.strip():
        st.warning("Please enter a bug description first.")
    else:
        with st.spinner("Asking the model..."):
            response = generate_bug_report(bug_input, severity, model)

            if not response or "⚠️" in response:
                st.error("Something went wrong. Try again or check the model setup.")
            else:
                st.success("✅ Bug Report Generated:")
                st.code(response, language="markdown")

                st.text_area("📋 Copyable Report", value=response, height=300)
                st.download_button(
                    "📥 Download Report",
                    data=response,
                    file_name="bug_report.txt",
                    mime="text/plain"
                )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 0.85rem; color: gray;'>Built with ❤️ for QA Engineers · Powered by LLaMA 3.2 & DeepSeek via Ollama</p>",
    unsafe_allow_html=True
)
