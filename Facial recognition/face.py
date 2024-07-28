import face_module as m   # 匯入自訂模組

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'  # api
key = 'key'                                                    
gid = 'gp01'                                                       
pid = 'id'                         

m.face_init(base, key)  # 初始化金鑰
m.face_use(gid, pid)    # 指定要操作的 gid 和 pid
m.face_shot('who')      # 呼叫拍照函式來拍照並上傳到Azuse新增成員人臉影像
