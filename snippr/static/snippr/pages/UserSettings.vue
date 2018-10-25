<template>
	<div class="columns is-centered">
		<div class="column is-paddingless">
			<div class="columns is-centered tile is-ancestor">
				<div class="column is-9 tile is-parent">
				<div class="tile is-child box is-white">
					<p class="title">
						<span class="title is-size-4">Manage your Account</span>
					</p>
					<p class="subtitle info-description">
						Lorem ipsum dolor sit amet, 
						consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
						tortor non, blandit congue massa. Donec fermentum lobortis 
						tempus.
					</p>
				</div>
				</div>
			</div>
			<div class="columns is-centered">
				<div class="column is-3 tile is-ancestor">
					<div class="columns tile is-parent is-paddingless">
						<div class="column is-11 is-paddingless">
							<aside class="has-background-grey-dark menu box">
								<p class="menu-label has-text-white">
									Settings
								</p>
								<ul class="menu-list">
									<li>
										<router-link :to="{name: 'settings', query:{mode: 'userinfo'}}" :class="[{'is-active': mode == 'userinfo'}]">
											<span class="icon">
												<font-awesome-icon icon="user" />
											</span>
											<span>Account Settings</span>
										</router-link>
									</li>
									<li>
										<router-link :to="{name: 'settings', query:{mode: 'changepassword'}}" :class="[{'is-active': mode == 'changepassword'}]">
											<span class="icon">
												<font-awesome-icon icon="key" />
											</span>
											<span>Change Password</span>
										</router-link>
									</li>
								</ul>
							</aside>
						</div>
					</div>
				</div>
				<div class="column is-6 tile is-ancestor is-paddingless">
					<div class="tile is-parent is-vertical right-content">
						<UserInfoSettings v-if="mode == 'userinfo'"/>
						<ChangePasswordSettings v-if="mode == 'changepassword'"/>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import FormInput from '../components/_generics/FormInput.vue'
	import UserInfoSettings from '../components/settings/UserInfoSettings.vue'
	import ChangePasswordSettings from '../components/settings/ChangePasswordSettings.vue'
	export default {
		name: 'UserSettings',

		components: {
			FormInput,
			UserInfoSettings,
			ChangePasswordSettings
		},
		data () {
			return {
			}
		},
		computed: {
      mode() {
        return this.$route.query.mode ? this.$route.query.mode : 'userinfo'
      },
    },
	}
</script>

<style scoped>
	.menu{
		margin-top: 1.5rem;
		border-radius: 4px;
	}
	.info-description {
		font-size: .9rem;
	}
	.left-bar {
		padding-left: 0;
		padding-right: 0;
	}
	.right-content{
		padding-top: 1.5rem;
		padding-right: 0;
	}
</style>