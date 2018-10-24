<template>
	<div class="columns is-centered feed">
		<div class="column is-8">
			<div class="columns is-marginless is-mobile">
				<div class="column is-10 is-paddingless">
					<div class="tabs is-borderless">
						<ul>
							<li :class="{tabOption: !register}">
								<a>
									<span class="tab-item">Open</span>
									<span class="tag is-light">12</span>
								</a>
							</li>
							<li :class="{'is-active': register}">
								<a>
									<span class="tab-item">Closed</span>
									<span class="tag is-light">8</span>
								</a>
							</li>
							<li :class="{'is-active': !register}">
								<a>
									<span class="tab-item">All</span>
									<span class="tag is-light">4</span>
								</a>
							</li>
						</ul>
					</div>
				</div>
				<div class="column is-2 is-paddingless">
					<router-link :to="{ name: 'createissue' }" class="button is-success is-pulled-right">New Issue</router-link>
				</div>
			</div>
			<hr class="is-marginless">
			<div class="columns">
				<div class="column search-bar has-background-light">
					<FormInput
						type="text"
						class="has-addons"
						placeholder="Search"
						v-bind:value="search"
						inputClass="input"
						v-model="search"
						>
						<div slot="right-addon" class="control">
							<span class="select">
								<select>
									<option>Select dropdown</option>
									<option>With options</option>
								</select>
							</span>
						</div>
					</FormInput>
				</div>
			</div>
			<div class="columns has-bottom-border" v-for="snippet in snippets" :key="snippet.pk">
				<div class="column is-flex level is-marginless">
					<article class="media flex-vertical-center">
						<div class="media-left has-text-centered">
							<div>
								<span class="icon">
									<font-awesome-icon icon="caret-up" />
								</span>
							</div>
							<div class="is-size-5">
								<strong>{{ snippet.upvotes }}</strong>
							</div>
							<div>
								<span class="icon">
									<font-awesome-icon icon="caret-down" />
								</span>
							</div>
						</div>
						<div class="media-content">
							<div class="content">
								<div class="title is-size-5">
									<span class="tag is-success">Open</span>
									<router-link :to="{name: 'issue', params: { id:snippet.pk }}" class="has-text-primary">
										<strong>{{ snippet.title }}</strong>
									</router-link>
								</div>
								<p class="subtitle is-size-6">
									<small>Opened {{ timestamp(snippet.date_created) }} by</small>
									<router-link :to="{name:'user', params: {id:snippet.user_id} }"><small>{{ snippet.username }}</small></router-link>
									<span class="tag is-light">{{ snippet.language }}</span>
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
						<div>updated 2 days ago</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'source/plugins/axios';
import moment from 'moment';

import FormInput from "../components/_generics/FormInput.vue";
export default {
  name: "MainFeed",

  components: {
    FormInput
  },

  data() {
    return {
      tabOption: 0,
      search: "",
      searchbindType: "",
      snippets: null,
      register: false,
      languageFilter: null,
    };
  },

  methods: {
    timestamp(date) {
      return moment(date, moment.ISO_8601).fromNow();
    },
  },

  async mounted() {
    let headers = {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    };
    let languageFilter = this.languageFilter
    let query = 'http://127.0.0.1:8000/api/commit' + (languageFilter ? ('?language=' + this.languageFilter) : '/')
    let response = await axios.get(query, headers);
    this.snippets = response;
    console.log(this.snippets)
  }
};
</script>

<style scoped>
.tabs {
  margin-bottom: 0px;

  .tab-item {
    margin-right: 8px;
  }
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
</style>