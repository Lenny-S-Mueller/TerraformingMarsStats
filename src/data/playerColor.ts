export const playerColors: Record<string, string> = {

    Anton: "#2ecc71",
    Lars: "#e74c3c",
    Lenny: "#f1c40f",
    Maik: "#3498db",
    Matteo: "#9b59b6"

}


export function getPlayerColor(name:string):string {

    return playerColors[name] ?? "#777"

}