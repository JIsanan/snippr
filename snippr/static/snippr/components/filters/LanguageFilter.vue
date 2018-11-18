<template>
	<span class="select">
		<select v-model="valueFilter" >
			<option value="All" v-if="hasFilterAll">All</option>
			<option v-for="language in languages" :value="language.name">
				{{language.name}}
			</option>
		</select>
	</span>
</template>

<script>
import axios from 'source/plugins/axios';
export default {
  name: "LanguageFilter",

  props: {
  	value: {
  		type: String,
  	},
  	hasFilterAll: {
  		type: Boolean
  	}
  },

  data() {
    return {
      languages: null,
    };
  },
  computed: {
    valueFilter: {
      get(){
        return this.value;
      },

      set(value) {
      	
        this.$emit('filter', value);
      }
    }
  },

  async mounted() {
    let headers = {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    };
    let languageFilter = this.languageFilter
    let query = 'https://1b7c4ba8.ngrok.io/api/language/'
    let response = await axios.get(query, headers);
    this.languages = response.results;
  }
};
</script>

<style>

</style>
