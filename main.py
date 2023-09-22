import streamlit as st
import json
from datetime import datetime
import pytz
import urllib.parse

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# ユーザーの投稿内容をチェックする関数
def check_post_content(title, content):
    # タイトルと投稿内容の禁止ワードの検出
    for banned_word in banned_words:
        if banned_word in title:
            title = title.replace(banned_word, "＠" * len(banned_word))
        if banned_word in content:
            content = content.replace(banned_word, "＠" * len(banned_word))
    return title, content

# 投稿ごとのGoodとBadのカウンターを管理する辞書
post_votes = {}

# イラストのGoodとBadのカウンターを管理する辞書
illustration_votes = {}

def save_post(title, content, is_illustration):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str}
    with open('posts.json', 'a') as file:
        file.write(json.dumps(post))
        file.write('\n')
    if is_illustration:
        # イラストの場合、カウンターを初期化
        illustration_votes[title] = {'good': 0, 'bad': 0}

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
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")

    # イラストかどうかの選択
    is_illustration = st.checkbox("イラスト")

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
        if "＠" in new_post_title or "＠" in new_post_content:
            st.warning("禁止ワードが含まれています！")
        save_post(new_post_title, new_post_content, is_illustration)
        st.success("投稿が保存されました！")

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")
    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            # 各タイトルにリンクを付けて表示
            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"

            # 投票ボタンを追加
            good_button = st.button(f"Good ({post_votes.get(post['title'], {'good': 0}).get('good', 0)})", key=f"good_{post['title']}")
            bad_button = st.button(f"Bad ({post_votes.get(post['title'], {'bad': 0}).get('bad', 0)})", key=f"bad_{post['title']}")

            if good_button:
                # Goodボタンが押された場合の処理
                if post['title'] in post_votes:
                    post_votes[post['title']]['good'] += 1
                else:
                    post_votes[post['title']] = {'good': 1, 'bad': 0}
                st.success("Goodボタンが押されました！")

            if bad_button:
                # Badボタンが押された場合の処理
                if post['title'] in post_votes:
                    post_votes[post['title']]['bad'] += 1
                else:
                    post_votes[post['title']] = {'good': 0, 'bad': 1}
                st.warning("Badボタンが押されました！")

            st.subheader(post['content'])
            st.write(post['timestamp'])  # タイムスタンプを表示
            if is_illustration:
                st.write(f"Good: {illustration_votes.get(post['title'], {'good': 0}).get('good', 0)}")
                st.write(f"Bad: {illustration_votes.get(post['title'], {'bad': 0}).get('bad', 0)}")
            st.markdown(post_url, unsafe_allow_html=True)
            st.markdown("---")

if __name__ == "__main__":
    main()

