from SuperPlayer import SuperPlayer 
import datetime

class DebugPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None

    def return_my_name(self):
        return "DebugPlayer"

    def main(self):
        """
        DebugPlayerは、ballObjectのメンバ変数をすべて出力します。
        デバッグしたい内容は、ballObjectのメンバ変数に乗せて、
        DebugPlayerをスケジューリングすればよいということです。
        """

        # SuperPlayerのメンバ変数。
        # このmain実行する直前に
        # SuperPlayerでself.one_time_world_instance に
        # 最新のworldを代入してあります。
        world = self.one_time_world_instance # SuperPlayerに保持したworldの反映
        print(f"\n==== {datetime.datetime.now()} ==============================")
        for key, value in world.ball.__dict__.items():
            print(f'{key}: {value}')

        return "Completed"
