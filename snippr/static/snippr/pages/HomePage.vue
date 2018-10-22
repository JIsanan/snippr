<template>
    <div class="columns is-centered landing">
    	<div class="column is-4">
    		<div class="content">
    			<h1 class="title is-2">Welcome to Snippr!</h1>
    			<p class="is-size-5">Snippr is the all new network for developers to have elaborative and friendly environment which allows them to exchange knowledge related to anything about computer programming. With Snippr there's no need to manually keep track of code versions Snippr has got that all covered! Join us now!</p>
    		</div>
    	</div>
    	<div class="column is-3">
		    <div class="tabs is-toggle is-fullwidth">
			  <ul>
			    <li :class="{'is-active': !register}">
			    	<a v-on:click="isSignin">Sign in</a>
			    </li>
			    <li :class="{'is-active': register}">
			    	<a v-on:click="isRegister">Register</a>
			    </li>
			  </ul>
			</div>
			<RegisterForm v-if="register" ></RegisterForm>
			<LoginForm v-else ></LoginForm>
    	</div>
    </div>
</template>

<script>
	import LoginForm from '../components/home/LoginForm.vue'
	import RegisterForm from '../components/home/RegisterForm.vue'
    export default {
        name: 'HomePage',

        components: {
        	LoginForm,
        	RegisterForm
        },

		data () {
		    return {
		      register: true,
		    }
		 },
		 methods: {
		    isRegister () {
		    	this.register = true
		    },
		    isSignin () {
		    	this.register = false
		    }
		  }
    }
</script>

<style scoped>
	.tabs {
		margin-bottom: 0px;
	}
	.landing {
        padding-top: 4rem;
    }
</style>