<template>
  <nav class="navbar has-background-primary" role="navigation" aria-label="main navigation">
    <div class="container is-widescreen">
      <div class="navbar-brand">
        <div class="navbar-item logo">
          <img class="is-rounded" src="../assets/img/logo.png">
        </div>
        <div class="navbar-item logo-name">
          <router-link class="has-text-white" :to="{ name: 'feed' }">
          	<p class="is-size-4">
            	<strong>snippr</strong>
        	</p>
          </router-link>
        </div>
        <div class="navbar-item" v-if="isLoggedIn">
          <FormInput
            type="text"
            class="has-addons"
            placeholder=""
            :value="search"
            inputClass="input"
            v-model="search"
            >
            <div slot="right-addon" class="control">
              <router-link :to="{name: 'feed', query: {title: search, status: 'Open'}}" class="button is-success">
                <span class="icon">
                  <font-awesome-icon icon="search" />
                </span>
              </router-link>
            </div>
          </FormInput>
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
        <a :class="['navbar-link', {'has-text-white': !isOpen}, {'has-text-grey-lighter': isOpen}]" @click="toggle()" v-if="getUser">
          <figure class="image navbar-item is-48x48">
            <img class="is-rounded avatar" src="../assets/img/avatars/boy-2.png">
          </figure>
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
  import FormInput from "../components/_generics/FormInput.vue";
  export default {

    name: 'TheNavBar',

    components: {
      FormInput,
    },

    data () {
      return {
        isOpen: false,
        search: '',
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

.logo {
  padding: 0.25rem;
}

.logo-name {
  padding-left: 0;
}

.avatar {
  background: white;
  padding: 2px;
}

</style>
