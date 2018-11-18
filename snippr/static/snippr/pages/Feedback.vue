<template>
    <div class="columns is-centered">
    	<div class="column is-8 box">
    		<div class="columns is-marginless">
    			<div class="column level">
						<div class="level-item vertical content">
							<p class="title has-text-primary">
								Give Your Feedback
							</p>
							<p class="subtitle"><small>We need your feedback to help this become better.</small></p>
						</div>
					</div>
    		</div>
    		<hr class="is-marginless">
    		<div class="columns is-centered is-marginless">
    		  <div class="column is-10">
						<HorizontalFormInput
						  class="issue-input"
							type="textarea"
							label="Message"
							placeholder="Write your feedback here!"
							v-bind:value="message"
							inputClass="textarea has-fixed-size"
							v-model="message"
							rows="5"
						/>
    		  </div>
    		</div>
    		<hr>
    		<div class="columns is-centered is-marginless">
    			<div class="column is-12 is-flex justify-between">
    				<button class="button is-success" @click="submit">Submit Feedback</button>
    				<button class="button is-outlined" @click="cancel">Cancel</button>
    			</div>
    		</div>
    	</div>
    </div>
</template>

<script>
import axios from 'axios';

import LanguageFilter from "../components/filters/LanguageFilter.vue";
import HorizontalFormInput from "../components/_generics/HorizontalFormInput.vue";
export default {
  name: "CreateIssue",

  components: {
    HorizontalFormInput,
    LanguageFilter
  },

  data() {
    return {
      message: "",
    };
  },

  methods: {
    async submit() {
      let payload = {
        message: this.message
      };

      let headers = {
        headers: {
          'AUTHORIZATION': `Bearer ${localStorage.getItem('token')}`
        }
      };

      let response = await axios.post('https://1b7c4ba8.ngrok.io/api/feedback/', payload, headers);
      console.log(response);
    },

    selectLanguage(value){
    	this.language = value
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