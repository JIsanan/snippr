<template>
  <Card>
    <div class="card-content">
      <div class="notification is-danger" v-if="errorMessage">
        {{ errorMessage }}
      </div>
    <FormInput
      type="text"
      label="Username or Email"
      placeholder=""
      inputClass="input"
      v-model="username"
     />
     <FormInput
      type="password"
      label="Password"
      placeholder=""
      inputClass="input"
      v-model="password"
     />
     <button 
      class="button is-fullwidth is-success submit" 
      @click="login"
      >
        Submit
    </button>
     <div class="level">
      <div class="level-item">
        <a class="">Forget your password?</a>
      </div>
     </div>
    </div>
  </Card>
</template>

<script>
  import { mapActions } from 'vuex'
import axios from "axios";

import Card from "../Card.vue";
import FormInput from "../_generics/FormInput.vue";

export default {
  name: "LoginForm",

  components: {
    Card,
    FormInput
  },

  data() {
    return {
      loggedIn: false,
      username: "",
      password: "",
      errorMessage: ""
    };
  },

  methods: {
    ...mapActions('auth', ['tryLogIn']),
    async login() {    
      let payload = {
        username: this.username.trim(),
        password: this.password.trim()
      };

      const response = await this.tryLogIn(payload);
      this.username = ''
      this.password = ''
      if(response) {
        this.$router.push({ name: "feed" });
        console.log("hello")
      } else {
        this.errorMessage = "Invalid login or password."
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.submit {
  margin-top: 48px;

  + .level {
    margin-top: 12px;
  }
}

.tab-control {
  box-shadow: none;
}
</style>
