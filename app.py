import streamlit as st

# Custom CSS for Background Image & Styling
st.markdown(
    """
    <style>
        /* Background Image */
        .stApp {
            background-image: url('https://img.freepik.com/premium-photo/beautiful-blank-background-with-stack-books_955712-17973.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }

        /* Heading Styling */
        .main-title {
            color: white;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
            border: 3px solid skyblue;
            background: rgba(0, 0, 0, 0.6);
        }

        /* Subheading Styling */
        .sub-title {
            color: white;
            text-align: center;
            font-size: 25px;
            font-weight: bold;
            padding: 8px;
            border-radius: 8px;
            border: 2px solid skyblue;
            background: rgba(0, 0, 0, 0.5);
        }

        /* Text Styling */
        .styled-text {
            color: white;
            font-size: 18px;
            padding: 10px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 5px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: skyblue;
            color: black;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
        }

        /* Input Box Styling */
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            background-color: rgba(255, 255, 255, 0.8);
            border: 2px solid skyblue;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("📜 Text Analyzer")

# User Input
st.header("📖 Enter Your Paragraph:")
paragraph = st.text_area("")

# Search & Replace Functionality
st.header("🔍 Search & Replace")
search_word = st.text_input("Enter the word to search for:")
replace_word = st.text_input("Enter the word to replace it with:")

if st.button("Replace Word"):
    if search_word in paragraph:
        modified_paragraph = paragraph.replace(search_word, replace_word)
        st.success("✅ Replacement Successful!")
        st.subheader("✨ Modified Paragraph:")
        st.markdown(f'<div class="custom-box">{modified_paragraph}</div>', unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ '{search_word}' not found in the paragraph.")

# Uppercase & Lowercase Conversion
st.header("🔠 Uppercase & Lowercase Conversion")
if paragraph:
    st.subheader("🔡 Uppercase Version:")
    st.markdown(f'<div class="custom-box">{paragraph.upper()}</div>', unsafe_allow_html=True)

    st.subheader("🔠 Lowercase Version:")
    st.markdown(f'<div class="custom-box">{paragraph.lower()}</div>', unsafe_allow_html=True)

# Type Casting: Word & Vowel Count
st.header("🔢 Word & Vowel Count")

word_count = len(paragraph.split())  
vowel_count = sum(1 for char in paragraph.lower() if char in "aeiou")  

st.write(f"📜 **Total Words:** {str(word_count)}")  
st.write(f"🔠 **Total Vowels:** {str(vowel_count)}")

# Operators: Check for "Python" & Average Word Length
st.header("📚 Operators & Calculations")

# Checking for the word "Python"
if "Python" in paragraph:
    st.success("✅ The paragraph contains the word 'Python'.")
else:
    st.warning("❌ The paragraph does not contain the word 'Python'.")

# Average Word Length Calculation
total_chars = len(paragraph.replace(" ", ""))  
average_word_length = total_chars / word_count if word_count > 0 else 0

st.write(f"📏 **Average Word Length:** {average_word_length:.2f}")

st.subheader("📜 Text Analysis Completed! 🚀")


 # Footer with Love ❤️
st.markdown('<div class="footer">Created with ❤️ by Shabnam Wahid</div>', unsafe_allow_html=True)