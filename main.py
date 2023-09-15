import json
from datetime import datetime
import pytz
import urllib.parse
import streamlit as st
# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]
# 各投稿にgoodとbadの評価を保持するための辞書
post_ratings = {}
def check_post_content(title, content):
    # 禁止ワードが含まれているかチェック
    for word in banned_words:
        if word in title or word in content:
            st.warning("禁止ワードが含まれています！")
            return "", ""
    return title, content
def save_post(title, content):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str, "good": 0, "bad": 0}
    with open('posts.json', 'a') as file:
        file.write(json.dumps(post))
        file.write('\n')
    post_ratings[title] = {"good": 0, "bad": 0}  # 評価カウンターを初期化
def load_posts():
    with open('posts.json', 'r') as file:
        lines = file.readlines()
        posts = [json.loads(line.strip()) for line in lines]
        # タイムスタンプを日本時間に変換
        for post in posts:
            timestamp = datetime.strptime(post['timestamp'], "%Y-%m-%d %H:%M:%S")
            timestamp = pytz.timezone("Asia/Tokyo").localize(timestamp)
            post['timestamp'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            # 評価カウンターを初期化
            post_ratings[post["title"]] = {"good": 0, "bad": 0}
        return posts
def main():
    st.title("掲示板アプリ")
    # 新規投稿の入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")
    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
        if new_post_title and new_post_content:
            save_post(new_post_title, new_post_content)
    # 投稿一覧を表示
    posts = load_posts()
    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            # 各タイトルにリンクを付けて表示
            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"
            st.subheader(post['content'])
            st.write(post['timestamp'])  # タイムスタンプを表示

            # GoodボタンとBadボタンを追加
            col1, col2 = st.columns(2)
            good_button = col1.button(f"Good ({post_ratings[post['title']]['good']})", key=f"good_{post['title']}")
            bad_button = col2.button(f"Bad ({post_ratings[post['title']]['bad']})", key=f"bad_{post['title']}")
            if good_button:
	@@ -81,3 +81,4 @@ def main():

    # Goodボタンのイラスト
    good_icon = "👍"

    # Badボタンのイラスト
    bad_icon = "👎"

def main():
    st.title("GoodボタンとBadボタンのイラスト")

    st.markdown("Goodボタンをクリックすると、Goodのカウントが増えます。")
    st.markdown("Badボタンをクリックすると、Badのカウントが増えます。")

    good_count = st.button(f"{good_icon} Good")
    bad_count = st.button(f"{bad_icon} Bad")

    st.write(f"Good: {good_count}")
    st.write(f"Bad: {bad_count}")

if __name__ == "__main__":
    main()