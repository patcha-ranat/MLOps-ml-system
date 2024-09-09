"""
Streamlit App for Machine Learning Deployment (MBTI Inference)
"""

import os
import json
import numpy as np
import pickle
import streamlit as st


RELATIVE_PATH = os.getenv("DOCKER_OPERATE", "mbti_ipip/streamlit/")

st.set_page_config(layout="wide")
st.title("MBTI Machine Learning Inference 🚀")
st.caption("powered by scikit-learn, GCP Cloud Run, and ken🌚")

st.header("What is MBTI 🤔")
st.markdown("""
The MBTI® assessment is designed to help people identify and gain some understanding around how they take in information and make decisions, the patterns of perception and judgment, as seen in normal, healthy behavior.
""")

st.subheader("Take 12 questions to get prediction of your MBTI 🥳")
st.caption("from the full test having approxiamately 94 questions 😱")
st.caption("Model: Logistic Regression - [Accuracy = 43.77 % / F1-Score = 40.01 % / Baseline (Random Guess) = 3.125 %]")

map_input_dict = {
    ":blue[1]": 1, 
    ":green[2]": 2, 
    "3": 3, 
    ":orange[4]": 4, 
    ":red[5]": 5
}
# read input list
with open(f'{RELATIVE_PATH}models/input_format.json', encoding="utf8") as json_file:
    input_format = json.load(json_file)
qa_list = [qa_code for qa_code in input_format.keys()]

with st.form("ml_input"):
    qa_1 = st.radio(
        label=f"1.) {input_format[qa_list[0]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_2 = st.radio(
        label=f"2.) {input_format[qa_list[1]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_3 = st.radio(
        label=f"3.) {input_format[qa_list[2]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_4 = st.radio(
        label=f"4.) {input_format[qa_list[3]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_5 = st.radio(
        label=f"5.) {input_format[qa_list[4]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_6 = st.radio(
        label=f"6.) {input_format[qa_list[5]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_7 = st.radio(
        label=f"7.) {input_format[qa_list[6]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_8 = st.radio(
        label=f"8.) {input_format[qa_list[7]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
    horizontal=True,
        index=None,
    )

    qa_9 = st.radio(
        label=f"9.) {input_format[qa_list[8]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )
    
    qa_10 = st.radio(
        label=f"10.) {input_format[qa_list[9]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_11 = st.radio(
        label=f"11.) {input_format[qa_list[11]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    qa_12 = st.radio(
        label=f"12.) {input_format[qa_list[10]]}",
        options=[":blue[1]", ":green[2]", "3", ":orange[4]", ":red[5]"],
        horizontal=True,
        index=None,
    )

    submitted = st.form_submit_button("Submit")
    if submitted:
        raw_input = [qa_1, qa_2, qa_3, qa_4, qa_5, qa_6, qa_7, qa_8, qa_9, qa_10, qa_11, qa_12]
        if None not in raw_input:
            input_data = [map_input_dict[choice] for choice in raw_input]
            with st.spinner("wait for it..."):
                # TODO: change this to dynamic from inference
                # pre-processing
                input_data = np.array(input_data).reshape(1, -1)

                # load model and predict
                # time.sleep(5)
                model = pickle.load(open(f"{RELATIVE_PATH}models/logistic_regression_mbti.bin", "rb"))
                decoder = pickle.load(open(f"{RELATIVE_PATH}models/encoder.pkl", "rb"))
                raw_personality = model.predict(input_data)
                personality = str(decoder.inverse_transform(raw_personality))[2:-2]
                # personality = "ISFJ-T"
                st.balloons()
            st.success(f"Done! your MBTI is '{personality}' 🚀", icon="✅")

            # extract data
            with open(f'{RELATIVE_PATH}mbti_info/letters_info.json', encoding="utf8") as json_file:
                letters_info = json.load(json_file)
            with open(f'{RELATIVE_PATH}mbti_info/mbti_info.json', encoding="utf8") as json_file:
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
