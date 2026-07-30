<template>

<div class="game-card">


    <!-- Kopfbereich -->

    <div 
        class="summary"
        @click="expanded = !expanded"
    >


        <div class="date">
            <!-- 📅 -->
            {{ game.date }}

        </div>



        <div
            v-for="(player,index) in sortedPlayers"
            :key="player.player"
            class="player-summary"
        >


            <!-- <span class="rank">

                {{ index === 0 ? "🥇" :
                   index === 1 ? "🥈" :
                   index === 2 ? "🥉" :
                   index + 1 }}

            </span> -->



            <span
                class="player-name"
                :style="{
                    color:getPlayerColor(player.player)
                }"
            >

                {{ player.player }}

            </span>



            <img
                class="faction-icon"
                :src="getFactionIcon(player.faction)"
                :alt="player.faction"
            >



            <span class="score">

                {{ player.total }}

            </span>



        </div>



        <font-awesome-icon
            class="arrow"
            :icon="expanded ? 'chevron-up' : 'chevron-down'"
        />


    </div>





    <!-- Detailbereich -->

    <Transition name="expand">

    <div
        v-if="expanded"
        class="details"
    >



        <table>


            <thead>

                <tr>

                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('avatar')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('faction')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('tf_rating')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('awards')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('milestones')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('greenery')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('city')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('victory_points')"
                        >
                    </th>
                    <th>
                        <img
                            class="tf-icon"
                            :src="getIcon('megacredits')"
                        >
                    </th>
                    <th>
                        GESAMT
                    </th>

                </tr>

            </thead>



            <tbody>


                <tr
                    v-for="player in sortedPlayers"
                    :key="player.player"
                >


                    <td
                        :style="{
                            color:getPlayerColor(player.player),
                        }"
                    >

                        {{ player.player }}

                    </td>


                    <td>

                        <img
                            class="table-icon"
                            :src="getFactionIcon(player.faction)"
                        >

                    </td>


                    <td>
                        {{ player.tf_rating }}
                    </td>


                    <td>
                        {{ player.awards }}
                    </td>


                    <td>
                        {{ player.milestones }}
                    </td>


                    <td>
                        {{ player.greenery }}
                    </td>


                    <td>
                        {{ player.city }}
                    </td>


                    <td>
                        {{ player.victory_points }}
                    </td>


                    <td>
                        {{ player.money ?? "-" }}
                    </td>


                    <td class="total">

                        {{ player.total }}

                    </td>


                </tr>


            </tbody>


        </table>


    </div>

    </Transition>


</div>


</template>





<script setup lang="ts">


import { ref, computed } from "vue"

import { getFactionIcon } from "@/data/factions"

import { getPlayerColor } from "@/data/playerColor"

import { getIcon } from "./tmf_icons"



const props = defineProps<{

    game:{
        game_id:number,
        date:string,
        players:any[]
    }

}>()



const expanded = ref(false)



const sortedPlayers = computed(() => {

    return [...props.game.players]
        .sort((a,b)=>b.total-a.total)

})


</script>





<style scoped>


.game-card {

    width:100%;

    background:#2b313b;

    border-radius:16px;

    overflow:hidden;

    box-shadow:0 5px 15px rgba(0,0,0,.2);

}



.summary {


    display:grid;

    grid-template-columns:
        160px
        repeat(5,1fr)
        40px;


    align-items:center;

    gap:1rem;

    padding:1.3rem;

    cursor:pointer;

    transition:.2s;

}



.summary:hover {

    background:#343c49;

}



.date {

    font-weight:bold;

    font-size:1.1rem;

}




.player-summary {

    display:flex;

    align-items:center;

    gap:.5rem;

}



.rank {

    width:25px;

}



.player-name {

    font-weight:bold;

}



.faction-icon {

    width:40px;

    height:40px;

    object-fit:contain;

}



.score {

    font-size:1.2rem;

    font-weight:bold;

}



.arrow {

    justify-self:end;

}




.details {

    padding:1rem 1.5rem 1.5rem;

    border-top:1px solid #555;

}



table {

    width:100%;

    border-collapse:collapse;

}



th {

    text-align:center;

    padding:.8rem;

    color:#aaa;

}



td {

    text-align:center;

    padding:.8rem;

}



tbody tr:hover {

    background:#343c49;

}



.table-icon {

    width:40px;

    /* height:40px; */

}

.tf-icon {

    width: 40px;

}



.total {

    font-weight:bold;

    font-size:1.1rem;

}





.expand-enter-active,
.expand-leave-active {

    transition:.25s ease;

}



.expand-enter-from,
.expand-leave-to {

    opacity:0;

    transform:translateY(-10px);

}



</style>