<template>

    <div class = 'player-detail'>

        <PlayerHeader
        v-if="player"
        :player="player?.player"
    />

        <section class = "elo-section">

            <EloChart
            v-if="player"
            :player="player?.player.player"
            :elo-history="player?.elo"
            />

        </section>
        
        <section class = "stats-grid">
            
            <div class = 'card'>
                <h3>
                Lieblingskonzerne: Spiele (Siege)
                </h3>
            <FactionChart
                v-if="player"
                :player = "player?.player.player"
                :factions="player?.factions"
            />
            </div>


            <div class = 'card'>
                <h3>
                    Head-to-Head Spielervergleich:
                </h3>
            <H2HMatrix
                v-if="player"
                :current-player="player?.player.player"
                :h2h="player?.h2h"
            />
            </div>

        </section>
    </div>

</template>


<script setup lang="ts">

import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import EloChart from "@/components/EloChart.vue"
import FactionChart from "@/components/FactionChart.vue"
import H2HMatrix from "@/components/H2HMatrix.vue"
import PlayerHeader from "@/components/PlayerHeader.vue"




const route = useRoute()


const player = ref<any>(null)


onMounted(async () => {

    const name = route.params.name


    const response = await fetch(
        `http://127.0.0.1:8000/players/${name}`
    )


    player.value = await response.json()

})


</script>

<style scoped>

.player-detail {

    width: 100%;

    display: flex;

    flex-direction: column;

    gap: 2rem;

}

.elo-section {

    width: 100%;

}


.stats-grid {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 2rem;

}


.card {

    /* background: white; */

    border-radius: 12px;

    padding: 1.5rem;

    box-shadow:
        0 2px 8px rgba(0,0,0,0.08);


}
</style>