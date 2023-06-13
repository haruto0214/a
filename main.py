
import streamlit as st
import sqlite3

import streamlit as st

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
st.title("Bulletin Board App")

# 新しい投稿の作成
st.header("Create New Post")
title = st.text_input("Title")
content = st.text_area("Content")
if st.button("Create"):
    create_post(title, content)
    st.success("Post created successfully!")

# 投稿一覧の表示
st.header("Posts")
if len(posts) == 0:
    st.info("No posts yet.")
else:
    show_posts()

# データベース接続とテーブル作成
conn = sqlite3.connect('posts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS posts (content TEXT)''')

# 投稿の保存
def save_post(content):
    c.execute("INSERT INTO posts VALUES (?)", (content,))
    conn.commit()

# Streamlitアプリケーションの設定
st.title('掲示板アプリ')

# 投稿フォーム
new_post = st.text_input('新規投稿')
if st.button('投稿'):
    save_post(new_post)
    st.success('投稿が保存されました。')

# データベースから投稿を読み込み表示
c.execute("SELECT * FROM posts")
posts = c.fetchall()
for post in posts:
    st.write(f'- {post[0]}')

# データベース接続をクローズ
conn.close()

