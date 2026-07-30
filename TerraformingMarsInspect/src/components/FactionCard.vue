<template>

<div 
    class="faction-card"
    
>

    <img 
        class="faction-logo"
        :src="getFactionIcon(faction.faction)"
        :alt="faction.faction"
    >


    <h3>
        {{ factionName }}
    </h3>


    <div class="games">
        Spiele: {{ faction.games }} | Siege: {{ faction.wins }}
    </div>

</div>

</template>


<script setup lang="ts">

import { computed } from "vue"
import { useRouter } from "vue-router"

import { getFactionIcon, getFactionName } from "@/data/factions"


const props = defineProps<{
    faction:{
        faction:string,
        games:number
    }
}>()


const router = useRouter()


const factionName = computed(() =>
    getFactionName(props.faction.faction)
)


function openDetail(){

    router.push(
        `/factions/${props.faction.faction}`
    )

}

</script>

<style>

.faction-card {

    width: 220px;
    height: 220px;

    background:#20262E;

    border-radius:16px;

    padding:1.5rem;

    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;

    color:white;

    cursor:pointer;

    transition:.2s;

}


.faction-card:hover {

    transform:translateY(-5px);

    box-shadow:0 8px 20px rgba(0,0,0,.3);

}


.faction-logo {

    width:100px;
    height:100px;

    object-fit:contain;

    margin-bottom:0.5rem;

}


.games {

    color:#bbb;

    margin-top:.5rem;

}

</style>