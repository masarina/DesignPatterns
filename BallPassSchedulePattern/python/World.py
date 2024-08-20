from BallObject import BallObject
from FirstPlayer import FirstPlayer
from FinalPlayer import FinalPlayer
from DebugPlayer import DebugPlayer

class World:
    def __init__(self):

        # ballとplayerの作成
        self.ball = BallObject()
        self.firstPlayer = FirstPlayer()
        self.finalPlayer = FinalPlayer()
        self.debugPlayer = DebugPlayer()

    def get_before_player_status(self, world=None, my_name=None):

        mini_schedule_status = world.ball.now_schedule_status[world.ball.index_of_schedule]
        before_player_status = None

        # もし、ミニスケの先頭だった場合（でかつ、FirstPlayerを除く。）
        if (world.ball.index_of_schedule_of_schedule == 0) and (my_name != "FirstPlayer"):
            # ひとつ前ミニスケの一番後ろのplayerのステータスを取得。
            before_mini_schedule_status = world.ball.now_schedule_status[world.ball.index_of_schedule - 1]
            before_player_status = before_mini_schedule_status[-1]

        # もし、FirstPlayerだった場合
        elif my_name == "FirstPlayer":
            before_player_status = "Completed"  # 一つ前のプレイヤーはいないから強制

        # もし、ミニスケの先頭でもなく、FirstPlayerでもなかった場合
        else:
            # 普通にひとつ前のplayerのステータスを取得。
            before_player_status = mini_schedule_status[world.ball.index_of_schedule_of_schedule - 1]

        return before_player_status

    def update_now_schedule_status(self, world=None, player_status=None):
        axis_0 = world.ball.index_of_schedule
        axis_1 = world.ball.index_of_schedule_of_schedule
        world.ball.now_schedule_status[axis_0][axis_1] = player_status

    def go_to_next_index_of_schedule_of_schedule(self, world=None):
        """
        ミニスケジュール内のインデックスを一つ進める。
        """
        axis_0 = world.ball.index_of_schedule
        axis_1 = world.ball.index_of_schedule_of_schedule

        # 仮に一つ進めて、..

        if axis_1 + 1 >= len(world.ball.now_schedule[axis_0]):
            world.ball.index_of_schedule_of_schedule = 0
            return "over!"
        else:
            world.ball.index_of_schedule_of_schedule += 1
            return True



    def go_to_next_index_of_schedule(self, world=None):
        """
        index_of_schedule を 1 進めるメソッド
        次のミニスケジュールが存在しない場合は index_of_schedule = 0 にし、"over"を返す
        """
        mini_schedule_is_all_completed = True
        axis_0 = world.ball.index_of_schedule
        now_mini_schedule_status = world.ball.now_schedule_status[axis_0]

        # 今のミニスケジュールのすべてのステータスを確認する。
        for status in now_mini_schedule_status:
            if status != "Completed":
                mini_schedule_is_all_completed = False
                break


        # 算出したミニスケジュールの状態を参考に、分岐。

        if mini_schedule_is_all_completed: # ミニスケは全compだった
            world.ball.index_of_schedule += 1 # だから次のミニスケにした。
        
            # でもすべてのミニスケをこれで完了だった場合
            if world.ball.index_of_schedule >= len(world.ball.now_schedule):
                # ゼロにする。
                world.ball.index_of_schedule = 0
                world.ball.index_of_schedule_of_schedule = 0
                world.ball.reset_schedule_status()

                return "range over!"

        if mini_schedule_is_all_completed == False:
            # ミニスケジュールはまだ完了してないので、次のスケジュールには遷移しない。
            return "Not this mini schedule is all completed yet"

    def go_to_next_schedule_mode(self, world=None):
        world.ball.schedule_mode_settings()


    def doing_now_players_main_AND_update_now_players_status(
            self, 
            world=None, 
            before_player_status=None, 
            now_players_main_method=None,
            ):
        result = 0

        # 一つ前のプレイヤーのミッションが完了していた場合
        if before_player_status == "Completed":

            # すでに自身のmainが実行されていた場合はpassをする。（自身のmainが非同期関数の場合あり得ることです。）
            if world.ball.now_schedule_status[world.ball.index_of_schedule][world.ball.index_of_schedule_of_schedule] == "Not completed yet":
                pass

            else:
                result = now_players_main_method()

        if result == 0:
            pass

        elif result == "Completed":
            world.update_now_schedule_status(world=world, player_status="Completed")

        else:
            # メインを実行したけれど、メインは完了していない場合。（つまり、main内に非同期関数を含めてもOKです。）
            world.update_now_schedule_status(world=world, player_status="Not completed yet")


        result_of_main_method = result
        return result_of_main_method

    def doing_next_players_catch_ball_method_by_player_name(self, player_name=None, world=None):
        
        if player_name == "FirstPlayer":
            self.firstPlayer.catch_ball(world=world)

        elif player_name == "DebugPlayer":
            self.debugPlayer.catch_ball(world=world)

        elif player_name == "FinalPlayer":
            self.finalPlayer.catch_ball(world=world)








