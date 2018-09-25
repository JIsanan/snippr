<template>
    <div id="app" class="app">
    	<Navbar />
        <router-view class="app-page" />
    </div>
</template>

<script>
	import Navbar from './Navbar.vue';
	import {mapState, mapActions, mapGetters, mapMutations} from 'vuex';

    export default {
        name: 'App',

        components: {
        	Navbar,
        },
    };
</script>
<style scoped>
    .app-page {
        padding-top: 5rem;
    }
</style>
