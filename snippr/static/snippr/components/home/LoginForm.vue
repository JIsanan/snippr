<template>
  <Card>
    <div class="card-header tab-control">
      
    </div>
    <div class="card-content">
    <FormInput
      type="text"
      label="Username or Email"
      placeholder=""
      v-bind:value="username"
      inputClass="input"
      v-model="username"
     />
     <FormInput
      type="text"
      label="Password"
      placeholder=""
      v-bind:value="password"
      inputClass="input"
      v-model="password"
     />
     <button class="button is-fullwidth is-success submit">Submit</button>
     <div class="level">
      <div class="level-item">
        <a class="">Forget your password?</a>
      </div>
     </div>
    </div>
  </Card>
</template>

<script>
  import Card from '../Card.vue'
  import FormInput from '../_generics/FormInput.vue'
  export default {
    name: 'LoginForm',

    components: {
      Card,
      FormInput
    },

    data () {
        return {
          loggedIn: false,
          username: '',
          password: ''
        }
     },
  }
</script>

<style lang="scss" scoped>

  .submit {
    margin-top: 48px;

    + .level {
      margin-top: 12px;
    }
  }

  .tab-control{
    box-shadow: none;
  }

</style>
