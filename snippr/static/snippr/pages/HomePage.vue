<template>
    <div class="columns is-centered">
    	<div class="column is-3">
    		<div class="content">
    			<h1 class="title">Snippr</h1>
    			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in felis nunc. Nulla facilisi. Nam ornare laoreet nulla, non pretium nulla pretium lacinia. Donec pretium in ante ac interdum. Mauris nibh orci, rhoncus in lectus non, feugiat tempor quam. In a porttitor nisl. Mauris id ultrices turpis.</p>
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
</style>