<template>
    <div id="app" class="app">
    	<TheNavBar />
        <router-view />
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

</style>
