
import math
import streamlit as st
import pandas as pd

st.text("ヤッハロー")
#         ↑ガハマすこ

# 投稿データを保持するリスト
posts = []

# 投稿の作成
def create_post(title, content):
    posts.append({"title": title, "content": content})

# 投稿の表示
def show_posts():
    for post in posts:
        st.write(f"**{post['title']}**")
        st.write(post['content'])
        st.write('---')

# 掲示板アプリのタイトル
st.title("舞チャン")

# 新しい投稿の作成
st.header("新しい投稿を作成")
title = st.text_input("スレタイトル")
content = st.text_area("内容")
if st.button("作成！"):
    create_post(title, content)
    st.success("作成完了！")

# 投稿一覧の表示
st.header("スレタイトル一覧")
if len(posts) == 0:
    st.info("まだ投稿はありません")
else:
    show_posts()
import streamlit as st

<<<<<<< HEAD
# 禁止ワードのリスト
banned_words = ["バカ", "禁止ワード2", "禁止ワード3"]
=======
import streamlit as st
>>>>>>> 1f7fe387894e5b6aa0ebcf8c403b4b5060ae0593

<<<<<<< HEAD
# ユーザーの投稿内容をチェックする関数
def check_post_content(post_content):
    # 禁止ワードの検出
    for banned_word in banned_words:
        if banned_word in post_content:
            return True # 禁止ワードが検出された場合はTrueを返す
    return False # 禁止ワードが検出されなかった場合はFalseを返す
=======
# 禁止ワードのリスト
banned_words = ["バカ", "禁止ワード2", "禁止ワード3"]
>>>>>>> 1f7fe387894e5b6aa0ebcf8c403b4b5060ae0593

<<<<<<< HEAD
# 掲示板アプリのメイン処理
def main():
    st.title("掲示板アプリ")
    
    # ユーザーの投稿内容を入力
    post_content = st.text_input("投稿内容")
    
    # 投稿ボタンがクリックされた場合の処理
    if st.button("投稿"):
        # 禁止ワードのチェック
        if check_post_content(post_content):
            # 禁止ワードが検出された場合は警報を出す
            st.warning("禁止ワードが含まれています！")
        
        # 投稿内容を表示
        st.write("投稿内容:", post_content)
=======
# ユーザーの投稿内容をチェックする関数
def check_post_content(post_content):
    # 禁止ワードの検出
    for banned_word in banned_words:
        if banned_word in post_content:
            return True # 禁止ワードが検出された場合はTrueを返す
    return False # 禁止ワードが検出されなかった場合はFalseを返す
>>>>>>> 1f7fe387894e5b6aa0ebcf8c403b4b5060ae0593

<<<<<<< HEAD
# アプリの実行
if __name__ == "__main__":
    main()
=======
# 掲示板アプリのメイン処理
def main():
    st.title("掲示板アプリ")
    
    # ユーザーの投稿内容を入力
    post_content = st.text_input("投稿内容")
    
    # 投稿ボタンがクリックされた場合の処理
    if st.button("投稿"):
        # 禁止ワードのチェック
        if check_post_content(post_content):
            # 禁止ワードが検出された場合は警報を出す
            st.warning("禁止ワードが含まれています！")
        
        # 投稿内容を表示
        st.write("投稿内容:", post_content)
>>>>>>> 1f7fe387894e5b6aa0ebcf8c403b4b5060ae0593

<<<<<<< HEAD
=======
# アプリの実行
if __name__ == "__main__":
    main()


>>>>>>> 1f7fe387894e5b6aa0ebcf8c403b4b5060ae0593