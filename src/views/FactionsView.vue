<template>

<div>

<h2>Konzerne</h2>

<TransitionGroup 
name="faction"
tag="div"
class="faction-grid">

    <FactionCard
        v-for="(faction, index) in (showFaction ? factions : [])"
        :key="faction.faction"
        :faction="faction"
        :style="{ '--delay': `${index * 20}ms` }"
    />

</TransitionGroup>

</div>

</template>


<script setup lang="ts">

import { ref, onMounted } from "vue"
import FactionCard from "@/components/FactionCard.vue"


const factions = ref([])

const showFaction = ref(false)


onMounted(async () => {

    const res = await fetch("/data/factions.json")

    factions.value = await res.json()

    showFaction.value = true

})

</script>

<style>

.faction-grid {

    display: grid;

    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));

    gap: 2rem;

    padding: 1rem;

}

.faction-enter-active {
    transition: all .35s ease;

    transition-delay: var(--delay);
}

.faction-enter-from {
    opacity: 0;
    transform: scale(.95);
}

.faction-enter-to {
    opacity: 1;
    transform: scale(1);
}

</style>