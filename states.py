from enum import Enum, auto

class BotState(Enum):
    """
    機器人狀態列舉
    """
    IDLE = auto()             # 閒置中
    WAITING_FOR_BITE = auto() # 等待魚兒上鉤
    QTE = auto()              # 進行 QTE (快速反應事件) 控制中
    SUCCESS = auto()          # 釣魚成功
    FAILURE = auto()          # 釣魚失敗
    OUT_OF_BAIT = auto()      # 魚餌不足
    ANDROID_INITIALIZING = auto()  # Android初始化中
