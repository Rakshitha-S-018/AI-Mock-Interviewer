import streamlit as st

from modules.resume_analyzer import (
    analyze_resume,
    extract_resume_text
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Resume Analysis",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

with open("styles/style.css") as css:

    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )


# ==========================================
# CHECK REGISTRATION
# ==========================================

if "name" not in st.session_state:

    st.warning(
        "⚠️ Please register from the Home Page first."
    )

    st.stop()


# ==========================================
# HEADER
# ==========================================

st.title(
    "📄 AI Resume Analysis"
)


st.markdown(
    f"### Analyze your resume, {st.session_state.name}! 👋"
)


st.write(
    "Upload your resume and let AI analyze your skills, "
    "experience, strengths, and areas for improvement."
)


st.markdown("---")


# ==========================================
# RESUME UPLOAD
# ==========================================

st.subheader(
    "📤 Upload Your Resume"
)


uploaded_resume = st.file_uploader(

    "Upload Resume PDF",

    type=["pdf"],

    key="resume_upload"

)


# ==========================================
# ANALYZE RESUME
# ==========================================

if uploaded_resume is not None:


    st.success(
        "✅ Resume uploaded successfully!"
    )


    if st.button(

        "🤖 Analyze Resume",

        use_container_width=True

    ):


        with st.spinner(

            "🔍 AI is analyzing your resume..."

        ):


            try:


                # ==========================================
                # EXTRACT TEXT FOR SAVING / DISPLAY
                # ==========================================

                resume_text = extract_resume_text(

                    uploaded_resume

                )


                if not resume_text.strip():

                    st.error(

                        "❌ Could not extract text from this PDF."

                    )

                    st.stop()


                # ==========================================
                # RESET FILE POINTER
                # ==========================================

                uploaded_resume.seek(0)


                # ==========================================
                # ANALYZE USING AI
                # ==========================================

                analysis = analyze_resume(

                    uploaded_resume,

                    st.session_state.role

                )


                # ==========================================
                # SAVE RESULTS
                # ==========================================

                st.session_state.resume_text = resume_text

                st.session_state.resume_analysis = analysis


                st.success(

                    "🎉 Resume analysis completed!"

                )


            except Exception as e:


                st.error(

                    f"❌ Error analyzing resume: {e}"

                )


# ==========================================
# DISPLAY ANALYSIS
# ==========================================

if "resume_analysis" in st.session_state:


    st.markdown("---")


    st.subheader(

        "🧠 AI Resume Analysis"

    )


    st.markdown(

        st.session_state.resume_analysis

    )


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title(

    "📄 Resume Analysis"

)


st.sidebar.write(

    f"👤 **Candidate:** "

    f"{st.session_state.name}"

)


st.sidebar.write(

    f"💼 **Target Role:** "

    f"{st.session_state.role}"

)


st.sidebar.markdown("---")


st.sidebar.success(

    "🤖 AI Analysis Ready"

)