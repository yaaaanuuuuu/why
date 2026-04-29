 사용 중입니다. 구체적인 사물 명칭으로 모델링 해주세요."
    else:
        feedback = "적절한 발화입니다. 확장을 통해 문장을 길게 만들어주세요."
        
    return word_count, feedback

# UI 구성
st.title("💡 아동 발화 분석 및 코칭 도구")
st.write("아동의 발화를 입력하면 간단한 분석과 피드백을 제공합니다.")

user_input = st.text_input("아동의 발화를 입력하세요:", "선생님 이거 싫어")

if st.button("분석하기"):
    count, advice = analyze_speech(user_input)
    st.info(f"**분석 결과:** 어절 수 약 {count}개")
    st.success(f"**추천 피드백:** {advice}")
"""

with open('app.py', 'w') as f:
    f.write(content)