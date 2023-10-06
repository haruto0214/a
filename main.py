import streamlit as st
import json
from datetime import datetime
import pytz

def save_post(content, good_count, bad_count):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"content": content, "timestamp": now_str, "good_count": good_count, "bad_count": bad_count}
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
    
    # グッドボタンとバッドボタンのカウントを初期化
    good_count = 0
    bad_count = 0

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_content:
        new_post_content = check_post_content(new_post_content)
        if "＠" in new_post_content:
            st.warning("禁止ワードが含まれています！")
        save_post(new_post_content, good_count, bad_count)
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

            # グッドボタンとバッドボタンを表示
            if st.button(f"グッドボタン ({post['good_count']})"):
                post['good_count'] += 1
                st.success("グッドボタンがクリックされました！")

            if st.button(f"バッドボタン ({post['bad_count']})"):
                post['bad_count'] += 1
                st.error("バッドボタンがクリックされました！")

            st.markdown("---")

if __name__ == "__main__":
    main()
