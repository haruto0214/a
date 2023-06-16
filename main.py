
import streamlit as st
import json

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

def save_post(title, content):
    post = {"title": title, "content": content}
    with open('posts.json', 'a') as file:
        json.dump(post, file)
        file.write('\n')

def load_posts():
    with open('posts.json', 'r') as file:
        return [json.loads(line) for line in file]

def main():
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post_title = st.text_input("タイトル")
    new_post_content = st.text_area("新規投稿", height=100)

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
        if "＠" in new_post_title or "＠" in new_post_content:
            st.warning("禁止ワードが含まれています！")

        save_post(new_post_title, new_post_content)
        st.success("投稿が保存されました！")

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")

    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            st.text(post["title"])
            st.text(post["content"])
            st.markdown("---")

if __name__ == "__main__":
    main()

import streamlit as st

# 投稿クラス
class Post:
    def __init__(self, title, content, link):
        self.title = title
        self.content = content
        self.link = link

# 投稿のリスト
posts = [
    Post("投稿1", "これは投稿1の内容です。", "https://example.com/post1"),
    Post("投稿2", "これは投稿2の内容です。", "https://example.com/post2"),
    Post("投稿3", "これは投稿3の内容です。", "https://example.com/post3")
]

# 掲示板アプリ
def main():
    st.title("掲示板アプリ")

    # 各投稿を表示
    for post in posts:
        # タイトルをリンクとして表示
        st.markdown(f"## [{post.title}]({post.link})")
        st.write(post.content)

if __name__ == "__main__":
    main()


