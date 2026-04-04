import Home from '../pages/home/index.vue'
import LivePage from '../pages/home/LivePage.vue'
import type { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: Home },
  { path: '/home/live', component: LivePage },
  {
    path: '/video-detail',
    name: 'video-detail',
    component: () => import('@/pages/other/VideoDetail.vue')
  }
]

export default routes
