"""
Streamlit App for Machine Learning Deployment (MBTI Inference)
"""

import time
import json
import streamlit as st


RELATIVE_PATH = "big_five_personality_test/streamlit/"

st.title("MBTI Machine Learning Inference 🚀")
st.caption("powered by LightGBM, GCP Cloud Run, and ken🌚")

st.header("What is MBTI 🤔")
st.markdown("""
The MBTI® assessment is designed to help people identify and gain some understanding around how they take in information and make decisions, the patterns of perception and judgment, as seen in normal, healthy behavior.
""")

st.subheader("Take 10 questions to get prediction of your MBTI 🥳")
st.caption("from the full test having approxiamately 94 questions 😱")
st.caption("Model's Accuracy = xx.xx % / F1-Score = xx.xx %")

map_input_dict = {
    ":blue[1]": 1, 
    ":green[2]": 2, 
    "3": 3, 
    ":orange[4]": 4, 
    ":red[5]": 5
}
    
with st.form("ml_input"):
    qa_1 = st.radio(
        label="1. Question-1",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_2 = st.radio(
        "2. Question-2",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_3 = st.radio(
        "3. Question-3",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_4 = st.radio(
        "4. Question-4",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_5 = st.radio(
        "5. Question-5",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_6 = st.radio(
        "6. Question-6",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_7 = st.radio(
        "7. Question-7",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_8 = st.radio(
        "8. Question-8",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
    horizontal=True,
        index=None,
    )

    qa_9 = st.radio(
        "9. Question-9",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )
    
    qa_10 = st.radio(
        "10. Question-10",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    submitted = st.form_submit_button("Submit")
    if submitted:
        raw_input = [qa_1, qa_2, qa_3, qa_4, qa_5, qa_6, qa_7, qa_8, qa_9, qa_10]
        if None not in raw_input:
            input_data = [map_input_dict[choice] for choice in raw_input]
            with st.spinner("wait for it..."):
                # TODO: change this to dynamic from inference
                # pre-processing
                # input = 

                # load model and predict
                time.sleep(5)
                # model = pickle.load("model/mbti_lgbm.bin")
                # labeler = pickle.load(model/labeler.pkl)
                # raw_personality = model.predict(input)
                # personality = labeler.inverse_transform(raw_personality)
                personality = "ISFJ-T"
                st.balloons()
            st.success(f"Done! your MBTI is '{personality}' 🚀", icon="✅")

            # extract data
            with open(f'{RELATIVE_PATH}mbti_info/letters_info.json') as json_file:
                letters_info = json.load(json_file)
            with open(f'{RELATIVE_PATH}mbti_info/mbti_info.json') as json_file:
                mbti_info = json.load(json_file)

            letter_1 = personality[0]
            letter_2 = personality[1]
            letter_3 = personality[2]
            letter_4 = personality[3]
            letter_5 = personality[4:]
            personality_short = personality[:-2]

            # fill in details about personality
            st.image(f"{RELATIVE_PATH}picture/{personality_short.lower()}.png", caption="MBTI Character")
            st.write(f"""
                - **Group**: {mbti_info.get(personality_short).get("group")}
                - **Role**: {mbti_info.get(personality_short).get("role")}
                - **Summary**:
                    - {mbti_info.get(personality_short).get("description")}
            """)
            st.link_button(":blue[More about your MBTI]", mbti_info.get(personality_short).get("link"))
            st.subheader(f"Personality Detail: {personality} 🌟")
            st.markdown(f"""
                - 📍 {letters_info.get(letter_1)}
                    - {letters_info.get("IE")}
                - 📍 {letters_info.get(letter_2)}
                - 📍 {letters_info.get(letter_3)}
                    - {letters_info.get("TF")}
                - 📍 {letters_info.get(letter_4)}
                - 📍 {letters_info.get(letter_5)}
            """)
        else:
            st.error("Questions are not fully answered.")

# appendix
columns = st.columns(2)
with columns[0]:
    st.link_button(":green[Take the Full Test from Official Site. 📊]", "https://www.16personalities.com/free-personality-test")
with columns[1]:
    st.link_button("Check Out for other Personalities 🌎", "https://www.16personalities.com/personality-types")
