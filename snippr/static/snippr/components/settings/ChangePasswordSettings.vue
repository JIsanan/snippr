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
        You can change your password using this module.
      </p>
    </div>
  </div>
  <div class="tile is-parent" v-if="messageUpdate">
    <div class="tile is-child is-1"></div>
    <div class="notification is-success tile is-child is-5">
      {{ messageUpdate }}
    </div>
  </div>
  <div class="form tile is-parent">
    <div class="tile is-child is-1"></div>
    <div class="tile is-child is-5">
      <FormInput
        type="password"
        label="New Password"
        v-model="password.newPword"
        placeholder=""
        inputClass="input has-background-white-bis"
        :value="password.newPword"
       />
       <FormInput
        type="password"
        label="Confirm Password"
        v-model="password.confirmPword"
        placeholder=""
        inputClass="input has-background-white-bis"
        :value="password.confirmPword"
       />
      <button class="button is-success submit" @click="onUpdate">
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
          newPword: '',
          confirmPword: ''
        },
        messageUpdate: '',
      };
    },
    computed: {
    },
    methods: {
      async onUpdate() {
      console.log(this.password)
        if(this.password.newPword != this.password.confirmPword){
          this.messageUpdate = "New password and Confirm password is not the same"
        }else{
          let ret = {}
          ret['password'] = this.password.newPword
          let headers = {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
          };
          let query = 'https://1b7c4ba8.ngrok.io/api/users/'
          let response = await axios.patch(query, ret, headers);
          if(response) {
            this.messageUpdate = "Successfully Updated"
          }
        }
      },
    }
  };
</script>

<style lang="scss" scoped>
  .info-description {
    font-size: .9rem;
  }
</style>
