from SuperPlayer import SuperPlayer 
import datetime

class ExamplePlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None

    def return_my_name(self):
        return "ExamplePlayer"

    def main(self):
        """
        testですね。いぐざんぷるです。
        """
        # SuperPlayerのメンバ変数。
        # このmain実行する直前に
        # SuperPlayerでself.one_time_world_instance に
        # 最新のworldを代入してあります。
        print("return_my_nameが実行されました。")

        return "Completed"
