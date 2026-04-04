# 抖音 Vue 项目自定义指南

本项目已配置为支持完全自定义的视频内容、点赞/评论/收藏统计数据以及自定义评论列表。所有的内容都可以通过修改一个 JSON 文件来完成。

## 🚀 快速开始

1.  **安装依赖**：
    ```bash
    npm install
    ```
2.  **启动项目**：
    ```bash
    npm run dev
    ```
3.  **自定义内容**：
    打开 `src/assets/data/posts6.json` 文件进行编辑。

---

## 📂 核心配置文件：`posts6.json`

所有的视频数据都存储在 [posts6.json](file:///d:/code/douyin/src/assets/data/posts6.json) 中。您可以修改、添加或删除其中的项。

### 1. 视频与描述配置
- `aweme_id`: 视频的唯一 ID（建议为每个视频设置不同的 ID）。
- `desc`: 视频下方的文字描述。
- `video.play_addr.url_list`: 视频的播放地址。
- `video.cover.url_list`: 视频未播放时的封面图地址。

### 2. 统计数据自定义 (`statistics` 字段)
您可以手动设置视频的点赞、评论和收藏显示数量：
- `digg_count`: 点赞数。
- `comment_count`: 评论数显示。
- `collect_count`: 收藏数。
- `share_count`: 分享数。

### 3. 自定义评论内容 (`comments` 字段)
您可以为每个视频指定具体的评论内容：
```json
"comments": [
  {
    "user": {
      "nickname": "粉丝名",
      "avatar_thumb": { "url_list": ["头像链接"] }
    },
    "text": "评论内容",
    "create_time": 1692091704,
    "digg_count": 520
  }
]
```

### 4. 自定义主播主页信息 (`author` 字段)
点击头像进入的主页信息现在也可以通过 `posts6.json` 自定义：
- `nickname`: 主播名称。
- `signature`: 个人简介。
- `follower_count`: 粉丝数。
- `following_count`: 关注数。
- `total_favorited`: 获赞总数。
- `gender`: 性别（1为男，2为女）。
- `ip_location`: IP 属地显示（如 "IP属地：北京"）。
- `cover_url`: 主页背景图链接。

---

## 📹 如何使用自己的视频文件？

### 方案 A：使用远程视频 (推荐)
直接将视频上传到云端或使用现有的网络视频链接，填入 `url_list` 中。

### 方案 B：使用本地视频
1. 将您的视频文件放入项目的 `public` 文件夹中。
2. 在 `posts6.json` 中使用相对根目录的路径（如 `"/my-video.mp4"`）。

---

## 🛠️ 技术细节 (开发者参考)

- **数据同步**：Mock 机制已修改为实时读取 `posts6.json`。
- **主页拦截**：`/user/panel` 接口现在会优先返回 `posts6.json` 中第一个视频的作者信息。
