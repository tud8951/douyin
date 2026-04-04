import json

# 读取视频数据
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

# 找到神探狸狸的视频
video_id = "1774630103015"
found = False

for video in videos:
    if video.get("aweme_id") == video_id:
        # 获取兔宝大人的信息
        rabbit_avatar = "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24~c5_168x168.jpeg?from=2956013662"
        
        # 更新视频作者信息
        video["author"] = {
            "nickname": "兔宝大人",
            "uid": "1774630103015",
            "author_user_id": "1774630103015",
            "avatar_168x168": {
                "url_list": [rabbit_avatar]
            },
            "avatar_300x300": {
                "url_list": [rabbit_avatar]
            },
            "cover_url": [{"url_list": [rabbit_avatar]}],
            "signature": "兔宝大人的个人空间，欢迎关注！",
            "follower_count": 5000000,
            "mplatform_followers_count": 5000000,
            "following_count": 100,
            "total_favorited": 9999999,
            "aweme_count": 1,
            "gender": 2,
            "user_age": 18,
            "ip_location": "IP属地：北京"
        }
        # 更新author_user_id字段
        video["author_user_id"] = "1774630103015"
        
        found = True
        print(f'✅ 已更新视频 {video_id} 的作者为兔宝大人')
        break

if not found:
    print(f'❌ 未找到ID为 {video_id} 的视频')

# 保存更新后的数据
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'w', encoding='utf-8') as f:
    json.dump(videos, f, ensure_ascii=False, indent=2)

print(f'当前视频总数: {len(videos)}')

# 显示所有视频的作者
print('\n当前视频列表:')
for v in videos:
    print(f'  - {v.get("desc", "无描述")} (作者: {v.get("author", {}).get("nickname", "未知")})')