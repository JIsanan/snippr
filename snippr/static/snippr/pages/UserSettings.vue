<template>
	<section class="section">
		<div class="container is-fluid">
				<div class="whole columns is-fullheight">
		<div class="has-background-dark column is-3">
			<div class="columns is-centered">
				<div class="column is-11">
					<aside class="has-background-grey menu box">
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
		<div class="column is-9 tile is-ancestor">
			<div class="tile is-parent is-vertical right-content">
				<div class="tile is-child box is-white">
					<p class="title">
						<span class="icon is-size-5">
							<font-awesome-icon icon="wrench" />
						</span>
						<span class="title is-size-4">Manage your Account</span>
					</p>
					<p class="subtitle is-size-6">
						Lorem ipsum dolor sit amet, 
						consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
						tortor non, blandit congue massa. Donec fermentum lobortis 
						tempus. Etiam posuere feugiat tempor. Maecenas vestibulum eu 
						enim ac posuere. Ut aliquam nulla in blandit ultrices.
					</p>
				</div>
				<article class="person-info tile is-child notification box is-white">
					<figure class="img2 image is-64x64">
						<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
					</figure>
					<span class="header">
						<span class="title is-size-5">Personal Information</span><br>
						<p class="subtitle is-size-7">Lorem ipsum dolor sit amet, 
							consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
							tortor non, blandit congue massa. Donec fermentum lobortis 
							tempus. Etiam posuere feugiat tempor. Maecenas vestibulum eu 
							enim ac posuere. Ut aliquam nulla in blandit ultrices.
						</p>
					</span>
					<div class="form">
						<div class="control">
							<label class="label">First Name:</label>
							<input class="input fname" type="text" placeholder="">
						</div>
						<div class="control control2">	
							<label class="label">Last Name:</label>
							<input class="input lname" type="text" placeholder="">
						</div>
							<div class="control control2">
							<label class="label">Username:</label>
							<input class="input uname" type="text" placeholder="">
						</div>
						<div class="control control2">	
							<label class="label">Email Address:</label>
							<input class="input eadd" type="text" placeholder="">
						</div><br>
						<button class="button update-but submit">Update Settings</button>
					</div>
					<div class="form2">
						<div class="control">
							<label class="label">Password:</label>
							<input class="input fname" type="password" placeholder="">
						</div>
						<div class="control control2">	
							<label class="label">Change Password:</label>
							<input class="input lname" type="password" placeholder="">
						</div>
							<div class="control control2">
							<label class="label">Confirm Password:</label>
							<input class="input uname" type="password" placeholder="">
						</div><br>
						<button class="button update-but submit">Change Password</button>
					</div>
				</article>
			</div>
		</div>
	</div>
		</div>
	</section>
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
	.whole {
		background-color: #F7F4F4;
	}
	.menu{
		margin-top: 1.5rem;
	}
	.header{
		margin-top: 5px;
		margin-left: 10px;
		position:absolute;
	}
	.uppertile{
		margin-bottom:25px;
		padding-bottom: 50px;
	}
	.left-bar {
		display: inherit;
		/* height: 605px; */
		margin-top: 17px;
		margin-left: 10px;
		border-radius: 0%;
		background-color: #272F31;
	}
	.right-content{
		padding-top: 1.5rem;
	}
	.update-but, update-but:hover {
		background-color: #00d1b2;
		color:white;
	}
	.update-but {
		width: 170px;
		margin-bottom: 10px;
		height: 50px;
		border-radius: 40px;
	
	}
	.control {
		width: 350px;
		
	}
	.form, .form2 {
		margin-left: 72px;
	}
	.input {
		border-radius: 40px;
		height: 40px;
		text-align: center;
	}
	.input, .textarea{
		background-color: #F0F0F2;
	}
	.control2{
		margin-top: 5px;
	}
</style>