<script setup lang="ts">
import { ref, onMounted } from 'vue'

import PlayerCard from '@/components/PlayerCard.vue'

import type { Player } from '@/data/players'
// import { players } from '@/data/players'


const players = ref([])

const showPlayers = ref(false)

onMounted(async () => {
    const response = await fetch("http://localhost:8000/players")
    players.value = await response.json()

    showPlayers.value = true

    console.log(players.value)
})



// onMounted(() => {
//   showPlayers.value = true
// })
</script>

<template>
  <h2>Spieler</h2>
  <TransitionGroup
    name="player"
    tag="div"
    class="player-grid"
  >
    <PlayerCard
      v-for="(player, index) in (showPlayers ? players : [])"
      :key="player.player"
      :player="player"
      :style="{ '--delay': `${index * 50}ms` }"
    />
  </TransitionGroup>
</template>

<style>
.player-grid {

    display: grid;

    grid-template-columns: repeat(5, 280px);

    gap: 1.5rem;

    margin-top: 1.5rem;


}

.player-enter-active {
    transition: all .35s ease;

    transition-delay: var(--delay);
}

.player-enter-from {
    opacity: 0;
    transform: scale(.95);
}

.player-enter-to {
    opacity: 1;
    transform: scale(1);
}
</style>