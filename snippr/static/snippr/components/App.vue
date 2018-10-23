<template>
    <div id="app" class="app">
    	<TheNavBar />
        <router-view :key="$route.path" />
    </div>
</template>

<script>
    import {mapGetters, mapActions, mapMutations} from 'vuex';
	import TheNavBar from './TheNavBar.vue'
    export default {
        name: 'App',

        components: {
        	TheNavBar,
        },
        methods: {
            ...mapMutations('auth', ['setToken'])
        }
    };
</script>

<style scoped>

</style>
