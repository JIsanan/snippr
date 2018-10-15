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
    				<button class="button is-success" @click="submit">Submit Issue</button>
    				<button class="button is-outlined" @click="cancel">Cancel</button>
    			</div>
    		</div>
    	</div>
    </div>
</template>

<script>
import axios from 'axios';

import HorizontalFormInput from "../components/_generics/HorizontalFormInput.vue";
export default {
  name: "CreateIssue",

  components: {
    HorizontalFormInput
  },

  data() {
    return {
      title: "",
      description: "",
      tags: "",
      code: ""
    };
  },

  methods: {
    async submit() {
      let payload = {
        title: this.title,
        // description: this.description,
        language: this.tags,
        code: this.code
      };

      let headers = {
        headers: {
          'AUTHORIZATION': `Token ${localStorage.getItem('token')}`
        }
      };

      let response = await axios.post('http://127.0.0.1:8000/api/commit/', payload, headers);
      console.log(response);

      if(response.data.message === "successfully created") {
        this.$router.push({ 
          name: 'issue', 
          params: { 
            id: response.data.pk
          } 
        });
      }
    },

    cancel() {
      this.$router.go(-1);
    }
  }
};
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
  align-items: flex-end !important;
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