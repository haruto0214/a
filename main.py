import streamlit as st

def main():
    st.title("掲示板アプリ")

    # ユーザーが入力するためのテキストエリア
    user_input = st.text_area("投稿内容を入力してください:")

    # 投稿内容が空でない場合に番号をつけて表示
    if user_input:
        # 改行で分割し、各行に番号をつけて表示
        posts = user_input.split('\n')
        numbered_posts = [f"{i+1}. {post}" for i, post in enumerate(posts)]
        st.markdown("\n".join(numbered_posts))

if __name__ == "__main__":
    main()
