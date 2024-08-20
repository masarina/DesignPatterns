import time 
import copy

class SuperPlayer:
    def __init__(self):
        self.one_time_world_instance = None
        self.my_name = None

    def main(self):
        e = "Main をオーバライドしていないプレイヤーがいます！"
        print(e)
        return e

    def return_myname(self):
        e = "return_myname をオーバライドしていないプレイヤーがいます！"
        print(e)
        return e


    def catch_ball(self, world=None):
        # 変数の準備
        world.ball.next_player_name = None
 
        # catch_ballが渡されたplayerの名前を代入
        self.my_name = self.return_my_name()


        time.sleep(1)
        # 一つ前のプレイヤーのステータスを参考にして
        #  self.Main の実行の有無を決めて、self.Main の処理。
        # プレイヤーself自身のステータスも更新する。
        self.one_time_world_instance = world

        world.ball.now_catch_balling_player = f"{self.my_name}"  # ここでself.my_nameを確認


        """test"""
        # print("\n=================================================")
        # print("\n==== キャッチボール開始 ====")
        # for key,value in world.ball.__dict__.items():
        #     print(f"{key}:{value}")
        


        # ひとつ前のプレイヤーのステータスを取得
        before_player_status = world.get_before_player_status(world=world, my_name=self.my_name)

        _ = world.doing_now_players_main_AND_update_now_players_status(
            world=world,
            before_player_status=before_player_status,
            now_players_main_method=self.main,
        )

        # of_schedule_of_schedule を 一つ進める
        result = world.go_to_next_index_of_schedule_of_schedule(world=world)
        

        # ミニスケジュール内のplayerがすべて"Completed"だった場合、
        # 次のミニスケジュールに遷移
        if result == "over!":
            result = world.go_to_next_index_of_schedule(world=world)



        # 今回実行しているスケジュールモードの全ステータスが
        # "Completed"の場合、次のschedule_modeに遷移、
        # 次のモードのスケジュールとステータスの準備
        # ↪　now_cheduleの更新、now_chedule_statusの初期化
        if result == "range over!":
            world.go_to_next_schedule_mode(world=world)
            world.ball.reset_schedule_status()



        # 次のプレイヤーのcatch_ballを実行する
        # 一旦単純につぎのcatch_ballを実行してみます。
        # この時点ですでに、
        # world.ball.axis_0
        # world.ball.axis_1
        # world.ball.schedule_mode
        # これらは更新されているため、インデックスはこのまま使用すれば
        # 次のplayerを選択することになるはずです。
        axis_0 = world.ball.index_of_schedule
        axis_1 = world.ball.index_of_schedule_of_schedule

        # 次のプレイヤーの名前を取得。
        world.ball.next_player_name = world.ball.now_schedule[axis_0][axis_1][0]



        """test"""
        # print("\n==== このパラメータで次のプレイヤーへ。 ====")
        # for key,value in world.ball.__dict__.items():
        #     print(f"{key}:{value}")



        world.doing_next_players_catch_ball_method_by_player_name(
            player_name=world.ball.next_player_name, 
            world=world,
        ) # その名前のインスタンスのcatch_ballを実行。


        """test"""
        # print("\n==== キャッチボール完了 ====")
        # for key,value in world.ball.__dict__.items():
        #     print(f"{key}:{value}")





















