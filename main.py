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

import json

def save_post(title, content):
    post = {"title": title, "content": content}
    with open('posts.json', 'a') as file:
        json.dump(post, file)
        file.write('\n')

    print("投稿を保存しました。")
    print("[保存された投稿を表示する](load_posts)")

def load_posts():
    with open('posts.json', 'r') as file:
        posts = [json.loads(line) for line in file]

    if len(posts) > 0:
        print("保存された投稿:")
        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post['title']}: {post['content']}")
    else:
        print("保存された投稿はありません。")
    print("[新しい投稿を保存する](save_post)")



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
            # 各タイトルにリンクを付けて表示
            post_url = f"[{post['title']}](#{post['title']})"
            st.markdown(post_url, unsafe_allow_html=True)
            st.write(post['content'])
            st.markdown("---")

if __name__ == "__main__":
    main()


