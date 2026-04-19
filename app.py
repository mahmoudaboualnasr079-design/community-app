import streamlit as st

st.set_page_config(page_title="مبادرة محمود للمجتمع", page_icon="🌟")

st.title("🌟 منصة محمود لخدمة المجتمع")
st.subheader("أهلاً بك في تطبيقنا الأول للعمل الخيري")

name = st.text_input("اكتب اسمك يا بطل:")
task = st.selectbox("إيه العمل اللي تحب تشارك فيه؟", ["توزيع وجبات", "تنظيف الشوارع", "تعليم الأطفال", "تبرع بالملابس"])

if st.button("تسجيل مشاركتي"):
    if name:
        st.balloons()
        st.success(f"شكراً يا {name}! تم تسجيل رغبتك في {task}. إنت فخر للمجتمع!")
    else:
        st.warning("من فضلك اكتب اسمك أولاً")
