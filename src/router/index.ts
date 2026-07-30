import { createRouter, createWebHistory } from "vue-router"

import DashboardView from "@/views/DashboardView.vue"
import GamesView from "@/views/GamesView.vue"
import PlayersView from "@/views/PlayersView.vue"
import FactionsView from "@/views/FactionsView.vue"
import AppLayout from "@/layouts/AppLayout.vue"
import PlayerDetailView from "@/views/PlayerDetailView.vue"

const router = createRouter({
  history : createWebHistory(import.meta.env.BASE_URL),

  routes: [
    {
      path: '/',
      component: AppLayout,

      children: [

        {
          path: '/dashboard',
          name: 'dashboard',
          component: DashboardView,
        },
        {
          path: '/games',
          name: 'games',
          component: GamesView,
        },
        {
          path: '/players',
          name: 'players',
          component: PlayersView,
        },
        {
          path: '/factions',
          name: 'factions',
          component: FactionsView,
        
        },
        {
          path: 'players/:name',
          component: PlayerDetailView
        }
      ]
    },
    
  ],
})

export default router