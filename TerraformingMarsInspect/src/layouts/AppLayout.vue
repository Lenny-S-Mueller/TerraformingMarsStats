<template>
  <div class="app-layout">

    <Sidebar 
        :collapsed = "sidebarCollapsed"
        @toggle = "sidebarCollapsed = !sidebarCollapsed"
    />

    <main class="content">
      <router-view />
    </main>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Sidebar from '@/components/Sidebar.vue'

const sidebarCollapsed = ref(false)
</script>

<style scoped>

.app-layout {
  display: flex;
  min-height: 100vh;
}

.content {
  flex: 1;
  padding: 2rem;
}

</style>