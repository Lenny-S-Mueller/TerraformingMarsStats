<template>
    <aside class = "sidebar" :class="{ collapsed }">

        <h2 class = "sidebar-header" @click="emit('toggle')">
            <span v-if="collapsed"><font-awesome-icon icon = 'globe'/></span>
            <span v-if="!collapsed"><font-awesome-icon icon = 'globe'/> Terraforming Mars <font-awesome-icon icon = 'globe'/></span>
        </h2>
        
        <nav>
            <RouterLink to = "/dashboard">
                <font-awesome-icon icon = "chart-line"/><span v-if="!collapsed"> Übersicht</span>
            </RouterLink>
            
            <RouterLink to = "/games">
                <font-awesome-icon icon = "chess-board"/><span v-if="!collapsed"> Runden</span>
            </RouterLink>

            <RouterLink to = "/players">
                <font-awesome-icon icon="users" /><span v-if="!collapsed"> Spieler</span>
            </RouterLink>

            <RouterLink to = "/factions">
                <font-awesome-icon icon = "industry" /><span v-if="!collapsed"> Konzerne</span>
            </RouterLink>
        </nav>

    </aside>
</template>

<script setup lang="ts">
defineProps<{
    collapsed : boolean
}>()

const emit = defineEmits<{
    (e: 'toggle'): void
}>()
</script>

<style scoped>

.sidebar {  
  width: 320px;
  min-height: 100vh;
  padding: 2rem;
  background-color: #20262E;
  transition: width .3s ease;
  overflow: hidden;
}

.sidebar.collapsed {
    width: 130px;
    padding: 2rem;
    
}

.sidebar.collapsed nav a {
    justify-content: center;
    
    padding: .75rem 2rem;

    border-radius: 8px;

    align-items: center;
}

.sidebar-header {
    text-align: center;
    margin-bottom: 1.5rem;
}

.sidebar-header span {
    white-space: nowrap;
}

nav {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0rem;
}

nav a {

    height: 60px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;


    color: grey;

    text-decoration: none;

    padding: .75rem 2rem;

    border-radius: 8px;

    transition: .2s;
}

nav a:not(.router-link-exact-active):hover {
  background-color: #3A4352;
}

.router-link-exact-active {

    background-color: #238017;

    color: lightgray;

    font-weight: bold;

}

</style>