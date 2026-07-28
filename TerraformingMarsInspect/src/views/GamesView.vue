<script setup lang="ts">

import GameCard from '@/components/GameCard.vue'
import { games } from '@/data/games'

import { ref, onMounted } from 'vue'

const showGames = ref(false)

onMounted(() => {
  showGames.value = true
})

</script>

<template>
  <h2>Rundenübersicht</h2>
  <TransitionGroup name="games" tag="div" class="game-grid">
  
    <GameCard v-for="(game, index) in (showGames ? games : [])"
    :style="{ '--delay': `${index * 120}ms` }"
    :key="game.date"
    :game="game"/>
  
  </TransitionGroup>

</template>


<style>

.game-grid {

    width: 100%;
  
    display: flex;

    flex-direction: column;

    /* grid-template-columns: repeat(1, 100%); */

    gap: 1.5rem;

    margin-top: 1.5rem;

}

.games-enter-active {
    transition: all .35s ease;

    transition-delay: var(--delay);
}

.games-enter-from {
    opacity: 0;
    transform: scale(.95);
}

.games-enter-to {
    opacity: 1;
    transform: scale(1);
}

</style>