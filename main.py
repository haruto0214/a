import streamlit as st
import json
import pandas as pd
from datetime import datetime
import pytz
import urllib.parse

# 禁止ワードをExcelファイルから読み込む
df = pd.read_excel("banned_list.xlsx", sheet_name=0)
# 禁止ワードをbanned_wordsに
banned_words = df['禁止ワード'].tolist()
banned_words = [str(word) for word in banned_words]

# ユーザーの投稿内容をチェックする関数
def check_post_content(title, content):
    for banned_word in banned_words:
        if str(banned_word) in title:
            title = title.replace(banned_word, "＠" * len(banned_word))
        if banned_word in content:
            content = content.replace(banned_word, "＠" * len(banned_word))
    return title, content

def save_post(title, content, image):
    # タイムスタンプを設定
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str, "image": image}
    with open('posts.json', 'a') as file:
        file.write(json.dumps(post))
        file.write('\n')

def load_posts():
    with open('posts.json', 'r') as file:
        lines = file.readlines()
        posts = [json.loads(line.strip()) for line in lines]

    for post in posts:  # タイムスタンプを日本時間に変換
        timestamp = datetime.strptime(post['timestamp'], "%Y-%m-%d %H:%M:%S")
        timestamp = pytz.timezone("Asia/Tokyo").localize(timestamp)
        post['timestamp'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return posts

def main():
    st.title("掲示板アプリ")
    # ページのタイトルの入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")
    uploaded_file = st.file_uploader("画像をアップロード", type=["jpg", "jpeg", "png"])

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
        if "＠" in new_post_title or "＠" in new_post_content:
            st.warning("禁止ワードが含まれています！")
        save_post(new_post_title, new_post_content, uploaded_file)
        st.success("投稿が保存されました！")

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")
    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for i, post in enumerate(posts, 1):
            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"
            st.subheader(f"{i}. {post['content']}")
            if post['image'] is not None:
                st.image(post['image'], caption="投稿された画像", use_column_width=True)
            st.write(post['timestamp'])  # タイムスタンプ
            st.markdown(post_url, unsafe_allow_html=True)
            st.markdown("---")

if __name__ == "__main__":
    main()
