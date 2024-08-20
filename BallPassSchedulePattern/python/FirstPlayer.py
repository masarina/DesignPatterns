from SuperPlayer import SuperPlayer

class FirstPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す

    def return_my_name(self):
        return "FirstPlayer"

    def main(self):
        return "Completed"
