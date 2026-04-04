import json

# 读取视频数据
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

# 新的封面URL
new_cover_url = "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24~c5_168x168.jpeg?from=2956013662"

# 更新所有视频的封面
updated_count = 0
for video in videos:
    if "video" in video and "cover" in video["video"]:
        video["video"]["cover"]["url_list"] = [new_cover_url]
        updated_count += 1
    if "cover" in video:
        video["cover"]["url_list"] = [new_cover_url]
        updated_count += 1

# 保存更新后的数据
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'w', encoding='utf-8') as f:
    json.dump(videos, f, ensure_ascii=False, indent=2)

print(f'✅ 已更新 {updated_count} 个视频的封面')
print(f'新封面URL: {new_cover_url}')
print(f'当前视频总数: {len(videos)}')