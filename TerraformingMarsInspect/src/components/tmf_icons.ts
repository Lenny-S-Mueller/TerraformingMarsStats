import game_logo from "@/data/tfm-icons/game_logo.png"
import megacredits from "@/data/tfm-icons/megacredits.png"
import greenery from "@/data/tfm-icons/greenery.png"
import tf_rating from "@/data/tfm-icons/terraform_rating.png"
import victory_points from "@/data/tfm-icons/victorypoints.png"
import avatar from "@/data/tfm-icons/avatar.png"
import city from "@/data/tfm-icons/city.png"
import awards from "@/data/tfm-icons/awards2.png"
import milestones from "@/data/tfm-icons/milestone2.png"
import faction from "@/data/tfm-icons/faction.png"


export const icons = {

    game_logo: {
        name: "game_logo",
        icon: game_logo
    },

    megacredits: {
        name: "megacredits",
        icon: megacredits
    },

    greenery: {
        name: "greenery",
        icon: greenery
    },

    tf_rating: {
        name: "tf_rating",
        icon: tf_rating
    },

    victory_points: {
        name: "victory_points",
        icon: victory_points
    },

    avatar: {
        name: "avatar",
        icon: avatar
    },

    city: {
        name: "city",
        icon: city
    },

    milestones: {
        name: "milestones",
        icon: milestones
    },

    awards: {
        name: "awards",
        icon: awards
    },

    faction: {
        name: "faction",
        icon: faction
    },
}

export function getIcon(id: string){

    return icons[id]?.icon ?? id
}