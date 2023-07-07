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
        message_to_delete = st.selectbox("削除するメッセージを選択してください:", messages)
        delete_word = st.text_input("削除ワードを入力してください:")
        if st.button("削除") and delete_word in message_to_delete:
            delete_message(message_to_delete)
            st.success("メッセージが削除されました。")

if __name__ == "__main__":
    main()
