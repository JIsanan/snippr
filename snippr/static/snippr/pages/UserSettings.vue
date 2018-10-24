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
										<a class="has-text-white">
											<span class="icon">
												<font-awesome-icon icon="user" />
											</span>
											<span>Account Settings</span>
										</a>
									</li>
									<li>
										<a class="has-text-white">
											<span class="icon">
												<font-awesome-icon icon="key" />
											</span>
											<span>Change Password</span>
										</a>
									</li>
								</ul>
							</aside>
						</div>
					</div>
				</div>
				<div class="column is-6 tile is-ancestor is-paddingless">
					<div class="tile is-parent is-vertical right-content">
						<article class="person-info tile is-vertical notification box is-white">
							<div class="tile is-white is-parent">
								<div class="icon tile is-child is-1	 is-size-3">
									<font-awesome-icon icon="user" />
								</div>
								<div class="tile is-child is-vertical">
									<p class=" tile title is-size-5">
										Personal Information
									</p>
									<p class="subtitle info-description">
										Lorem ipsum dolor sit amet, 
										consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
										tortor non, blandit congue massa.
									</p>
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
							      v-model="user.fname"
							     />
							     <FormInput
							      type="text"
							      label="Last Name"
							      placeholder=""
							      inputClass="input has-background-white-bis"
							      v-model="user.lname"
							     />
							     <FormInput
							      type="text"
							      label="Username"
							      placeholder=""
							      inputClass="input has-background-white-bis"
							      v-model="user.username"
							     />
							     <FormInput
							      type="email"
							      label="Email Address"
							      placeholder=""
							      inputClass="input has-background-white-bis"
							      v-model="user.email"
							     />
									<button class="button submit is-success">
										Update Settings
									</button>
								</div>
							</div>
						</article>
						<article class="person-info tile is-vertical notification box is-white">
							<div class="tile is-white is-parent">
								<div class="icon tile is-child is-1 is-size-3">
									<font-awesome-icon icon="key" />
								</div>
								<div class="tile is-child is-vertical">
									<p class=" tile title is-size-5">
										Change Password
									</p>
									<p class="subtitle info-description">
										Lorem ipsum dolor sit amet, 
										consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
										tortor non, blandit congue massa.
									</p>
								</div>
							</div>
							<div class="form tile is-parent">
								<div class="tile is-child is-1"></div>
								<div class="tile is-child is-5">
									<FormInput
							      type="password"
							      label="Password"
							      placeholder=""
							      inputClass="input has-background-white-bis"
							      v-model="password.oldPword"
							     />
									<FormInput
							      type="password"
							      label="New Password"
							      placeholder=""
							      inputClass="input has-background-white-bis"
							      v-model="password.newPword"
							     />
							     <FormInput
							      type="password"
							      label="Confirm Password"
							      placeholder=""
							      inputClass="input has-background-white-bis"
							      v-model="password.confirmPword"
							     />
									<button class="button is-success submit">
										Change Password
									</button>
								</div>
							</div>
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
				user: {
					fname: '',
					lname: '',
					username: '',
					email: '',
				},
				password: {
					oldPword: '',
					newPword: '',
					confirmPword: ''
				}
			}
		},
	}
</script>

<style scoped>
	.menu{
		margin-top: 1.5rem;
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