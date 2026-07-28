<template>
    <div class="game-card">
        {{ game.date }}     {{game.player1}}    {{ game.player2 }}     {{ game.player3 }}      {{ game.player4 }}      {{ game.player5 }}
    </div>
</template>

<script setup lang="ts">

import type { Game } from "@/data/games"

const props = defineProps<{
    game: Game
}>()

</script>

<style>

.game-card {

    background-color: grey;

    color: black;

    border-radius: 12px;

    padding: 1.5rem;

    cursor: pointer;

    transition: 
        transform .2s,
        box-shadow .2s;
}

</style>