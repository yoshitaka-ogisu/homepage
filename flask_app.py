from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# 保存先ディレクトリとファイルの設定
SAVE_DIR = os.path.dirname(os.path.abspath(__file__))  # 現在のスクリプトと同じディレクトリ
CSV_FILE = os.path.join(SAVE_DIR, 'reactions.csv')

# 講義パスワード（初期値）
current_lecture_password = "LECTURE0001"

# 管理者パスワード
ADMIN_PASSWORD = "teacher2024"



# トップページのルート設定
@app.route('/')
def index():
    return render_template('form.html')  # form.htmlをレンダリング

# フォーム送信の処理
@app.route('/submit_reaction', methods=['POST'])
def handle_reaction():
    if request.form['lecture_password'] != current_lecture_password:
        return "講義パスワードが正しくありません。", 403

    student_id = request.form.get('student_id', '未入力')
    reaction_content = request.form['reaction_content']
    assignment_response = request.form.get('assignment_response', '')

    submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #  CSVファイルが存在しない場合、ヘッダーを作成
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', encoding='utf-8') as f:
            f.write('送信日時,学籍番号,リアクション,課題回答\n')

    # データの保存
    try:
        with open(CSV_FILE, 'a', encoding='utf-8') as f:
            f.write(f'"{submission_time}","{student_id}","{reaction_content}","{assignment_response}"\n')
        return "送信が完了しました。ありがとうございました。"
    except Exception as e:
        print(f"保存エラー: {e}")  # サーバーログにエラーを出力
        return "送信中にエラーが発生しました。", 500


# 管理者ページ表示
@app.route('/admin')
def admin_page():
    return render_template('admin.html', current_password=current_lecture_password)

# パスワード変更処理
@app.route('/admin/change_password', methods=['POST'])
def change_password():
    if request.form['admin_password'] == ADMIN_PASSWORD:
        global current_lecture_password
        current_lecture_password = request.form['new_password']
        return render_template('admin.html',
                             current_password=current_lecture_password,
                             message="パスワードを更新しました")
    return "管理者認証に失敗しました", 403


# 実行用コードを追加
if __name__ == '__main__':
    app.run(debug=True)