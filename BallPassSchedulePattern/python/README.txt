
# メモ
**2024-08-24**
各プレイヤーのインスタンスは、ballオブジェクトが持つべきだ。そのように変更しよう。  
プレイヤーを1つ作成する度に、プレイヤーを登録する作業が多すぎる。  
自動化しよう。  
そもそもballオブジェクトは全ての情報を"持つ"ように設計するべきだ。

**2024-08-26**  
ballオブジェクトに全ての情報を持たせる、というのはあくまでもメモリ上での話(実行中での話)であり、  
各プレイヤーが作成、用意しているデータは、各プレイヤーと同じディレクトリ層に位置させることにする。  
つまり、各プレイヤーの設定は、各プレイヤーと同じディレクトリ層にjsonで置くとする。  
または全ての設定をまとめたjsonをMainファイルの隣に置き、シンクさせることも必要かもしれない。

**2024-11-08**  
=== ATTENTION ===
現在KB_projectでかなりの進化を遂げている。このデザインパターンはかなりの進化を遂げている。
完成次第、ここのBallPassSchedulePatternも更新する。
=================

# 自己紹介
私の名前は、Masarinaまたは、Ri：naです。（@Masarina002）  
"独学の野生"のプログラマです。  
邪道だらけですが大目に見てください。。  
Twitter(X): @Masarina002

# Playerを追加方法

以下のフォーマットでPlayerを作成してください。

\`\`\`python
# ==== プレイヤーの名前.py ============================================================
from SuperPlayer import SuperPlayer 

class プレイヤーの名前(SuperPlayer):
    def __init__(self):
        self.my_name = "FinalPlayer"

    def main(self):
        # 任意の処理

        # 処理が完了したら、戻り値に必ず "Completed" を返してください。
        # なお、非同期関数などもこのmainに実行しても構いません。その場合、非同期関数が求める結果になったなら
        # world.ball.now_schedule_status[world.index_of_schedule][world.index_of_schedule_of_schedule] = "Completed"
        # としてください。"Completed"がステータスに入れば、自然と次のplayerに移行するはずです。

        return "Completed"
\`\`\`

このPlayerはBallObject.pyと同じディレクトリ層においてください。

---

Playerの作成が完了したら、Worldファイルにimportさせ、次のようにelif分岐を追加してください。

\`\`\`python
# ==== World.py ================================================================================
from ExamplePlayer import ExamplePlayer

# ・・・

def doing_next_players_catch_ball_method_by_player_name(self, player_name=None, world=None):
    if player_name == "FirstPlayer":
        self.firstPlayer.catch_ball(world=world)

    elif player_name == "DebugPlayer":
        self.debugPlayer.catch_ball(world=world)

    elif player_name == "FinalPlayer":
        self.finalPlayer.catch_ball(world=world)

    elif player_name == "ExamplePlayer":
        self.examplePlayer.catch_ball(world=world)
\`\`\`

---

次に、プレイヤーを任意にスケジュールしてください。BallObjectを編集します。

\`\`\`python
# ==== BallObject.py ========================================================================================
def schedule_dict(self, mode_name=None):
    array_2d = None

    # ・・・

    elif mode_name == "example_mode":
        array_2d = [
            [['FirstPlayer'], ["ExamplePlayer"]],  # 例: 第一ミニスケジュール
            [['ExamplePlayer']],  # 例: 第二ミニスケジュール
            [['ExamplePlayer'], ['DebugPlayer'], ['ExamplePlayer'], ['FinalPlayer']]  # 例: 第三ミニスケジュール
        ]

    self.now_schedule = array_2d
\`\`\`

---

次に、modeのスケジュールを設定してください。  
「このモードの次は、このモードを実行する」というイメージです。

\`\`\`python
# ==== BallObject.py ========================================================================================
def schedule_mode_settings(self):
    if self.schedule_mode == 'sample_mode':
        self.schedule_mode = 'sample2_mode'

    elif self.schedule_mode == 'sample2_mode':
        self.schedule_mode = "example_mode"

    elif self.schedule_mode == 'example_mode':
        self.schedule_mode = "sample_mode"

    # 
    self.schedule_dict(mode_name=self.schedule_mode)
\`\`\`



