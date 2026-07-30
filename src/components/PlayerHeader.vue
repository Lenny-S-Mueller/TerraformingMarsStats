<template>

<div class="player-header">


    <div class="player-name"
    :style="{
    borderTopColor:getPlayerColor(player.player)
}"
>

        {{ player.player }}

    </div>



    <div class="stat">

        <span class="label">
            ELO
        </span>

        <strong>
            {{ player.current_elo }}
        </strong>

        <small>
            #{{ player.elo_rank }}
        </small>

    </div>



    <div class="stat">

        <span class="label">
            Spiele
        </span>

        <strong>
            {{ player.games }}
        </strong>

        <small>
            #{{ player.games_rank }}
        </small>

    </div>



    <div class="stat">

        <span class="label">
            Siege
        </span>

        <strong>
            {{ player.wins }}
        </strong>

        <small>
            #{{ player.wins_rank }}
        </small>

    </div>



    <div class="stat">

        <span class="label">
            Siegquote
        </span>

        <strong>
            {{ player.ratio * 100}}%
        </strong>

        <small>
            #{{ player.win_rate_rank }}
        </small>

    </div>

    <div class="stat">

        <span class="label">
            Mean-Score
        </span>

        <strong>
            {{ (player.avg_performance * 100).toFixed(1)}}%
        </strong>

        <small>
            #{{ player.perf_rank }}
        </small>

    </div>

</div>


</template>


<script setup lang="ts">

import { getPlayerColor } from "@/data/playerColor"

defineProps({

    player:{
        type:Object,
        required:true
    }

})

</script>


<style scoped>


.player-header {

    width:100%;

    /* background:white; */

    border-radius:16px;

    padding:1.5rem 2rem;

    display:grid;

    grid-template-columns:
        2fr repeat(5,1fr);


    align-items:center;


    box-shadow:
        0 4px 15px rgba(0,0,0,0.08);

}



.player-name {

    font-size:4rem;

    font-weight:700;

    border-top: 6px solid;
}



.stat {

    display:flex;

    flex-direction:column;

    align-items:center;

}



.label {

    font-size:1rem;

    color:#777;

    text-transform:uppercase;

}



.stat strong {

    font-size:2rem;

}



.stat small {

    color:#888;

}



@media(max-width:900px){


.player-header{

    grid-template-columns:1fr 1fr;

    gap:1rem;

}


.player-name{

    grid-column:1/-1;

}


}


</style>