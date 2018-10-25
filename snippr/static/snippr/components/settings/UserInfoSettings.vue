<template>
  <article class="person-info tile is-vertical notification box is-white">
    <div class="tile is-white is-parent">
      <div class="icon tile is-child is-1  is-size-3">
        <font-awesome-icon icon="user" />
      </div>
      <div class="tile is-child is-vertical">
        <p class=" tile title is-size-5">
          Personal Information
        </p>
        <p class="subtitle info-description">
          Lorem ipsum dolor sit amet, 
          consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
          tortor non, blandit congue massa.
        </p>
      </div>
    </div>
    <div class="form tile is-parent">
      <div class="tile is-child is-1"></div>
      <div class="tile is-child is-5">
        <FormInput
          type="text"
          label="First Name"
          placeholder=""
          inputClass="input has-background-white-bis"
          :value="fname"
         />
         <FormInput
          type="text"
          label="Last Name"
          placeholder=""
          inputClass="input has-background-white-bis"
          :value="lname"
         />
         <FormInput
          type="text"
          label="Username"
          placeholder=""
          inputClass="input has-background-white-bis"
          :value="username"
         />
         <FormInput
          type="email"
          label="Email Address"
          placeholder=""
          inputClass="input has-background-white-bis"
          :value="email"
         />
        <button class="button submit is-success">
          Update Settings
        </button>
      </div>
    </div>
  </article>
</template>

<script>
  import { mapGetters } from 'vuex'
  import axios from "axios";

  import FormInput from "../_generics/FormInput.vue";

  export default {
    name: "UserInfoSettings",

    components: {
      FormInput
    },

    data() {
      return {
      };
    },
    computed: {
      ...mapGetters('auth', ['getUser']),
      fname() {
        return this.getUser ? this.getUser.first_name : ''
      },
      lname() {
        return this.getUser ? this.getUser.last_name : ''
      },
      username() {
        return this.getUser ? this.getUser.username : ''
      },
      email() {
        return this.getUser ? this.getUser.email : ''
      },
    },
    methods: {
    }
  };
</script>

<style lang="scss" scoped>
  .info-description {
    font-size: .9rem;
  }
</style>
