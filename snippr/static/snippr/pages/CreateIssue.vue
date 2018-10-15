<template>
    <div class="columns is-centered feed">
    	<div class="column is-8">
    		<div class="columns is-marginless">
    			<p class="title">New Issue</p>
    		</div>
    		<hr>
    		<div>
				<HorizontalFormInput
			      type="text"
			      label="Title"
			      placeholder="My First Issue"
			      v-bind:value="title"
			      inputClass="input"
			      v-model="title"
			     />
			     <HorizontalFormInput
			      type="textarea"
			      label="Description"
			      placeholder="My First Issue"
			      v-bind:value="desription"
			      inputClass="textarea has-fixed-size"
			      v-model="description"
			      rows="5"
			     />
			     <HorizontalFormInput
			      type="text"
			      label="Tags"
			      placeholder="Please use commas ( , ) to separate your tags"
			      v-bind:value="tags"
			      inputClass="input"
			      v-model="tags"
			     />
				<div class="file has-name is-right">
				  <label class="file-label">
				    <input class="file-input" type="file" name="resume">
				    <span class="file-cta">
				      <span class="file-icon">
				        <i class="fas fa-upload"></i>
				      </span>
				      <span class="file-label">
				        Choose a file…
				      </span>
				    </span>
				    <span class="file-name">
				      Screen Shot 2017-07-29 at 15.54.25.png
				    </span>
				  </label>
				</div>
    		</div>
    	</div>
    </div>
</template>

<script>
	import HorizontalFormInput from '../components/_generics/HorizontalFormInput.vue'
    export default {
        name: 'CreateIssue',

        components: {
        	HorizontalFormInput,
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