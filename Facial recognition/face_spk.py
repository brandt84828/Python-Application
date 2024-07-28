import face_spk_module as m   # 匯入有語音功能的自訂模組

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'  # api
key = 'key'                                                     # 你的金鑰
gid = 'gp01'                                                         # 群組 Id
pid = 'id'                         # 成員 Id

m.face_init(base, key)  # 初始化金鑰
m.face_use(gid, pid)    # 指定要操作的 gid 和 pid
m.face_shot('who')      # 呼叫拍照函式來拍照並上傳到Azuse新增成員人臉影像
