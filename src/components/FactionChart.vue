<template>

<div class="faction-chart">


    <div
    v-for="faction in topFactions"
    :key="faction.faction"
    class="faction-row"
>


    <div class="icon-wrapper">


        <img
            :src="getFactionIcon(faction.faction)"
            class="faction-icon"
        />


        <div class="tooltip">


            <strong>
                {{ faction.faction }}
            </strong>


            <span>
                Spiele:
                {{ faction.times_played }}
            </span>


            <span>
                Siege:
                {{ faction.wins }}
            </span>


            <span>
                Siegquote:
                {{ getWinRate(faction) }}%
            </span>


        </div>


    </div>



    <div class="bar-container">


        <div
            class="bar"
            :style="{
                width:
                (faction.times_played / maxGames * 100)
                + '%',
                '--bar-color': getPlayerColor(props.player)
            }"
        >

            {{ faction.times_played }}
            ({{ faction.wins }})

        </div>


    </div>


</div>


</div>


</template>


<script setup lang="ts">

import { computed } from "vue"

import { Bar } from "vue-chartjs"

import { getPlayerColor } from "@/data/playerColor"

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend
} from "chart.js"

import ChartDataLabels from "chartjs-plugin-datalabels"


ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend,
    ChartDataLabels
)


import aphrodite from "@/assets/icons/aphrodite.png"
import arcadiancommunities from "@/assets/icons/arcadiancommunities.png"
import aridor from "@/assets/icons/aridor.png"
import arklight from "@/assets/icons/arklight.png"
import astrodrill from "@/assets/icons/astrodrill.png"
import beginner from "@/assets/icons/beginner.png"
import celestic from "@/assets/icons/celestic.png"
import cheungshing from "@/assets/icons/cheungshing.png"
import credicor from "@/assets/icons/credicor.png"
import ecoline from "@/assets/icons/ecoline.png"
import helion from "@/assets/icons/helion.png"
import interplanetary from "@/assets/icons/interplanetary.png"
import inventrix from "@/assets/icons/inventrix.png"
import manutech from "@/assets/icons/manutech.png"
import miningguild from "@/assets/icons/miningguild.png"
import morningstarinc from "@/assets/icons/morningstarinc.png"
import pharmacy from "@/assets/icons/pharmacy.png"
import phobolog from "@/assets/icons/phobolog.png"
import pointluna from "@/assets/icons/pointluna.png"
import polyphemos from "@/assets/icons/polyphemos.png"
import poseidon from "@/assets/icons/poseidon.png"
import recyclon from "@/assets/icons/recyclon.png"
import robinson from "@/assets/icons/robinson.png"
import saturnsystems from "@/assets/icons/saturnsystems.png"
import splice from "@/assets/icons/splice.png"
import stormcraft from "@/assets/icons/stormcraft.png"
import teractor from "@/assets/icons/teractor.png"
import tharsisrepublic from "@/assets/icons/tharsisrepublic.png"
import thorgate from "@/assets/icons/thorgate.png"
import unitedmarsinitiative from "@/assets/icons/unitedmarsinitiative.png"
import valleytrust from "@/assets/icons/valleytrust.png"
import viron from "@/assets/icons/viron.png"
import vitor from "@/assets/icons/vitor.png"





const props = defineProps<{
    
    player : string,

    factions: {

        faction: string

        times_played:number

        wins:number

    }[]

}>()


const playerColor = getPlayerColor(props.player)

const icons: Record<string,string> = {

    aphrodite,
    arcadiancommunities,
    aridor,
    arklight,
    astrodrill,
    beginner,
    celestic,
    cheungshing,
    credicor,
    ecoline,
    helion,
    interplanetary,
    inventrix,
    manutech,
    miningguild,
    morningstarinc,
    pharmacy,
    phobolog,
    pointluna,
    polyphemos,
    poseidon,
    recyclon,
    robinson,
    saturnsystems,
    splice,
    stormcraft,
    teractor,
    tharsisrepublic,
    thorgate,
    unitedmarsinitiative,
    valleytrust,
    viron,
    vitor,

}



const topFactions = computed(() => {

    return [...props.factions]

        .filter(
            f => f.faction
        )

        .sort(
            (a,b)=>
            b.times_played-a.times_played
        )

        .slice(0,5)

})



const maxGames = computed(() => {

    return Math.max(
        ...topFactions.value.map(
            f=>f.times_played
        )
    )

})



function getFactionIcon(
    faction:string
){

    return icons[faction]

}


const chartData = computed(() => ({

    labels: topFactions.value.map(
        faction => faction.faction
    ),


    datasets: [

        {
            label: "Spiele",

            data: topFactions.value.map(
                faction => faction.times_played
            ),

            backgroundColor: "#e67e22",

            borderRadius: 8,

            barThickness: 18

        }

    ]

}))

function getWinRate(
    faction:any
){

    if(
        faction.times_played === 0
    )
        return 0


    return (
        faction.wins /
        faction.times_played *
        100
    )
    .toFixed(1)

}

const chartOptions = {

    indexAxis: "y",


    responsive: true,


    maintainAspectRatio: false,


    plugins: {

        legend: {

            display: false

        },


        tooltip: {

            callbacks: {

                label(context: any) {

                    const faction =
                        topFactions.value[context.dataIndex]


                    return [
                        `Spiele: ${faction.times_played}`,
                        `Siege: ${faction.wins}`
                    ]

                }

            }

        },


        datalabels: {

            anchor: "end",

            align: "right",


            color: "#444",


            font: {

                weight: "bold"

            },


            formatter(
                value: number,
                context: any
            ) {

                const faction =
                    topFactions.value[context.dataIndex]


                return `${value} (${faction.wins})`

            }

        }

    },


    scales: {

        x: {

            beginAtZero: true,


            ticks: {

                stepSize: 1

            },


            grid: {

                color: "rgba(128,128,128,0.25)"

            }

        },


        y: {

            grid: {

                display: false

            }

        }

    }

}


</script>


<style scoped>

.faction-chart {

    display:flex;

    flex-direction:column;

    gap:12px;

}



.faction-row {

    display:flex;

    align-items:center;

    gap:15px;

}



.icon-wrapper {

    position:relative;

    display:flex;

    align-items:center;

}



.faction-icon {

    width:45px;

    height:45px;

    object-fit:contain;

    transition:
        transform 0.2s ease;

}



.icon-wrapper:hover
.faction-icon {

    transform:scale(1.15);

}



/*
    Tooltip
*/

.tooltip {

    position:absolute;

    left:55px;

    top:50%;

    transform:
        translateY(-50%);


    background:#333;

    color:white;


    padding:10px 14px;


    border-radius:8px;


    display:flex;

    flex-direction:column;


    gap:4px;


    font-size:0.85rem;


    white-space:nowrap;


    opacity:0;


    pointer-events:none;


    transition:
        opacity 0.2s ease;


    z-index:10;

}



.icon-wrapper:hover
.tooltip {

    opacity:1;

}



.bar-container {

    flex:1;

    /* background:#eee; */

    border-radius:8px;

    overflow:hidden;

}



.bar {

    height:30px;

    background-color: var(--bar-color);

    border-radius:8px;

    display:flex;

    align-items:center;

    padding-left:10px;

    /* color:white; */

    font-weight:bold;

    text-align: right;

    transition:
        transform 0.2s ease,
        filter 0.2s ease;

}



.faction-row:hover .bar {

    transform:scaleY(1.1);

    filter:brightness(1.2);

}


</style>