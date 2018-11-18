<template>
	<div class="columns is-centered feed">
		<div class="column is-8">
			<div class="columns level box" v-if="profile">
				<div class="column is-narrow level-left">
					<article class="media flex-vertical-center">
					  <figure class="media-left">
						    <p class="image is-128x128">
						      <img class="is-rounded avatar" src="../assets/img/avatars/boy-2.png">
						    </p>
						  </figure>
					  <div class="media-content">
					    <div class="content">
								<p class="title is-size-3 name"><strong>{{ profile.first_name }} {{ profile.last_name }}</strong></p>
								<p class="subtitle is-size-5">
									@{{ profile.username }}
								</p>
					    </div>
					  </div>
					</article>
				</div>
				<div class="column is-6 level-right">
					<nav class="level">
					  <div class="level-item has-text-centered">
					    <div>
					    	<p class="heading">Issues</p>
					    	<p class="title">{{ profile.issue_count }}</p>
					    </div>
					  </div>
					  <div class="level-item has-text-centered">
					    <div>
					      <p class="heading">Comments</p>
					      <p class="title">{{ profile.comment_count }}</p>
					    </div>
					  </div>
					  <div class="level-item has-text-centered">
					    <div>
					      <p class="heading">Resolved</p>
					      <p class="title">{{ profile.resolved_count }}</p>
					    </div>
					  </div>
					</nav>
				</div>
			</div>
			<hr class="is-marginless">
			<div class="columns">
				<div class="column title is-size-4 box">
					Recent issues
				</div>
			</div>
			<hr class="is-marginless">

			<div class="box snippet-list">
				<SnippetRow v-for="snippet in snippets" :snippet="snippet" :key="snippet.pk" />
			</div>
		</div>
	</div>
</template>

<script>
	import { mapActions, mapGetters  } from 'vuex'
	import SnippetRow from "../components/feed/SnippetRow.vue";
	import FormInput from '../components/_generics/FormInput.vue'
	export default {
		name: 'UserProfile',

		components: {
			FormInput,
    		SnippetRow,
		},

		data () {
			return {
				profile: null,
				snippets: null,
			}
		},

		async mounted() {
				if(this.$route.path === '/myprofile/') {
					return this.$store.getters['auth/getUser']
				} else {
					this.getInfo()
				}
			},

		methods: {
			...mapActions('user', ['getUserProfile']),
			async getInfo() {
				let response = await this.getUserProfile(this.$route.params.id);
		    	this.profile = response
		    	this.snippets = this.profile.issues
			}
		}
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

	.name {
		text-transform: uppercase;
		font-weight: 600;
	}

	.avatar {
		background: white;
		padding: 12px;
		box-shadow: 0px 0px 20px 2px rgba(grey, 0.1);
	}

	.snippet-list {
		padding-left: 40px;
		padding-right: 40px;
	}
</style>