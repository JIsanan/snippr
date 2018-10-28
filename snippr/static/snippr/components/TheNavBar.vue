<template>
  <nav class="navbar has-background-primary" role="navigation" aria-label="main navigation">
    <div class="container is-widescreen">
      <div class="navbar-brand">
        <div class="navbar-item">
          <router-link class="has-text-white" :to="{ name: 'feed' }">
          	<p class="is-size-4">
            	<strong>snippr</strong>
        	</p>
          </router-link>
        </div>
      </div>
      <div class="navbar-end">
        <div class="navbar-item" v-if="isLoggedIn">
          <router-link :to="{ name: 'createissue' }" class="button is-primary is-outlined is-inverted">
            <span class="icon">
              <font-awesome-icon icon="plus" />
            </span>
            <span>Create Issue</span>
          </router-link>
        </div>
      <div 
        v-if="isLoggedIn"
        class="navbar-item has-dropdown"
        v-bind:class="{'is-active': isOpen}"
      >
        <a :class="['navbar-link', {'has-text-white': isOpen}]" @click="toggle()" v-if="getUser">
          {{ getUser.username }}
        </a>
        <div class="navbar-dropdown" v-if="getUser">
          <a class="navbar-item" @click="routePage({ name: 'user', params: { id:getUser.id} })">Profile</a>
          <a class="navbar-item" @click="routePage({ name: 'settings' })">Settings</a>
          <a class="navbar-item" @click="logout">Log out</a>
        </div>
      </div>
      <div class="navbar-item" v-else>
        <div class="buttons">
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

    data () {
      return {
        isOpen: false,
      }
    },

    computed: {
      ...mapGetters('auth', ['isLoggedIn', 'getUser']),

    },

    methods: {
      ...mapActions('auth', ['removeJWT']),

      async logout() {
        const response = await this.removeJWT();
        if(response) {
          this.isOpen = false,
          this.$router.push({ name: 'home' });
        }
      },

      toggle: function() {
        this.isOpen = !this.isOpen;
      },

      routePage(params) {
        this.toggle();
        this.$router.push(params);
      }
    },

  }
</script>

<style lang="scss" scoped>

</style>
