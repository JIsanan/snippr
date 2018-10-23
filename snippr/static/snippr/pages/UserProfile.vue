<template>
	<div class="columns is-centered feed">
		<div class="column is-8">
			<div class="columns is-centered" v-if="profile">
				<div class="column is-11">
					<div class="level">
						<div class="level-item">
							<figure>
						    <p class="image is-128x128">
						      <img src="https://bulma.io/images/placeholders/128x128.png">
						    </p>
						  </figure>
						</div>
					</div>
					<div class="level">
						<div class="level-item has-text-centered">
							<div>
								<p class="heading is-size-2"><strong>{{ profile.first_name }} {{ profile.last_name }}</strong></p>
								<p class="subheading is-size-4">@{{ profile.username }}</p>
							</div>
						</div>
					</div>
					<hr>
					<nav class="level">
					  <div class="level-item has-text-centered">
					    <div>
					    	<p class="heading">Issues Submitted</p>
					    	<p class="title">{{ profile.issue_count }}</p>
					    </div>
					  </div>
					  <div class="level-item has-text-centered">
					    <div>
					      <p class="heading">Following</p>
					      <p class="title">123</p>
					    </div>
					  </div>
					  <div class="level-item has-text-centered">
					    <div>
					      <p class="heading">Followers</p>
					      <p class="title">456K</p>
					    </div>
					  </div>
					  <div class="level-item has-text-centered">
					    <div>
					      <p class="heading">Likes</p>
					      <p class="title">789</p>
					    </div>
					  </div>
					</nav>
				</div>
			</div>
			<hr>
			<div class="column title is-size-4">
				Issues <span class="tag is-medium">120</span>
			</div>
			<hr>
			<div class="columns has-bottom-border">
				<div class="column is-flex level is-marginless is-paddingless">
					<article class="media flex-vertical-center">
						<div class="media-left has-text-centered">
							<div>
								<span class="icon">
									<font-awesome-icon icon="caret-up" />
								</span>
							</div>
							<div class="is-size-5">
								<strong>120</strong>
							</div>
						<div>
							<span class="icon">
								<font-awesome-icon icon="caret-down" />
							</span>
						</div>
						</div>
						<div class="media-content">
							<div class="content">
								<p class="title is-size-5">
									<span class="tag is-success">Open</span>
									<strong>Error 500: SMPT Host Undefined</strong>
								</p>
								<p class="subtitle is-size-6">
									<small>Opened 2 months ago by</small>
									<a><small>Xavier Luke Pulmones</small></a>
									<span class="tag is-light">Java</span>
									<span class="tag is-light">C#</span>
									<span class="tag is-light">C++</span>
								</p>
							</div>
						</div>
					</article>
				</div>
				<div class="column is-2 is-flex level is-marginless">
					<div class="level-item vertical flex-right">
						<span class="flex-vertical-center">
							<span class="icon">
								<font-awesome-icon icon="comment-alt" />
							</span>
							<span>120</span>
						</span>
						<div class="is-size-6">
							<small>updated 2 days ago</small>
						</div>
					</div>
				</div>
			</div>
			<div class="columns has-bottom-border">
				<div class="column is-flex level is-marginless is-paddingless">
					<article class="media flex-vertical-center">
						<div class="media-left has-text-centered">
							<div>
								<span class="icon">
									<font-awesome-icon icon="caret-up" />
								</span>
							</div>
							<div class="is-size-5">
								<strong>120</strong>
							</div>
							<div>
								<span class="icon">
									<font-awesome-icon icon="caret-down" />
								</span>
							</div>
						</div>
						<div class="media-content">
							<div class="content">
								<p class="title is-size-5">
									<span class="tag is-success">Open</span>
									<strong>Error 500: SMPT Host Undefined</strong>
								</p>
								<p class="subtitle is-size-6">
									<small>Opened 2 months ago by</small>
									<a><small>Xavier Luke Pulmones</small></a>
									<span class="tag is-light">Java</span>
									<span class="tag is-light">C#</span>
									<span class="tag is-light">C++</span>
								</p>
							</div>
						</div>
					</article>
				</div>
				<div class="column is-2 is-flex level is-marginless">
					<div class="level-item vertical flex-right">
						<span class="flex-vertical-center">
							<span class="icon">
								<font-awesome-icon icon="comment-alt" />
							</span>
							<span>120</span>
						</span>
						<div class="is-size-6">
							<small>updated 2 days ago</small>
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
		name: 'UserProfile',

		components: {
			FormInput,
		},

		data () {
			return {
				user: '',
			}
		},

		computed: {
			profile: function () {
				if(this.$route.path === '/myprofile/') {
					return this.$store.getters['auth/getUser']
				} else {
					return null
				}
			},
		},
	}
</script>

<style scoped>
	.feed {
		padding-top: 2rem;
	}

	.tabs {
		margin-bottom: 0px;

		.tab-item {
			margin-right: 8px;
		}
	}

	.description {
		margin: 24px 0px;

		.subtitle {
			white-space:pre-wrap; 
		}
	}

	.code {
		padding: 12px;
		background: hsl(0, 0%, 98%);
		border: 1px solid hsl(0, 0%, 86%);
		font-family: 'Source Code Pro', monospace;
		font-size: .8em;
	}

	.search-bar {
		margin: 12px;
	}

	.vertical {
		flex-direction: column;
	}

	.flex-right {
		align-items: flex-end   !important;
	}

	.flex-vertical-center {
		display: flex;
		align-items: center;
	}

	.has-bottom-border {
		border-bottom: 1px solid hsl(0, 0%, 86%);
	}
	.media-left {
		margin-right: 40px;
	}

	.code-line {
		margin-bottom: 0px !important;
	}

	.list-hr {
		margin: 1em 0;
	}
</style>