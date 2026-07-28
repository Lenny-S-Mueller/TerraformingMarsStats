<template>

<div 
    class="player-card" :style="{ '--player-color': getPlayerColor(props.player.player)}"
    @click="openPlayer"
>

    <h2 class = "header">
        {{ player.player }}
    </h2>


    <div class="stats">

        <p>
            Spiele:
            {{ player.games }}
        </p>

        <p>
            Siege:
            {{ player.wins }}
        </p>

        <p>
            Winrate:
            {{ player.ratio  * 100}}%
        </p>

    </div>


    <p>
        ELO-Rating:
        {{ player.current_elo }}
    </p>


</div>

</template>


<script setup lang="ts">

import { computed } from 'vue'
import { useRouter } from 'vue-router'

import { getPlayerColor } from "@/data/playerColor"


// const props = defineProps<{
//     player: Player
// }>()

const props = defineProps<{
    player: any
}>()

const router = useRouter()


const winrate = computed(() => {
    return Math.round(
        props.player.wins /
        props.player.games *
        100
    )
})


function openPlayer() {

    router.push(
        `/players/${props.player.player}`
    )

}

const colors = [
    '#D4C685',
    '#F7EF81',
    '#CFE795',
    '#A7D3A6',
    '#ADD2C2',
    '#B4D6C8',
    '#BBDACD'
]


</script>

<style>
.player-card {

    background-color: var(--player-color);

    color: black;

    border-radius: 12px;

    padding: 1.5rem;

    cursor: pointer;

    transition: 
        transform .2s,
        box-shadow .2s;

}


.player-card:hover {

    transform: translateY(-4px);

    box-shadow:
        0 8px 20px rgba(0,0,0,.15);

}
.header {
    text-align: center;
}
</style>