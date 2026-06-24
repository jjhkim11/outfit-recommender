import streamlit as st
import logic, importlib
importlib.reload(logic)

st.set_page_config(page_title="오늘의 코디 추천기", page_icon="👕", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap');
* { font-family: 'Noto Sans KR', sans-serif; }

.title-box {
    border: 2px solid #333;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    margin-bottom: 8px;
}

/* radio 버튼을 pill 모양으로 */
div[role="radiogroup"] {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
div[role="radiogroup"] label {
    border: 1.5px solid #aaa;
    border-radius: 50px;
    padding: 6px 16px;
    cursor: pointer;
    font-size: 14px;
    background: white;
    transition: all 0.2s;
}
div[role="radiogroup"] label:has(input:checked),
div[role="radiogroup"] label:has(input:checked) p,
div[role="radiogroup"] label:has(input:checked) span {
    background-color: #333 !important;
    color: white !important;
    border-color: #333 !important;
    -webkit-text-fill-color: white !important;
}

/* radio 동그라미 숨기기 */
div[role="radiogroup"] input[type="radio"] {
    display: none;
}

/* 추천 버튼 */
div.stButton > button {
    border-radius: 8px;
    background-color: #333;
    color: white;
    font-size: 16px;
    font-weight: 500;
    width: 100%;
    padding: 12px;
    border: none;
}
div.stButton > button:hover {
    background-color: #555;
}

.result-box {
    border: 1.5px solid #ddd;
    border-radius: 12px;
    padding: 20px;
    background-color: white;
    margin-top: 16px;
}
hr { border: none; border-top: 1px solid #eee; margin: 12px 0; }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="title-box">
    <h2 style="margin:0; font-weight:700;">👕 오늘의 코디 추천기 👖</h2>
    <p style="margin:4px 0 0 0; color:#666; font-size:14px;">오늘 당신에게 어울리는 스타일은?</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


temp, condition = logic.get_weather("Busan")
st.info(f"🌤 현재 날씨: 부산 {temp}도, {condition}")

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown("**오늘 일정은 무엇인가요?**")
schedule = st.radio(
    "일정 선택",  
    ["🎓 수업", "🧑‍🤝‍🧑 친구 약속", "🏠 집콕", "💑 데이트"],
    horizontal=True,
    label_visibility="collapsed"  
)

st.markdown("<hr>", unsafe_allow_html=True)


st.markdown("**원하는 분위기는?**")
style = st.radio(
    "",
    ["😎 캐주얼", "✨ 깔끔하게", "😌 편하게"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<hr>", unsafe_allow_html=True)


recommend = st.button("코디 추천받기 🎯", use_container_width=True)


if recommend:
    with st.spinner("AI가 코디를 고르고 있어요..."):
        result = logic.get_outfit_recommendation(
            temp, condition, schedule, style
        )
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown("#### ✨ 오늘의 추천 코디")
    st.markdown(result)
    st.markdown('</div>', unsafe_allow_html=True)
