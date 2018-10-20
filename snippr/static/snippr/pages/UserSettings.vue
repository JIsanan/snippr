<template>
	<div class="whole columns is-fullheight">
		<div class="column is-8">
			<div class="columns">
				<div class="row column is-4">
					<aside class="left-bar menu box">
						<p class="menu-label">
							Settings
						</p>
						<ul class="menu-list">
							<li>
								<a class="menu-list-tab 1">
									<figure class="img image is-32x32">
										<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
									</figure>
									<span class="spantab">Account Settings</span>
								</a>
							</li>
							<li>
								<a class="menu-list-tab 2">
									<figure class="img image is-32x32">
										<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
									</figure>
									<span class="spantab">Change Password</span>
								</a>
							</li>
						</ul>
					</aside>
				</div>
				<div class="main-column column is-12 tile is-ancestor">
					<div class="tile is-vertical is-13">
						<div class="tile">
							<div class="right-bar tile is-parent is-vertical">
								<article class="uppertile tile is-child notification box is-white">
									<figure class="img2 image is-32x32">
										<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
									</figure>
									<span class="header">
										<span class="title is-size-5">Manage your Account</span><br>
										<p class="header2 subtitle is-size-7">Lorem ipsum dolor sit amet, 
											consectetur adipiscing elit. Nam massa nibh, ullamcorper eget 
											tortor non, blandit congue massa. Donec fermentum lobortis 
											tempus. Etiam posuere feugiat tempor. Maecenas vestibulum eu 
											enim ac posuere. Ut aliquam nulla in blandit ultrices.
										</p>
									</span>
									
								</article>
								<article class="person-info tile is-child notification box is-white">
									<figure class="img2 image is-64x64">
										<img class="is-rounded" src="https://bulma.io/images/placeholders/128x128.png">
									</figure>
									<span class="header">
										<span class="title is-size-5">Personal Information</span><br>
										<p class="header2 subtitle is-size-7">Lorem ipsum dolor sit amet, 
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
	.whole {
		background-color: #F7F4F4;
	}
	.menu-label, .menu-list-tab {
		color: white;
	}
	.image {
		display: inline-block;
	}
	.spantab{
		margin-left: 5px;
		vertical-align:10px;
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
	.row {
		background-color: #202427;
		display: inline;
	}
	.right-bar {
		height: 200px;
		width:1060px;
		padding-bottom:0em;
		padding-right:0.8em !important;
	}
	.right-bar .tile .is-parent .is-vertical{
		padding-right:0em;
	}
	.tile.is-parent{
		padding-top: 1.5rem;
		padding-left: 0.75rem;
	}
	.tile.is-vertical > .tile.is-child:not(:last-child){
		margin-bottom: 1rem !important;
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
	.main-column {
		border-radius: 0%;
		padding-bottom:0em;
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