<template>
  <Card>
    <div class="card-header tab-control">
      
    </div>
    <div class="card-content">
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
      password: ""
    };
  },

  methods: {
    async login() {
      let payload = {
        username: this.username.trim(),
        password: this.password.trim()
      };

      let response = await axios.post(
        "http://127.0.0.1:8000/api/login/",
        payload
      );

      if(response.data.message === "successful") {
        localStorage.setItem("token", response.data.token[0].key);
        this.$router.push({ name: 'feed' });
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
