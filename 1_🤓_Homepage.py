import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)


st.sidebar.header(":mailbox: Get In Touch With Me (customised-branch)!")


contact_form = """
<form action="https://data.endpoint.space/cl6o3mf5j001809mbpcf1n6gg" method="POST">
     <input type="text" name="artistName" placeholder="artist name" required>
     <input type="email" name="email" placeholder="artistname@email.com" required>
     <textarea name="message" placeholder="Drop a hi!"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.sidebar.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/styles.css")