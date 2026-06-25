import streamlit as st
from datetime import date

st.set_page_config(
    page_title="College Student Registration",
    page_icon="🎓",
    layout="centered"
)

st.markdown("<h1 style='text-align:center;'>🎓 SWAMI PREMANAD MAHAVIDYALAYA  </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Student Registration Form</h4>", unsafe_allow_html=True)

st.image("C:\\Users\\sharm\\Music\\OIP.jpg",caption="College Logo", width=150)

st.markdown("---")

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("student_registration_form"):

    st.subheader("INFORMATION OF CANDIDATE")

    student_name = st.text_input("candidate first Name *")
    student_surname = st.text_input("candidate surname*")
    roll_number = st.text_input("Roll Number *")
    registration_number = st.text_input("Registration Number *")

    father_name = st.text_input("Father's Name *")
    mother_name = st.text_input("Mother's Name *")

    dob = st.date_input(
        "Date of Birth *",
        min_value=date(1990, 1, 1),
        max_value=date.today()
    )

    gender = st.radio(
        "Gender *",
        ["Male", "Female", "Other"],
        horizontal=True
    )

    email = st.text_input("Email *")
    mobile = st.text_input("Mobile Number *")

    course = st.selectbox(
        "Course *",
        [
            "Select Course",
            "BCA",
            "B.Sc",
            "B.Com",
            "BBA",
            "BA",
            "MCA",
            "M.Sc"
        ]
    )

    semester = st.selectbox(
        "Semester *",
        [
            "Select Semester",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"
        ]
    )

    address = st.text_area("Address *")

    col1, col2 = st.columns(2)

    with col1:
        submit_btn = st.form_submit_button("Submit")

    with col2:
        clear_btn = st.form_submit_button("Clear Form")


if clear_btn:
    st.rerun()

if submit_btn:

    required_fields = [
        student_name,
        roll_number,
        registration_number,
        father_name,
        mother_name,
        email,
        mobile,
        address
    ]

    if (
        any(field.strip() == "" for field in required_fields)
        or course == "Select Course"
        or semester == "Select Semester"
    ):
        st.error("⚠️ Please fill all required fields.")
    else:

        st.success("✅ Registration Submitted Successfully!")

        st.markdown("---")
        st.subheader("Submitted Details")

        st.write(f"**Student Name:** {student_name}")
        st.write(f"**Roll Number:** {roll_number}")
        st.write(f"**Registration Number:** {registration_number}")
        st.write(f"**Father's Name:** {father_name}")
        st.write(f"**Mother's Name:** {mother_name}")
        st.write(f"**Date of Birth:** {dob}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Email:** {email}")
        st.write(f"**Mobile Number:** {mobile}")
        st.write(f"**Course:** {course}")
        st.write(f"**Semester:** {semester}")
        st.write(f"**Address:** {address}")

        st.balloons()
