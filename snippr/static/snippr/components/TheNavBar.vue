<template>
  <nav class="navbar has-background-primary" role="navigation" aria-label="main navigation">
    <div class="container is-fluid">
      <div class="navbar-brand">
        <div class="navbar-item">
          <router-link class="has-text-white" :to="{ name: 'feed' }"">
          	<p class="is-size-4">
            	<strong>snippr</strong>
        	</p>
          </router-link>
        </div>
      </div>
          <div class="navbar-end">
      <div class="navbar-item">
        <div v-if="isLoggedIn" class="buttons">
          <a class="button is-light" v-on:click="logout">
            Log out
          </a>
        </div>
        <div v-else class="buttons">
          <a class="button is-primary">
            <strong>Register</strong>
          </a>
          <a class="button is-light">
            Sign in
          </a>
        </div>
      </div>
    </div>
    </div>
  </nav>
</template>

<script>
  import { mapActions, mapGetters  } from 'vuex'
  export default {

    name: 'TheNavBar',

    computed: {
      ...mapGetters('auth', ['isLoggedIn']),

    },

    methods: {
      ...mapActions('auth', ['removeJWT']),

      async logout() {
        const response = await this.removeJWT();
        if(response) {
          this.$router.push({ name: 'home' });
        }
      }
    },
  }
</script>

<style>

</style>
