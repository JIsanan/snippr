<template>
  <Card>
  	<div class="card-header tab-control">
  	</div>
  	<div class="card-content">
  		<p v-if="errorMessage" class="has-text-danger">{{errorMessage}}</p>
		<FormInput
		  type="text"
		  label="Username"
		  placeholder=""
		  :value="userData.username"
		  :inputClass="inputClass"
		  v-model="userData.username"
		/>
		 <FormInput
		  type="text"
		  label="Email"
		  placeholder=""
		  :value="userData.email"
		  inputClass="input"
		  v-model="userData.email"
		/>
		 <FormInput
		  type="text"
		  label="First Name"
		  placeholder=""
		  :value="userData.first_name"
		  inputClass="input"
		  v-model="userData.first_name"
		/>
		<FormInput
		  type="text"
		  label="Last Name"
		  placeholder=""
		  :value="userData.last_name"
		  inputClass="input"
		  v-model="userData.last_name"
		/>
		<FormInput
		  type="password"
		  label="Password"
		  placeholder=""
		  :value="userData.password"
		  inputClass="input"
		  v-model="userData.password"
		/>
		<FormInput
		  type="password"
		  label="Confirm Password"
		  placeholder=""
		  :value="confirmPassword"
		  inputClass="input"
		  v-model="confirmPassword"
		/>
 		<p class="is-size-7 has-text-centered">By clicking "Sign up", you acknowledge that you have read our updated Terms and Services, Privacy Policy and Cookies Policy, and that your continued use of the website is subject to these policies.</p>
		 <button class="button is-fullwidth is-success submit" v-on:click="onSubmit">Sign Up</button>
  	</div>
  </Card>
</template>

<script>
	import { mapActions } from 'vuex'
	import Card from '../Card.vue'
	import FormInput from '../_generics/FormInput.vue'
	export default {
	  name: 'RegisterForm',

	  components: {
	  	Card,
	  	FormInput
	  },

		data () {
		  return {
		    loggedIn: false,
		    userData: {
			    username: '',
			    email: '',
			    first_name: '',
			    last_name: '',
			    password: '',
		    },
		    confirmPassword: '',
		    errorMessage: '',
		    inputClass: 'input',
		    errorClass: 'is-danger',
		    valid: false,
		  }
		},
		methods: {
			...mapActions('auth', ['createUser', 'tryLogIn']),

			async onSubmit() {

				if(this.userData.username.trim() != '') {
					if(this.userData.password.trim() != '' && this.confirmPassword.trim() == this.userData.password.trim()) {
						const response = await this.createUser(this.userData);
						console.log(response.status)
						if(response.status == 400) {
							this.errorMessage = response.message[0]
						} else if (response.status == 200) {
							let payload = {
								username: this.userData.username,
								password: this.userData.password
							};
							const login = await this.tryLogIn(payload)
							if(login) {
								this.$router.push({ name: "feed" });
							}
						}

					} else {
						this.errorMessage = "Please input the correct password."
					}
				} else {
					this.errorMessage = "Please input a valid username."
				}
			}

		},
	}
</script>

<style lang="scss" scoped>

	.submit {
		margin-top: 24px;

		+ .level {
			margin-top: 12px;
		}
	}

	.tab-control{
		box-shadow: none;
	}

</style>
