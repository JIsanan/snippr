<template>
    <div id="app" class="app">
    	<TheNavBar />
        <router-view class="app-page" />
    </div>
</template>

<script>
	import TheNavBar from './TheNavBar.vue'
    export default {
        name: 'App',

        components: {
        	TheNavBar,
        }
    };
</script>

<style scoped>
    .app-page {
        padding-top: 5rem;
    }
</style>
