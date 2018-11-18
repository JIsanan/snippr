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
          You can change your personal information using this module.
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
          type="text"
          label="First Name"
          placeholder=""
          inputClass="input has-background-white-bis"
          v-model="fname"
         />
         <FormInput
          type="text"
          label="Last Name"
          placeholder=""
          inputClass="input has-background-white-bis"
          v-model="lname"
         />
         <FormInput
          type="text"
          label="Username"
          placeholder=""
          inputClass="input has-background-white-bis"
          v-model="username"
         />
         <FormInput
          type="email"
          label="Email Address"
          placeholder=""
          inputClass="input has-background-white-bis"
          v-model="email"
         />
        <button class="button submit is-success" @click="onUpdate">
          Update Settings
        </button>
      </div>
    </div>
  </article>
</template>

<script>
  import { mapGetters } from 'vuex'
  import axios from 'source/plugins/axios';

  import FormInput from "../_generics/FormInput.vue";

  export default {
    name: "UserInfoSettings",

    components: {
      FormInput
    },

    data() {
      return {
        userData: {},
        messageUpdate: '',
      };
    },
    computed: {
      ...mapGetters('auth', ['getUser']),
      fname: {
        get(){
          return this.getUser ? this.getUser.first_name : ''
        },
        set(value){
          this.userData.first_name = value
        }
      },
      lname: {
        get(){
          return this.getUser ? this.getUser.last_name : ''
        },
        set(value){
          this.userData.last_name = value
        }
      },
      username: {
        get(){
          return this.getUser ? this.getUser.username : ''
        },
        set(value){
          this.userData.username = value
        }
      },
      email: {
        get(){
          return this.getUser ? this.getUser.email : ''
        },
        set(value){
          this.userData.email = value
        }
      },
    },
    methods: {
      async onUpdate() {
        let ret = {}
        ret['username'] = this.checkData(this.userData.username, this.username)
        ret['first_name'] = this.checkData(this.userData.first_name, this.fname)
        ret['last_name'] = this.checkData(this.userData.last_name, this.lname)
        ret['email'] = this.checkData(this.userData.email, this.email)
        let headers = {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        };
        let query = 'https://1b7c4ba8.ngrok.io/api/users/'
        let response = await axios.patch(query, ret, headers);
        if(response) {
          this.messageUpdate = "Successfully Updated"
          this.$store.dispatch('auth/getProfile');
        }
      },
      setData(data){
        console.log(data)
      },
      checkData(data, oldData){
        if(data) {
          if(data.trim() == '') {
            return oldData
          } else {
            return data.trim()
          }
        } else {
          return oldData
        }
      }
    }
  };
</script>

<style lang="scss" scoped>
  .info-description {
    font-size: .9rem;
  }
</style>
