import json
from datetime import datetime
import pytz
import urllib.parse
#goodボタンとbadボタンのカウンター変数
good_counter = 0
bad_counter = 0

# Goodボタンのイラスト
good_icon = "👍"

# Badボタンのイラスト
bad_icon = "👎"

for post in posts:
    # 各タイトルにリンクを付けて表示
    post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"
    st.subheader(post['content'])
    st.write(post['timestamp'])  # タイムスタンプを表示
    
    # Goodボタン
    if st.button(f"Good ({good_counter})", key=f"good_{post['title']}"):
        good_counter += 1
    
    # Badボタン
    if st.button(f"Bad ({bad_counter})", key=f"bad_{post['title']}"):
        bad_counter += 1
    
    st.markdown(post_url, unsafe_allow_html=True)
    st.markdown("---")

def save_post(title, content):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str}
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
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")
    
    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
        st.info("まだ投稿がありません。")
　　#ボタンカウンター
        st.title("GoodボタンとBadボタンのイラスト")

    st.markdown("Goodボタンをクリックすると、Goodのカウントが増えます。")
    st.markdown("Badボタンをクリックすると、Badのカウントが増えます。")

    good_count = st.button(f"{good_icon} Good")
    bad_count = st.button(f"{bad_icon} Bad")

    st.write(f"Good: {good_count}")
    st.write(f"Bad: {bad_count}")

if __name__ == "__main__":
    main()