<template>
	<div class="columns is-centered feed" v-if="issue != null">
		<div class="column is-6 box">
			<div class="columns is-marginless">
				<div class="column is-3">
					<span class="tag is-large" :class="{'is-success': !issue.is_resolved, 'is-light': issue.is_resolved}">
						<span v-if="!issue.is_resolved">Open</span>
						<span v-else>Closed</span>
					</span>
				</div>
				<div class="column">
					<div class="buttons is-right">
						<router-link :to="{ name: 'createissue' }" class="button is-danger is-outlined">Report Abuse</router-link>
						<router-link :to="{ name: 'answer', params: {c: issue.snippet.code, id: this.$route.params.id}}" class="button is-success is-outlined">Answer</router-link>
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
									<p class="title is-size-4"><strong>{{ issue.title }}</strong></p>
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
							<span class="flex-vertical-center" v-if="issue">
									<span class="icon">
										<font-awesome-icon icon="comment-alt" />
									</span>
									<span>{{ issue.comments.length }}</span>
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
						<pre class="code-line" v-for="(line, lineIndex) in issue.snippet.code.split('\n')" :key="lineIndex">
{{ line }}
						</pre>

					</div>
				</div>
			</div>
			<div class="columns is-marginless">
				<div class="column title is-size-4">
					Answers
				</div>
			</div>
			<div v-for="(comment, commentIndex) in issue.comments" class="comment" :key="comment.pk">
				<hr class="is-marginless">
				<div class="columns is-marginless">
					<div class="column level is-marginless">
							<article class="media flex-vertical-center">
								<div class="media-left has-text-centered">
									<button class="button is-success" :class="{'is-outlined': !comment.is_resolved}" v-if="showResolveBtn" @click="prompt(comment.pk, commentIndex)">
										<span class="icon">
											<font-awesome-icon icon="star" />	
										</span>
									</button>	
								</div>
								<div class="media-content">
									<div class="content">
										<p class="subtitle is-size-6">
											{{ comment.description }}
										</p>
										<p class="subtitle">
											<small>Answered {{ timestamp(comment.date_created) }} by</small>
											<a><small>{{ comment.username }}</small></a>
											<!-- <span class="tag is-light">Java</span>
											<span class="tag is-light">C#</span>
											<span class="tag is-light">C++</span> -->
										</p>
										<div class="code">
											<pre class="code-line" v-for="(line, lineIndex) in comment.code.split('\n')" :class="{'has-background-grey-dark': isChanged(lineIndex-1, commentIndex), 'has-text-white': isChanged(lineIndex-1, commentIndex)}" :key="lineIndex">
{{ line }}
											</pre>
											<!-- <p class="has-background-link code-line">printf("something");</p>
											<p class="code-line">printf("something");</p> -->
										</div>
									</div>
								</div>
							</article>
					</div>
				</div>
			</div>
			<div v-if="!hasComments" class="columns is-marginless">
				<hr class="is-marginless">
				<div class="column level">
					<div class="level-item vertical">
						<p class="image is-128x128 heading">
						      <img class="is-rounded" src="../assets/img/empty.svg">
						</p>
						<p class="subheading">
							No answers are currently submitted.
						</p>
					</div>
				</div>
			</div>
		</div>
		<div class="column is-2 addon-content">
			<div class="box">
				<div class="content">
					<p class="title is-5">Related Issues</p>
					<ul class="related-list is-marginless">
						<li v-for="related in relatedIssues" :key="related.pk">
							<span class="tag is-primary">{{ related.upvotes }}</span>
							<a class="is-size-6">
								{{ related.title }}
							</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<div class="modal" :class="{'is-active': isActive}">
			<div class="modal-background"></div>
			<div class="modal-content">
				<div class="card">
					<header class="card-header">
						<p class="card-header-title">
							Confirm
						</p>
						<a href="#" class="card-header-icon" aria-label="more options">
							<span class="icon">
								<i class="fas fa-angle-down" aria-hidden="true"></i>
							</span>
						</a>
					</header>
					<div class="card-content">
						<div class="content">
							Once marked as resolved, you <strong>cannot undo it</strong>. Are you sure this answer works?
							
						</div>
					</div>
					<footer class="card-footer">
						<a href="#" @click="resolveComment" class="card-footer-item">Yes</a>
						<a href="#" @click="() => { isActive = false; }" class="card-footer-item">Cancel</a>
					</footer>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import { mapGetters } from "vuex";

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
      relatedIssues: {},
      hasComments: false,
      isActive: false,
      resolvedCommentPk: -1,
      resolvedCommentIndex: -1
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
    },
    isChanged(lineIndex, commentIndex) {
      return lineIndex in this.issue.comments[commentIndex].line_changed;
    },
    prompt(commentPk, commentIndex) {
      this.isActive = true;
      this.resolvedCommentPk = commentPk;
      this.resolvedCommentIndex = commentIndex;
    },
    async resolveComment() {
      if (this.resolvedCommentPk > -1 && this.resolvedCommentIndex > -1) {
        let headers = {
          headers: {
            AUTHORIZATION: `Bearer ${localStorage.getItem("token")}`
          }
        };

        let payload = {
          track_id: this.resolvedCommentPk
        };

        let response = await axios.post(
          `http://127.0.0.1:8000/api/commit/${this.issue.pk}/resolve/`,
          payload,
          headers
        );

        if (response.data.message == "resolved") {
          this.issue.comments[this.resolvedCommentIndex].is_resolved = true;
        }
      }

      this.isActive = false;
    }
  },
  computed: {
    ...mapGetters("auth", ["isLoggedIn", "getUser"]),
    showResolveBtn() {
      let ret = false;

      if (this.getUser.username === this.issue.username) ret = true;

      return ret;
    }
  },

  async mounted() {
    let headers = {
      headers: {
        AUTHORIZATION: `Bearer ${localStorage.getItem("token")}`
      }
    };

    let response = await axios.get(
      `http://127.0.0.1:8000/api/commit/${this.$route.params.id}`,
      headers
    );

    if (response.data.detail != "Not Found.") {
      this.issue = response.data;
      this.hasComments = this.issue.comments.length == 0 ? false : true;
    }

    response = await axios.get(
      `http://127.0.0.1:8000/api/commit?limit=5&language=${
        this.issue.language_name
      }`,
      headers
    );
    this.relatedIssues = response.data.results.commits;
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
  line-height: normal;
  padding: 0;
  /* white-space: nowrap; */
  overflow: hidden;
}

.comment {
  margin-top: 12px;
}

.vote-count {
  margin: 12px 0;
}
</style>