<template>
	<div class="columns is-centered feed">
		<div class="column is-8">
			<div class="columns is-marginless is-mobile">
				<div class="column is-10 is-paddingless">
					<div class="tabs is-borderless">
						<ul>
							<li :class="{'is-active': statusFilter == 'O'}">
								<router-link :to="{name: 'feed', query: submitFilter(filterset, {status: 'Open'})}">
									<span class="tab-item">Open</span>
									<span class="tag is-light">12</span>
								</router-link>
							</li>
							<li :class="{'is-active': statusFilter == 'C'}">
								<router-link :to="{name: 'feed', query: submitFilter(filterset, {status: 'Closed'})}">
									<span class="tab-item">Closed</span>
									<span class="tag is-light">12</span>
								</router-link>
							</li>
							<li :class="{'is-active': !statusFilter}">
								<router-link :to="{name: 'feed', query: submitFilter(filterset, {status: 'All'})}">
									<span class="tab-item">All</span>
									<span class="tag is-light">12</span>
								</router-link>
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
				<div class="column search-bar box">
					<FormInput
						type="text"
						class="has-addons"
						placeholder=""
						:value="search"
						inputClass="input"
						v-model="search"
						>
						<div slot="addon" class="control">
							<LanguageFilter 
								:value="languageFilter"
								@filter="filter"
							/>
						</div>
						<div slot="right-addon" class="control">
							<router-link :to="{name: 'feed', query: submitFilter(filterset, {filter: languageFilter, title: searchText()})}" class="button is-link">Search</router-link>
						</div>
					</FormInput>
				</div>
			</div>
			<div class="box snippet-list">
				<div class="columns snippet" v-for="snippet in snippets" :key="snippet.pk">
					<div class="column is-flex level is-marginless">
						<article class="media flex-vertical-center">
							<VoteButtonSet 
								class="media-left has-text-centered"
								:upvotes="snippet.upvotes"
								:hasUpvoted="snippet.has_upvoted"
							/>
							<div class="media-content">
								<div class="content">
									<div class="title is-size-5">
										<span 
										 :class="['tag',
															{'is-success': snippet.status == 'Open'},
															{'is-light': snippet.status == 'Closed'}
														 ]" >
											{{ snippet.status }}
										</span>
										<router-link :to="{name: 'issue', params: { id:snippet.pk }}" class="has-text-primary">
											<strong>{{ snippet.title }}</strong>
										</router-link>
									</div>
									<p class="subtitle is-size-6">
										<small>Opened {{ timestamp(snippet.date_created) }} by</small>
										<router-link :to="{name:'user', params: {id:snippet.user_id} }"><small>{{ snippet.username }}</small></router-link>
										<span class="tag is-light">{{ snippet.language_name }}</span>
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
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'source/plugins/axios';
import moment from 'moment';

import VoteButtonSet from "../components/_generics/VoteButtonSet.vue";
import FormInput from "../components/_generics/FormInput.vue";
import LanguageFilter from "../components/filters/LanguageFilter.vue";
export default {
  name: "MainFeed",

  components: {
    FormInput,
    LanguageFilter,
    VoteButtonSet
  },

  data() {
    return {
      tabOption: 0,
      search: "",
      filterset: {},
      snippets: null,
      register: false,
      statusFilter: 'O',
      languageFilter: 'All',
    };
  },

  methods: {
    timestamp(date) {
      return moment(date, moment.ISO_8601).fromNow();
    },
    filter(value){
    	this.languageFilter = value
    },
    submitFilter(old, add){
    	return Object.assign({}, old, add);
    },
    searchText(){
    	if(this.search == ""){
    		return "All";
    	} else {
    		return this.search
    	}
    }
  },

  async mounted() {

  	this.filterset = this.$route.query
    let headers = {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    };
    let languageFilter = null
    let query = 'http://127.0.0.1:8000/api/commit' 
    let route = this.$route.query
    if(route.filter || route.status || route.title){
    	query = query + '?'
	    if(route.filter && route.filter != 'All'){
	    	languageFilter = route.filter
	    	this.languageFilter = route.filter
	    	query = query + 'language=' + languageFilter + '&'
	    }
	    if(route.title && route.title != "All"){
	    	this.search = route.title
	    	query = query + 'title=' + this.search + '&'
	    }
	    if(route.status){
	    	let status = route.status
	    	if (status == 'Open') {
	    		query = query + 'status=O'
	    		this.statusFilter = 'O'
	    	} else if (status == 'Closed'){
	    		query = query + 'status=C'
	    		this.statusFilter = 'C'
	    	} else {
	    		this.statusFilter = null
	    	}
	    }
    }
    if(!this.$route.query.filter && !this.$route.query.status){
    	query = query + '/'
    }
    
    
    let response = await axios.get(query, headers);
    this.snippets = response;
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

.snippet-list {
	padding-left: 40px;
	padding-right: 40px;
}
.snippet{
	&:not(:last-child) {
  	border-bottom: 1px solid hsl(0, 0%, 86%);
	}
}
</style>