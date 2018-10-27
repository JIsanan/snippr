<template>
	<div class="columns is-centered feed" v-if="issue != null">
		<div class="column is-6 box">
			<div class="columns is-marginless">
				<div class="column is-3">
					<span class="tag is-success is-large">Open</span>
				</div>
				<div class="column">
					<div class="buttons is-right">
						<router-link :to="{ name: 'createissue' }" class="button is-danger is-outlined">Report Abuse</router-link>
						<router-link :to="{ name: 'createissue' }" class="button is-success is-outlined">Answer</router-link>
					</div>
				</div>
			</div>
			<hr class="is-marginless">
			<div class="columns is-marginless has-bottom-border main-issue">
				<div class="column is-flex level is-marginless">
						<article class="media flex-vertical-center">
							<VoteButtonSet
							 :upvotes="issue.upvotes"
							 :hasUpvoted="issue.has_upvoted"
							 :hasDownvoted="issue.has_downvoted"
							 :issueId="issue.pk"
							 class="media-left has-text-centered"
							/>
							<div class="media-content">
								<div class="content">
									<p class="title is-size-4"><strong>{{ issue.title }}</strong> </p>
									<p class="subtitle is-size-6">
										<small>Opened {{ timestamp(issue.date_created) }} by</small>
										<a><small>{{ issue.username }}</small></a>
										<span class="tag is-light">{{ issue.language_name }}</span>
									</p>
								</div>
							</div>
						</article>
				</div>
				<div class="column is-3 is-flex level is-marginless">
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
			<div class="columns is-centered is-marginless">
				<div class="column is-11">
					<div class="content description">
						<h4 class="title is-size-5">Description</h4>
						<p class="subtitle is-size-6">
							{{ issue.description }}
						</p>
					</div>
				</div>
			</div>
			<div class="columns is-centered">
				<div class="column is-11">
					<div class="content code">
						<p v-for="line in issue.snippet.code.split('\n')">
							{{ line }}
						</p>

					</div>
				</div>
			</div>
			<hr>
			<div class="column title">
				Answers
			</div>
			<hr>
			<div class="columns has-bottom-border">
				<div class="column is-flex level is-marginless">
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
									<p class="title is-size-4"><strong>Error 500: SMPT Host Undefined</strong> </p>
									<p class="subtitle">
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
				<div class="column is-3 is-flex level is-marginless">
					<div class="level-item vertical flex-right">
						<span class="flex-vertical-center">
								<span class="icon">
									<font-awesome-icon icon="comment-alt" />
								</span>
								<span>120</span>
						</span>
						<div>updated 2 days ago</div>
					</div>
				</div>
			</div>
			<div class="columns is-centered">
				<div class="column is-11">
					<div class="content description">
						<h4 class="title is-size-5">Description</h4>
						<p class="subtitle is-size-6">Lorem ipsum dolor sit amet, exerci posidonium ad his, eu vis equidem indoctum. Choro expetenda scribentur ex eum. Ei sed soleat voluptua theophrastus. No has meis tacimates. Eu erant ignota antiopam vix, case illum mandamus no quo. Vis ut tollit aperiri. At populo postea cum. Ne pro vero qualisque dissentiet. An magna verterem usu, ex has alterum aliquid. Cu vix appetere interesset, assum alterum pro no.
						</p>
					</div>
				</div>
			</div>
			<div class="columns is-centered">
				<div class="column is-11">
					<div class="content code">
						<p class="has-background-link code-line">printf("something");</p>
						<p class="code-line">printf("something");</p>
					</div>
				</div>
			</div>
		</div>
		<div class="column is-2 addon-content">
			<div class="box">
				<div class="content">
					<p class="title is-5">Related Issues</p>
					<ul class="related-list is-marginless">
						<li v-for="related in relatedIssues" :keys="related.pk">
							<span class="tag is-primary">{{ related.upvotes }}</span>
							<a class="is-size-6">
								{{ related.title }}
							</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

import FormInput from "../components/_generics/FormInput.vue";
import VoteButtonSet from "../components/_generics/VoteButtonSet.vue";
export default {
  name: "IssueDetails",

  components: {
    FormInput,
    VoteButtonSet
  },

  data() {
    return {
      tabOption: 0,
      search: "",
			searchType: "",
			issue: null,
			relatedIssues: {}
    };
  },
  methods: {
    isRegister() {
      this.register = true;
    },
    isSignin() {
      this.register = false;
		},
		timestamp(date) {
      return moment(date, moment.ISO_8601).fromNow();
    }
	},

	async mounted() {
		let headers = {
      headers: {
        'AUTHORIZATION': `Bearer ${localStorage.getItem('token')}`
      }
		};
		
		let response = await axios.get(`http://127.0.0.1:8000/api/commit/${this.$route.params.id}`, headers);

		if(response.data.detail != "Not Found.") {
			this.issue = response.data;
		}

		response = await axios.get(`http://127.0.0.1:8000/api/commit?language=${this.issue.language_name}`, headers)
		this.relatedIssues = response.data;
	}
};
</script>

<style scoped>
.main-issue {
	margin-top: 12px;
}
.addon-content {
	padding-top: 0px;
}
.related-list {
	list-style: none;
}
.tabs {
  margin-bottom: 0px;

  .tab-item {
    margin-right: 8px;
  }
}

.description {
  margin: 24px 0px;
}

.code {
  padding: 12px;
  background: hsl(0, 0%, 98%);
  border: 1px solid hsl(0, 0%, 86%);
  font-family: "Source Code Pro", monospace;
  font-size: 0.8em;
}

.search-bar {
  margin: 12px;
}

.vertical {
  flex-direction: column;
}

.flex-right {
  align-items: flex-end !important;
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
</style>