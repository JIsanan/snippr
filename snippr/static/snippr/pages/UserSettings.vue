<template>
	<div class="columns is-centered feed">
	</div>
</template>

<script>
	import FormInput from '../components/_generics/FormInput.vue'
	export default {
		name: 'UserSettings',

		components: {
			FormInput,
		},

		data () {
			return {

			}
		},
	}
</script>

<style scoped>
	.feed {
		padding-top: 2rem;
	}
</style>