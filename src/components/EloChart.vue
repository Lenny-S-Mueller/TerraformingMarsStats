<template>
    <div class="elo-chart">
        <Line :data="chartData" :options="chartOptions"/>
    </div>
</template>

<script setup lang="ts">

import { computed } from "vue"
import { Line } from "vue-chartjs"

import { getPlayerColor } from "@/data/playerColor"



import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend
} from "chart.js"

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip,
    Legend
)

const props = defineProps<{
    player : string,
    eloHistory: {
        date: number,
        elo: number
    }[]
}>()


const playerColor = getPlayerColor(props.player)

const chartData = computed(() => ({
    labels: props.eloHistory.map(e => e.date),

    datasets: [
        {
            label: "ELO",

            data: props.eloHistory.map(e => e.elo),

            borderColor: playerColor,
            backgroundColor: playerColor,


            pointBackgroundColor: playerColor,
            pointBorderColor: "#ffffff",
            pointHoverBackgroundColor: playerColor,  
            

            pointRadius: 5,
            pointHoverRadius: 8,

            tension: 0.3
        }
    ]
}))

const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,

    scales: {
        x: {
            grid: {
                color: "#dddddd"
            }
        },

        y: {
            grid: {
                color: "#dddddd"
            }
        }
    },

    plugins: {

    datalabels: {
        display: false
    }

}
}

</script>

<style scoped>

.elo-chart {
    width: 100%;
    height: 350px;
}

</style>