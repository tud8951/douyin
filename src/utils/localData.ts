import posts6 from '@/assets/data/posts6.json'

// 处理视频数据
const processVideos = (videos: any[]) => {
  return videos.map((v) => ({
    ...v,
    type: 'recommend-video',
    // 确保必要字段存在
    statistics: v.statistics || {
      digg_count: 0,
      comment_count: 0,
      collect_count: 0,
      share_count: 0
    },
    author: v.author || { nickname: '未知用户', avatar_168x168: { url_list: [] } }
  }))
}

// 获取推荐视频
export async function recommendedVideo(params?: any) {
  const { start = 0, pageSize = 10 } = params || {}
  const allVideos = processVideos(posts6)
  const list = allVideos.slice(Number(start), Number(start) + Number(pageSize))

  return {
    success: true,
    data: {
      total: allVideos.length,
      list: list
    },
    code: 200,
    msg: ''
  }
}

// 获取长视频推荐
export async function recommendedLongVideo(params?: any) {
  const { start = 0, pageSize = 10 } = params || {}
  const allVideos = processVideos(posts6)
  let list = allVideos.slice(Number(start), Number(start) + Number(pageSize))

  // 如果数据不够，复制一些来展示
  if (list.length > 0 && list.length < 5) {
    while (list.length < 10) {
      list = list.concat(
        allVideos.map((v: any) => ({ ...v, aweme_id: v.aweme_id + Math.random() }))
      )
    }
  }

  return {
    success: true,
    data: {
      total: Math.max(allVideos.length, list.length),
      list: list
    },
    code: 200,
    msg: ''
  }
}

// 获取我的视频
export async function myVideo(params?: any) {
  const { pageNo = 0, pageSize = 10 } = params || {}
  const allVideos = processVideos(posts6)
  const start = pageNo * pageSize
  const list = allVideos.slice(start, start + pageSize)

  return {
    success: true,
    data: {
      pageNo: pageNo,
      total: allVideos.length,
      list: list
    },
    code: 200,
    msg: ''
  }
}

// 获取私密视频
export async function privateVideo(params?: any) {
  return {
    success: true,
    data: {
      total: 0,
      list: []
    },
    code: 200,
    msg: ''
  }
}

// 获取点赞视频
export async function likeVideo(params?: any) {
  return {
    success: true,
    data: {
      total: 0,
      list: []
    },
    code: 200,
    msg: ''
  }
}

// 获取视频评论
export async function videoComments(params?: any) {
  const id = params?.id
  const allVideos = processVideos(posts6)
  const video = allVideos.find((v: any) => String(v.aweme_id) === String(id))

  if (video && video.comments) {
    const mappedComments = video.comments.map((c: any) => ({
      ...c,
      nickname: c.user?.nickname || c.nickname || '匿名用户',
      avatar: c.user?.avatar_thumb?.url_list?.[0] || c.avatar || '',
      content: c.text || c.content || '',
      create_time: c.create_time || Date.now() / 1000,
      digg_count: c.digg_count || 0
    }))
    return { success: true, data: mappedComments, code: 200 }
  }

  return { success: true, data: [], code: 200 }
}

// 获取用户视频列表
export async function userVideoList(params?: any) {
  const id = params?.id
  const allVideos = processVideos(posts6)
  const list = allVideos.filter((v: any) => {
    return String(v.author?.uid) === String(id) || String(v.author_user_id) === String(id)
  })

  if (list.length > 0) {
    return { success: true, data: list, code: 200 }
  }

  // 如果没有找到，返回所有视频
  return { success: true, data: allVideos, code: 200 }
}

// 获取用户收藏
export async function userCollect(params?: any) {
  return {
    success: true,
    data: {
      video: {
        total: 0,
        list: []
      },
      music: {
        total: 0,
        list: []
      }
    },
    code: 200,
    msg: ''
  }
}

// 获取推荐帖子
export async function recommendedPost(params?: any) {
  const { pageNo = 0, pageSize = 10 } = params || {}
  const allVideos = processVideos(posts6)

  // 将视频数据转换为经验页面所需的格式
  const experiencePosts = allVideos.map((v: any) => ({
    id: v.aweme_id,
    type: 2,
    note_card: {
      display_title: v.desc || '视频描述',
      cover: {
        url_default: v.video.cover.url_list[0]
      },
      user: {
        nickname: v.author.nickname,
        avatar: v.author.avatar_168x168.url_list[0]
      },
      interact_info: {
        liked_count: v.statistics.digg_count
      }
    }
  }))

  const start = pageNo * pageSize
  const list = experiencePosts.slice(start, start + pageSize)

  return {
    success: true,
    data: {
      pageNo: pageNo,
      total: experiencePosts.length,
      list: list
    },
    code: 200,
    msg: ''
  }
}
