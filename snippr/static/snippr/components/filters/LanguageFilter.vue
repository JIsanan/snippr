<template>
	<span class="select">
		<select>
			<option v-for="language in languages">
				Select dropdown
			</option>
		</select>
	</span>
</template>

<script>
import axios from 'source/plugins/axios';
export default {
  name: "LanguageFilter",

  data() {
    return {
      languages: null,
    };
  },

  methods: {
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

<style>

</style>
