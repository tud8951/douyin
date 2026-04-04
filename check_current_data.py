import json

# 读取用户数据
with open(r'd:\code\douyin\public\data\users.json', 'r', encoding='utf-8-sig') as f:
    users = json.load(f)

# 读取视频数据
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

print(f'当前用户数: {len(users)}')
print(f'当前视频数: {len(videos)}')

# 显示当前用户列表
print('\n当前用户列表:')
for u in users:
    print(f'  - {u.get("nickname", "未知")} (UID: {u.get("uid", "无")})')

# 显示当前视频列表
print('\n当前视频列表:')
for v in videos:
    print(f'  - {v.get("desc", "无描述")} (ID: {v.get("aweme_id", "无")}, 作者: {v.get("author", {}).get("nickname", "未知")})')