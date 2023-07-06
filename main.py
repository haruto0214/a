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

def delete_post(posts, post_id):
    # 投稿を削除する処理を実装する
    # ここではダミーのデータフレームを使用しています
    posts = posts[posts['post_id'] != post_id]
    return posts

def main():
    # 過去の投稿を格納するデータフレームを作成する
    posts = pd.DataFrame({
        'post_id': [1, 2, 3],
        'content': ['投稿1', '投稿2', '投稿3']
    })

    st.title('投稿削除アプリ')

    # 投稿一覧を表示する
    st.subheader('投稿一覧')
    st.dataframe(posts)

    # 削除する投稿のIDを入力する
    post_id = st.text_input('削除する投稿のIDを入力してください')

    # 削除ボタンがクリックされた場合の処理
    if st.button('削除'):
        if post_id:
            try:
                post_id = int(post_id)
                posts = delete_post(posts, post_id)
                st.success('投稿が削除されました')
            except ValueError:
                st.error('無効な投稿IDです')
        else:
            st.warning('投稿IDを入力してください')

    # 更新された投稿一覧を表示する
    st.subheader('更新された投稿一覧')
    st.dataframe(posts)

if __name__ == "__main__":
    main()