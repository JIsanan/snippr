<template>
  <div id="app" class="app has-background-white-ter">
    <TheNavBar />
    <section class="section">
      <div class="container is-fluid">
        <router-view :key="$route.path" />
      </div>
    </section>  
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

  .app {
    min-height: 100vh;
  }

</style>
