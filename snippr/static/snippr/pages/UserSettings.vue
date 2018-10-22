<template>
	<div class="columns is-centered feed">
		<div class="column is-8">
			<div class="columns">
				<div class="column is-3">
					<aside class="menu box">
					  <p class="menu-label">
					    Settings
					  </p>
					  <ul class="menu-list">
					    <li><a>Account Settings</a></li>
					    <li><a>Change Password</a></li>
					  </ul>
					</aside>
				</div>
				<div class="column is-9 tile is-ancestor">
					    <div class="tile is-parent">
      <article class="tile is-child notification box is-white">
        <p class="title is-size-4">Manage your Account</p>
        <p class="subtitle is-size-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam massa nibh, ullamcorper eget tortor non, blandit congue massa. Donec fermentum lobortis tempus. Etiam posuere feugiat tempor. Maecenas vestibulum eu enim ac posuere. Ut aliquam nulla in blandit ultrices.</p>
      </article>
    </div>
				</div>
			</div>
		</div>
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