import streamlit as st
import json
from datetime import datetime
import pytz
import urllib.parse

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# ユーザーの投稿内容をチェックする関数
def check_post_content(content):
    # タイトルと投稿内容の禁止ワードの検出
    for banned_word in banned_words:
        if banned_word in content:
            content = content.replace(banned_word, "＠" * len(banned_word))
    return content

def save_post(content):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"content": content, "timestamp": now_str}
    with open('posts.json', 'a') as file:
        file.write(json.dumps(post))
        file.write('\n')

def load_posts():
    with open('posts.json', 'r') as file:
        lines = file.readlines()
        posts = [json.loads(line.strip()) for line in lines]
        
        # タイムスタンプを日本時間に変換
        for post in posts:
            timestamp = datetime.strptime(post['timestamp'], "%Y-%m-%d %H:%M:%S")
            timestamp = pytz.timezone("Asia/Tokyo").localize(timestamp)
            post['timestamp'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        return posts

def main():
    st.title("テスト")

    # 新規投稿の入力
    new_post_content = st.text_area("投稿", height=100)

    
    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_content:
        new_post_content = check_post_content(new_post_content)
        if "＠" in new_post_content:
            st.warning("禁止ワードが含まれています！")

        save_post(new_post_content)
        st.success("投稿が保存されました！")

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")

    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            st.subheader(post['content'])
            st.write(post['timestamp'])  # タイムスタンプを表示
            st.markdown("---")
import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import streamlit as st
import streamlit as st

# 投稿を格納するリスト
messages = []

def add_message(message):
    messages.append(message)

def delete_message(message):
    if message in messages:
        messages.remove(message)

def display_messages():
    if len(messages) == 0:
        st.write("まだ投稿はありません。")
    else:
        for i, message in enumerate(messages, start=1):
            st.write(f"{i}. {message}")

# メインのStreamlitアプリケーション
def main():
    st.title("掲示板アプリ")

    # メッセージの入力と追加
    new_message = st.text_input("新しいメッセージを入力してください:")
    if st.button("投稿"):
        add_message(new_message)

    # メッセージの表示と削除
    display_messages()

    if len(messages) > 0:
        st.subheader("メッセージの削除")
        message_to_delete = st.selectbox("あ:", messages)
        delete_word = st.text_input("あ:")
        if st.button("削除") and delete_word in message_to_delete:
            delete_message(message_to_delete)
            st.success("メッセージが削除されました。")

if __name__ == "__main__":
    main()