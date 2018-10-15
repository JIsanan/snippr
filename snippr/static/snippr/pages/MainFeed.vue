<template>
    <div class="columns is-centered feed">
    	<div class="column is-8">
    		<div class="columns is-marginless">
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
					      <p>
					        <strong>Error 500: SMPT Host Undefined</strong> 
					        <br>
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
    					<div>updated 2 days ago</div>
    				</div>
    			</div>
    		</div>
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
					      <p>
					        <strong>Error 500: SMPT Host Undefined</strong> 
					        <br>
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
    					<div>updated 2 days ago</div>
    				</div>
    			</div>
    		</div>
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
					      <p>
					        <strong>Error 500: SMPT Host Undefined</strong> 
					        <br>
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
    					<div>updated 2 days ago</div>
    				</div>
    			</div>
    		</div>
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
					      <p>
					        <strong>Error 500: SMPT Host Undefined</strong> 
					        <br>
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
    					<div>updated 2 days ago</div>
    				</div>
    			</div>
    		</div>
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
					      <p>
					        <strong>Error 500: SMPT Host Undefined</strong> 
					        <br>
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
    					<div>updated 2 days ago</div>
    				</div>
    			</div>
    		</div>
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
					      <p>
					        <strong>Error 500: SMPT Host Undefined</strong> 
					        <br>
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
    					<div>updated 2 days ago</div>
    				</div>
    			</div>
    		</div>
    	</div>
    </div>
</template>

<script>
	import FormInput from '../components/_generics/FormInput.vue'
    export default {
        name: 'MainFeed',

        components: {
        	FormInput,
        },

		data () {
		    return {
		      tabOption: 0,
		      search: '',
		      searchType: '',
		    }
		 },
		 methods: {
		    isRegister () {
		    	this.register = true
		    },
		    isSignin () {
		    	this.register = false
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

	.search-bar {
		margin: 12px;
	}

	.vertical {
		flex-direction: column;
	}

	.flex-right {
		align-items: flex-end	!important;
	}

	.flex-vertical-center {
		display: flex;
		align-items: center;
	}

	.has-bottom-border {
		border-bottom: 1px solid hsl(0, 0%, 86%);
	}
</style>