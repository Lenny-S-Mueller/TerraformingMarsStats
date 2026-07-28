export interface Game {
    date: string
    player1: [string, number]
    player2: [string, number]
    player3: [string, number]
    player4: [string, number]
    player5: [string, number]
}

export const games: Game[] = [
    {
        date: "01.01.2026",
        player1: ["Lenny", 93],
        player2: ["Maik", 88],
        player3: ["Anton", 99],
        player4: ["", 0],
        player5: ["", 0],
    },
    {
        date: "08.01.2026",
        player1: ["Matteo", 91],
        player2: ["Maik", 60],
        player3: ["Anton", 102],
        player4: ["Lenny", 82],
        player5: ["", 0],
    },
    {
        date: "14.02.2026",
        player1: ["Maik", 93],
        player2: ["Lenny", 88],
        player3: ["Matteo", 99],
        player4: ["Anton", 90],
        player5: ["Lars", 52],
    },
    {
        date: "15.01.2026",
        player1: ["Matteo", 105],
        player2: ["Lenny", 102],
        player3: ["Maik", 101],
        player4: ["", 0],
        player5: ["", 0],
    }
]