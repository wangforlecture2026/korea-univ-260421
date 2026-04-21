import streamlit as st

# 페이지 제목
st.title("🎉 자기소개")

# 이름과 간단한 소개
st.header("이름: 왕효원")
st.write("안녕하세요! 저는 수학교육 연구자입니다. 예를 들어, 저는 [직업/전공]을 하고 있으며, [관심사나 취미]를 좋아합니다.")

# 추가 섹션: 사진 (선택사항)
st.subheader("사진")
st.write("여기에 사진을 추가할 수 있습니다.")
# st.image("path/to/your/photo.jpg", caption="제 사진", use_column_width=True)

# 연락처 정보
st.subheader("연락처")
st.write("이메일: [your.email@example.com]")
st.write("GitHub: [https://github.com/yourusername]")

# 추가 정보
st.subheader("더 자세한 정보")
st.write("저에 대해 더 알고 싶으시면 아래에 추가 내용을 작성하세요.")
