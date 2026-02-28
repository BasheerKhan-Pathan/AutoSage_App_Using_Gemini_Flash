import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(input_prompt, image):
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded. Please upload an image to analyze.")

input_prompt = """
You are an expert vehicle analyst with comprehensive knowledge about two-wheelers and four-wheelers.
Analyze the vehicle image provided and give detailed information including:

1. **Brand & Model**: Identify the manufacturer and specific model name
2. **Vehicle Type**: Specify if it's a two-wheeler (motorcycle, scooter) or four-wheeler (car, SUV, truck, etc.)
3. **Key Features**: List notable features visible or known about this model
4. **Estimated Mileage**: Provide fuel efficiency information (km/l or mpg)
5. **Engine Specifications**: Engine capacity, type, and power output
6. **Price Range**: Approximate market price (mention currency and region if possible)
7. **Target Audience**: Who is this vehicle best suited for
8. **Pros and Cons**: List advantages and disadvantages
9. **Competitor Comparison**: Mention similar competing models
10. **Special Notes**: Any unique aspects, awards, or interesting facts about this vehicle

Please provide accurate, detailed, and helpful information to assist potential buyers in making informed decisions.
"""

st.set_page_config(page_title="AutoSage - Vehicle Expert", page_icon="🚗", layout="wide")

st.title("🚗 AutoSage App")
st.subheader("Your AI-Powered Vehicle Information Assistant")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📸 Upload Vehicle Image")
    st.markdown("Upload a clear image of any two-wheeler or four-wheeler to get comprehensive information.")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Vehicle Image")

with col2:
    st.markdown("### ℹ️ About AutoSage")
    st.info("""
    **AutoSage** is powered by Google's Gemini Flash AI technology to provide:

    - 🔍 Detailed vehicle specifications
    - 💰 Price information and comparisons
    - ⚡ Performance metrics
    - 🎯 Expert recommendations
    - 🌟 Pros and cons analysis

    Simply upload a vehicle image and click **Analyze Vehicle** to get started!
    """)

st.markdown("---")

submit = st.button("🔍 Analyze Vehicle", use_container_width=True, type="primary")

if submit:
    if uploaded_file is not None:
        with st.spinner("🤖 AI is analyzing the vehicle... Please wait..."):
            try:
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response(input_prompt, image_data)

                st.markdown("---")
                st.markdown("## 📊 Vehicle Analysis Results")
                st.markdown(response)

                st.success("✅ Analysis completed successfully!")

                with st.expander("💡 Want to know more?"):
                    st.write("You can upload a different vehicle image to compare or get more information about other models.")

            except Exception as e:
                st.error(f"❌ Error occurred: {str(e)}")
                st.info("Please make sure you have set up your Google API key correctly in the .env file.")
    else:
        st.warning("⚠️ Please upload a vehicle image first before clicking Analyze!")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Made with ❤️ using Gemini Flash AI | AutoSage © 2024</p>
    <p><em>Helping you make informed vehicle purchasing decisions</em></p>
</div>
""", unsafe_allow_html=True)
