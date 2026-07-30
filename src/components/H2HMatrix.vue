<template>

    <div class="h2h-wrapper">

        <table class="h2h-table">

            <thead>
                <tr>

                    <th>H2H</th>

                    <th
                        v-for="player in players"
                        :key="player"
                        :class="{
                            highlight:
                                player === currentPlayer
                        }" ,
                        :style="{ '--player-color': getPlayerColor(props.currentPlayer)}"
                    >
                        {{ player }}
                    </th>

                </tr>
            </thead>


            <tbody>

                <tr
                    v-for="row in h2h"
                    :key="row.player"
                >

                    <th
                        :class="{
                            // highlight:
                            //     row.player === currentPlayer
                        }"
                    >
                        {{ row.player }}
                    </th>


                    <td
                        v-for="player in players"
                        :key="player"

                        :class="{
                            highlight:
                                player === currentPlayer,

                            positive:
                                getValue(row, player) > 0,

                            negative:
                                getValue(row, player) < 0,

                            diagonal:
                                row.player === player
                        }",
                        :style="{ '--player-color': getPlayerColor(props.currentPlayer) + '33'}"
                    >

                        <span v-if="row.player !== player">
                            {{ formatValue(getValue(row, player)) }}
                        </span>

                        <span v-else>
                            -
                        </span>

                    </td>

                </tr>

            </tbody>


        </table>

    </div>

</template>



<script setup lang="ts">


import { getPlayerColor } from "@/data/playerColor"


const props = defineProps<{

    currentPlayer: string

    h2h: {
        player: string
        [key: string]: number | string
    }[]

}>()



// Spieler aus den Spaltennamen holen
const players = Object.keys(props.h2h[0])
    .filter(
        key => key !== "player"
    )



function getValue(
    row: any,
    player: string
) {

    return Number(row[player] ?? 0)

}



function formatValue(
    value: number
) {

    if (value > 0)
        return `+${value}`

    return value

}



</script>



<style scoped>


.h2h-wrapper {

    overflow-x: auto;

}



.h2h-table {

    border-collapse: collapse;

    width: 100%;

    font-size: 1.1rem;

}



th,
td {

    padding: 0.6rem;

    text-align: center;

    border: 1px solid #ddd;

}



.highlight {

    background-color: var(--player-color);

    font-size: 1.25rem;

    font-weight: bold;

}



.positive {

    color: green;

}



.negative {

    color: red;

}



.diagonal {

    color: gray;

}



</style>