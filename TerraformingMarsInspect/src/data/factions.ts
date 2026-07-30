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



export const factions = {

    arcadia:{
        name:"Arcadia",
        icon: arcadiancommunities
    },

    aridor:{
        name:"Aridor",
        icon: aridor
    },
    
    arklight:{
        name:"Arklight",
        icon: arklight
    },

    astrodrill:{
        name:"AstroDrill",
        icon: astrodrill
    },

    beginner:{
        name:"Beginner",
        icon: beginner
    },

    cheungshing:{
        name:"Cheung Shing Mars",
        icon: cheungshing
    },

    credicor:{
        name:"Credicor",
        icon: credicor
    },

    ecoline:{
        name:"Ecoline",
        icon: ecoline
    },

    helion:{
        name:"Helion",
        icon: helion
    },

    interplanetary:{
        name:"Interplanetary",
        icon: interplanetary
    },

    inventrix:{
        name:"Inventrix",
        icon: inventrix
    },

    pharmacy:{
        name:"Pharmacy Union",
        icon: pharmacy
    },

    phobolog:{
        name:"PhoboLog",
        icon: phobolog
    },

    pointluna:{
        name:"PointLuna",
        icon: pointluna
    },

    polyphemos:{
        name:"Polyphemos",
        icon: polyphemos
    },

    poseidon:{
        name:"Poseidon",
        icon: poseidon
    },

    recyclon:{
        name:"Recyclon",
        icon: recyclon
    },

    saturnsystems:{
        name:"Saturn Systems",
        icon: saturnsystems
    },

    splice:{
        name:"Splice",
        icon: splice
    },

    stormcraft:{
        name:"Stormcraft",
        icon: stormcraft
    },

    teractor:{
        name:"Teractor",
        icon: teractor
    },

    tharsisrepublic:{
        name:"Tharsis Republic",
        icon: tharsisrepublic
    },

    thorgate:{
        name:"Thorgate",
        icon: thorgate
    },

    unitedmarsinitiative:{
        name:"United Mars Initiative",
        icon: unitedmarsinitiative
    },

    valleytrust:{
        name:"ValleyTrust",
        icon: valleytrust
    },

    vitor:{
        name:"Vitor",
        icon: vitor
    },
}


export function getFactionName(id:string){

    return factions[id]?.name ?? id

}


export function getFactionIcon(id:string){

    return factions[id]?.icon ?? "@/assets/icons/beginner.png"

}