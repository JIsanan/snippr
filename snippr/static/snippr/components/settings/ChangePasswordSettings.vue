<template>
<article class="person-info tile is-vertical notification box is-white">
  <div class="tile is-white is-parent">
    <div class="icon tile is-child is-1 is-size-3">
      <font-awesome-icon icon="key" />
    </div>
    <div class="tile is-child is-vertical">
      <p class=" tile title is-size-5">
        Change Password
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
        type="password"
        label="Password"
        placeholder=""
        inputClass="input has-background-white-bis"
        :value="password.oldPword"
       />
      <FormInput
        type="password"
        label="New Password"
        placeholder=""
        inputClass="input has-background-white-bis"
        :value="password.newPword"
       />
       <FormInput
        type="password"
        label="Confirm Password"
        placeholder=""
        inputClass="input has-background-white-bis"
        :value="password.confirmPword"
       />
      <button class="button is-success submit">
        Change Password
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
    name: "ChangePasswordSettings",

    components: {
      FormInput
    },

    data() {
      return {
        password: {
          oldPword: '',
          newPword: '',
          confirmPword: ''
        }
      };
    },
    computed: {
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
