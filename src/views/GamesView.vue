<script setup lang="ts">

import { ref, computed, onMounted } from "vue"
import GameCard from "@/components/GameCard.vue"


const rows = ref<any[]>([])

const showGames = ref(false)


onMounted(async () => {

    const res = await fetch("/data/games.json")

    rows.value = await res.json()

    showGames.value = true

})



const games = computed(() => {

    const grouped: Record<number, any> = {}

    rows.value.forEach(row => {

        if (!grouped[row.game_id]) {

            grouped[row.game_id] = {
                game_id: row.game_id,
                date: row.date,
                players: []
            }

        }


        grouped[row.game_id].players.push({

            player: row.player,
            faction: row.faction,

            tf_rating: row.tf_rating,
            awards: row.awards,
            milestones: row.milestones,

            greenery: row.greenery,
            city: row.city,

            victory_points: row.victory_points,

            total: row.total,
            money: row.money

        })

    })


    return Object.values(grouped)
            .sort((a, b) => {
                return b.game_id - a.game_id
            })

})

</script>

<template>
<div>

    <TransitionGroup
    name="game"
    tag="div"
    class="games-container"
  >
    <GameCard
      v-for="(game, index) in (showGames ? games : [])"
      :key="game.game_id"
      :game="game"
      :style="{ '--delay': `${index * 50}ms` }"
    />
  </TransitionGroup>
</div>

</template>





<style scoped>

.games-container {

    width:100%;

    display:flex;

    flex-direction:column;

    gap:1.2rem;

    padding:2rem;

}

.game-enter-active {
    transition: all .35s ease;

    transition-delay: var(--delay);
}

.game-enter-from {
    opacity: 0;
    transform: scale(.95);
}

.game-enter-to {
    opacity: 1;
    transform: scale(1);
}


</style>