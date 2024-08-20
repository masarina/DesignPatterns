import copy


class BallObject:
    """
    このクラスはWorldクラスでインスタンス化されます。
    """
    def __init__(self):
        """
        デザインパターン用
        """
        # 変数の用意
        self.now_schedule = None
        self.now_schedule_status = None
        self.schedule_mode = None  # 初期スケジュールモード
        self.index_of_schedule = 0
        self.index_of_schedule_of_schedule = 0

        """
        本プログラム用
        """
        # 処理
        self.schedule_mode = "sample_mode" # モードを選択。
        self.schedule_dict(mode_name=self.schedule_mode) # スケジュールをセット。
        self.reset_schedule_status() # ステータスの初期化。

        """
        デバッグ用（メンバ変数は全てDebugPlayerがデバッグしてくれます。）
        """
        self.now_catch_balling_player = None
        self.next_player_name = None

    def schedule_mode_settings(self):
        if self.schedule_mode == 'sample_mode':
            self.schedule_mode = 'sample2_mode'

        elif self.schedule_mode == 'sample2_mode':
            self.schedule_mode = "example_mode"


        elif self.schedule_mode == 'example_mode':
            self.schedule_mode = "sample_mode"

        # ifで選択されたモードのスケジュールを、メンバ変数に反映させる。
        self.schedule_dict(mode_name=self.schedule_mode)


    def reset_schedule_status(self):
        keep = copy.deepcopy(self.now_schedule)

        self.now_schedule_status = self.now_schedule
        for mini_schedule in range(len(self.now_schedule_status)):
            for players_status in range(len(self.now_schedule_status[mini_schedule])):
                self.now_schedule_status[mini_schedule][players_status] = "None"

        self.now_schedule = keep


    def schedule_dict(self,mode_name=None):
        array_2d = None
        
        if mode_name == "sample_mode":
            array_2d = [
                [['FirstPlayer']],  # 例: 第一ミニスケジュール
                [['DebugPlayer'],['FinalPlayer']]  # 例: 第二ミニスケジュール
            ]

        elif mode_name == "sample2_mode":
            array_2d = [
                [['FirstPlayer'],['DebugPlayer']],  # 例: 第一ミニスケジュール
                [['DebugPlayer'],['DebugPlayer']],  # 例: 第二ミニスケジュール
                [['DebugPlayer'],['DebugPlayer'],['FinalPlayer']]  # 例: 第二ミニスケジュール
            ]


        elif mode_name == "example_mode":
            array_2d = [
                [['FirstPlayer'],["ExamplePlayer"]],  # 例: 第一ミニスケジュール
                [['DebugPlayer']],  # 例: 第二ミニスケジュール
                [['DebugPlayer'],['DebugPlayer'],['DebugPlayer'],['FinalPlayer']]  # 例: 第二ミニスケジュール
            ]

        if array_2d == None:
            print("モードの選択が出来ませんでした。モード名を確認してください。")
            exit()
        
        self.now_schedule = array_2d        







