<template>
    <div class="columns is-centered feed">
    	<div class="column is-8">
    		<div class="columns is-marginless">
    			<p class="title">New Issue</p>
    		</div>
    		<hr>
    		<div class="columns is-centered">
    		  <div class="column is-12">
						<HorizontalFormInput
						  class="issue-input"
					    type="text"
					    label="Title"
					    placeholder="My First Issue"
					    v-bind:value="title"
					    inputClass="input"
					    v-model="title"
					  />
						<HorizontalFormInput
						  class="issue-input"
							type="textarea"
							label="Description"
							placeholder="My First Issue"
							v-bind:value="description"
							inputClass="textarea has-fixed-size"
							v-model="description"
							rows="5"
						/>
						<HorizontalFormInput
							class="issue-input"
							type="text"
							label="Tags"
							placeholder="Please use commas ( , ) to separate your tags"
							v-bind:value="tags"
							inputClass="input"
							v-model="tags"
						/>
						<hr>
						<HorizontalFormInput
							type="textarea"
							label="Code"
							placeholder="My First Issue"
							v-bind:value="code"
							inputClass="textarea has-fixed-size snippet"
							v-model="code"
							rows="5"
						/>
    		  </div>
    		</div>
    		<hr>
    		<div class="columns is-centered">
    			<div class="column is-12 is-flex justify-between">
    				<button class="button is-success">Submit Issue</button>
    				<button class="button is-outlined">Cancel</button>
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
	      title: '',
	      description: '',
	      tags: '',
	      code: '',
	    }
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

	.file-input {
		opacity: 0;
	}
</style>