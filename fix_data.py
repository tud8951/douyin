import json

# 创建兔宝大人用户
rabbit_user = {
    "avatar_168x168": {
        "height": 720,
        "uri": "aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24",
        "url_list": [
            "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24~c5_168x168.jpeg?from=2956013662"
        ],
        "width": 720
    },
    "avatar_300x300": {
        "height": 720,
        "uri": "aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24",
        "url_list": [
            "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24~c5_300x300.jpeg?from=295601361662"
        ],
        "width": 720
    },
    "aweme_count": 1,
    "birthday_hide_level": 0,
    "can_show_group_card": 1,
    "city": "上海",
    "commerce_info": {
        "challenge_list": None,
        "head_image_list": None,
        "offline_info_list": [],
        "smart_phone_list": None,
        "task_list": None
    },
    "commerce_user_info": {
        "ad_revenue_rits": None,
        "has_ads_entry": True,
        "show_star_atlas_cooperation": True,
        "star_atlas": 1
    },
    "commerce_user_level": 0,
    "country": "中国",
    "cover_colour": "#03373EE5",
    "cover_url": [
        {
            "uri": "douyin-user-image-file/8777a333ff12e0ff1e24c840f426969d",
            "url_list": ["LnRxh1zcLlxDyi2DyuEet.png"]
        }
    ],
    "district": null,
    "favoriting_count": 0,
    "follow_status": 0,
    "follower_count": 5000000,
    "follower_request_status": 0,
    "follower_status": 0,
    "following_count": 100,
    "forward_count": 1,
    "gender": 2,
    "ip_location": "IP属地：北京",
    "max_follower_count": 5000000,
    "mplatform_followers_count": 5000000,
    "nickname": "兔宝大人",
    "province": "上海",
    "public_collects_count": 0,
    "share_info": {
        "bool_persist": 1,
        "share_desc": "长按复制此条消息，打开抖音搜索，查看TA的更多作品。",
        "share_image_url": {
            "uri": "tos-cn-p-0015/ec2c039ed41549489392dcfd519549c6_1698671189",
            "url_list": ["1eo2BqA_8uoyTC8b7Wz6B.png"]
        },
        "share_qrcode_url": {
            "uri": "2e0900002e399192ee6d7",
            "url_list": [
                "https://p3.douyinpic.com/obj/2e0900002e399192ee6d7",
                "https://p26.douyinpic.com/obj/2e0900002e399192ee6d7",
                "https://p6.douyinpic.com/obj/2e0900002e399192ee6d7"
            ]
        },
        "share_title": "快来加入抖音，让你发现最有趣的我！",
        "share_url": "www.iesdouyin.com/share/user/MS4wLjABAAAAonK7FndgFYn4mKBQwHc34iEiCCwvBI3tXNqGXqd18qFM9p_ZSxC1y9Gyv1e0XuG_?from_aid=6383&u_code=13kgm680k&did=MS4wLjABAAAAiOgYyZm8XbWZMr5o3OvhR-TEOuNygb_hQOwkie-VXJpDYaR4vZfpiIGBfAWKCFHB&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&sec_uid=MS4wLjABAAAAonK7FndgFYn4mKBQwHc34iEiCCwvBI3tXNqGXqd18qFM9p_ZSxC1y9Gyv1e0XuG_&from_ssr=1&from_aid=6383",
        "share_weibo_desc": "长按复制此条，打开抖音搜索，查看TA的更多作品。"
    },
    "short_id": "8357999",
    "signature": "兔宝大人的个人空间，欢迎关注！",
    "total_favorited": 9999999,
    "uid": "1774630103015",
    "unique_id": "tubaoda_1774630103015",
    "user_age": 18,
    "white_cover_url": [
        {
            "uri": "douyin-user-image-file/8777a333ff12e0ff1e24c840f426969d",
            "url_list": ["wqKmvIFifx1re2KR2VAXF.png"]
        }
    ]
}

# 保存用户数据
with open(r'd:\code\douyin\public\data\users.json', 'w', encoding='utf-8') as f:
    json.dump([rabbit_user], f, ensure_ascii=False, indent=2)

# 更新视频数据，将所有视频的作者改为兔宝大人
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

rabbit_avatar = "https://p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_99d3a4923c94e1e27b16209743eaec24~c5_168x168.jpeg?from=2956013662"

updated_count = 0
for video in videos:
    video['author'] = {
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
    updated_count += 1

# 保存更新后的视频数据
with open(r'd:\code\douyin\src\assets\data\posts6.json', 'w', encoding='utf-8') as f:
    json.dump(videos, f, ensure_ascii=False, indent=2)

print(f'✅ 用户重新创建完成')
print(f'   保留用户: 兔宝大人 (UID: 1774630103015)')
print(f'✅ 视频作者更新完成: {updated_count}个视频')
print(f'   所有视频现在都属于兔宝大人')